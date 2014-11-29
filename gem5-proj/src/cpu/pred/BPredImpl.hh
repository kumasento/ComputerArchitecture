{
    // See if branch predictor predicts taken.
    // If so, get its target addr either from the BTB or the RAS.
    // Save off record of branch stuff so the RAS can be fixed
    // up once it's done.

    using TheISA::MachInst;

    bool pred_taken = false;
    TheISA::PCState target;

    ++lookups;
    DPRINTF(Branch, "[tid:%i] [sn:%i] %s ... PC %s doing branch "
            "prediction: This is bpred_unit_impl\n", tid, seqNum,
            inst->disassemble(instPC.instAddr()), instPC);

    void *bp_history = NULL;

    if (inst->isUncondCtrl()) {
        DPRINTF(Branch, "[tid:%i] Unconditional control.\n", tid);
        pred_taken = true;
        // Tell the BP there was an unconditional branch.
        uncondBranch(bp_history);

        if (inst->isReturn() && RAS[tid].empty()) {
            DPRINTF(Branch, "[tid:%i] RAS is empty, predicting "
                    "false.\n", tid);
            pred_taken = false;
        }
    } else {
        ++condPredicted;
        
        pred_taken = lookup(predPC.instAddr(), bp_history);
    }

    PredictorHistory predict_record(seqNum, predPC.instAddr(), pred_taken,
                                    bp_history, tid);

    // Now lookup in the BTB or RAS.
    if (pred_taken) {
        if (inst->isReturn()) {
            ++usedRAS;

            // If it's a function return call, then look up the address
            // in the RAS.
            TheISA::PCState rasTop = RAS[tid].top();
            target = TheISA::buildRetPC(instPC, rasTop);

            // Record the top entry of the RAS, and its index.
            predict_record.usedRAS = true;
            predict_record.RASIndex = RAS[tid].topIdx();
            predict_record.RASTarget = rasTop;

            assert(predict_record.RASIndex < 16);

            RAS[tid].pop();

            DPRINTF(Branch, "[tid:%i]: Instruction %s is a return, "
                    "RAS predicted target: %s, RAS index: %i.\n",
                    tid, instPC, target,
                    predict_record.RASIndex);
        } else {
            ++BTBLookups;

            if (inst->isCall()) {

                RAS[tid].push(instPC);
                predict_record.pushedRAS = true;

                // Record that it was a call so that the top RAS entry can
                // be popped off if the speculation is incorrect.
                predict_record.wasCall = true;

                DPRINTF(Branch, "[tid:%i]: Instruction %s was a call"
                        ", adding %s to the RAS index: %i.\n",
                        tid, instPC, predPC,
                        RAS[tid].topIdx());
            }

            if (inst->isCall() &&
                inst->isUncondCtrl() &&
                inst->isDirectCtrl()) {
                target = inst->branchTarget(instPC);
            } else if (BTB.valid(predPC.instAddr(), asid)) {
                ++BTBHits;

                // If it's not a return, use the BTB to get the target addr.
                target = BTB.lookup(predPC.instAddr(), asid);

                DPRINTF(Branch, "[tid:%i]: [asid:%i] Instruction %s "
                        "predicted target is %s.\n",
                        tid, asid, instPC, target);
            } else {
                DPRINTF(Branch, "[tid:%i]: BTB doesn't have a "
                        "valid entry, predicting false.\n",tid);
                pred_taken = false;
            }
        }
    }

    if (pred_taken) {
        // Set the PC and the instruction's predicted target.
        predPC = target;
    }
    DPRINTF(Branch, "[tid:%i]: [sn:%i]: Setting Predicted PC to %s.\n",
            tid, seqNum, predPC);

    predHist[tid].push_front(predict_record);

    DPRINTF(Branch, "[tid:%i] [sn:%i] pushed onto front of predHist "
            "...predHist.size(): %i\n",
            tid, seqNum, predHist[tid].size());

    return pred_taken;
}
