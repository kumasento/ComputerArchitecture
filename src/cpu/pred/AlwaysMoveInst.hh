{
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

        pred_taken = false;
    }
    return pred_taken;
}
