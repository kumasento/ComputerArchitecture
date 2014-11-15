{
    DPRINTF(Branch, "[tid:%i] [sn:%i] %s ... PC %s no branch "
            "prediction, predPC is %s\n", tid, seqNum,
            inst->disassemble(instPC.instAddr()), instPC, predPC);

    return false;
}
