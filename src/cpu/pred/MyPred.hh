/*
 * Copyright (c) 2011 ARM Limited
 * All rights reserved
 *
 * The license below extends only to copyright in the software and shall
 * not be construed as granting a license to any other intellectual
 * property including but not limited to intellectual property relating
 * to a hardware implementation of the functionality of the software
 * licensed hereunder.  You may use the software subject to the license
 * terms below provided that you ensure that this notice is replicated
 * unmodified and in its entirety in all distributions of the software,
 * modified or unmodified, in source code or in binary form.
 *
 * Copyright (c) 2004-2006 The Regents of The University of Michigan
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met: redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer;
 * redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution;
 * neither the name of the copyright holders nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * Authors: Kevin Lim
 *          Timothy M. Jones
 *          Nilay Vaish
 */

#ifndef __CPU_PRED_MY_PRED_HH__
#define __CPU_PRED_MY_PRED_HH__

#include <vector>

#include "base/types.hh"
#include "cpu/pred/bpred_unit.hh"
#include "cpu/pred/sat_counter.hh"

class MyBP : public BPredUnit
{
  public:
    MyBP(const Params *params);

    bool lookup(Addr branch_addr, void * &bp_history);
    void uncondBranch(void * &bp_history);
    void btbUpdate(Addr branch_addr, void * &bp_history);
    void update(Addr branch_addr, bool taken, void *bp_history, bool squashed);
    void squash(void *bp_history);
    inline unsigned readGlobalHist() { return globalHistory; }
    virtual bool predictInOrder(StaticInstPtr &inst, const InstSeqNum &seqNum,
                          int asid, TheISA::PCState &instPC,
                          TheISA::PCState &predPC, ThreadID tid);

  private:
    inline bool getPrediction(uint8_t &count);

    inline unsigned calcLocHistIdx(Addr &branch_addr);
    inline void updateGlobalHistTaken();
    inline void updateGlobalHistNotTaken();
    inline void updateLocalHistTaken(unsigned local_history_idx);
    inline void updateLocalHistNotTaken(unsigned local_history_idx);
    struct BPHistory {
#ifdef DEBUG
        BPHistory()
        { newCount++; }
        ~BPHistory()
        { newCount--; }

        static int newCount;
#endif
        unsigned globalHistory;
        unsigned localHistory;
        bool localPredTaken;
        bool globalPredTaken;
        bool globalUsed;
    };

    static const int invalidPredictorIndex = -1;
    std::vector<SatCounter> localCtrs;

    unsigned localPredictorSize;
    unsigned localPredictorMask;
    unsigned localCtrBits;

    std::vector<unsigned> localHistoryTable;

    unsigned localHistoryTableSize;
    unsigned localHistoryBits;

    std::vector<SatCounter> globalCtrs;

    unsigned globalPredictorSize;
    unsigned globalCtrBits;
    unsigned globalHistory;
    unsigned globalHistoryBits;
    unsigned globalHistoryMask;
    unsigned choiceHistoryMask;
    unsigned historyRegisterMask;

    std::vector<SatCounter> choiceCtrs;

    unsigned choicePredictorSize;
    unsigned choiceCtrBits;
    unsigned instShiftAmt;
    unsigned localThreshold;
    unsigned globalThreshold;
    unsigned choiceThreshold;
};

#endif // __CPU_PRED_MY_PRED_HH__
