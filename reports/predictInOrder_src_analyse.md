#predictInOrder()源码分析

##参数列表：

* `StaticInstPtr` 存储与ISA相关的数据类
* `	InstSeqNum` 
* `TheISA::PCState` 存储PC相关数据，在`src/arch`里定义
* `ThreadID` 线程Id，一般为1

##流程分析：

###1.预处理阶段：

输出当前指令的状态：

	DPRINTF(Branch, "[tid:%i] [sn:%i] %s ... PC %s doing branch "                    
             "prediction\n", 
             tid, 
             seqNum,
             inst->disassemble(instPC.instAddr()), 
             instPC);

样例：

1. 条件判断指令（返回指令）
		
		[tid:0] [sn:9454] ret        (r26) ... 
		PC (0x120013944=>0x120013948) doing branch prediction
2. 条件判断指令：

		[tid:0] [sn:9448] beq        r0,0x120013934 ... 
		PC (0x12001392c=>0x120013930) doing branch prediction
3. 分析：
	* `inst->disassemble(instPC.instAddr())` 返回的是指令对应的字符串
	* `instPC` 对应 (当前PC)=>(PC + 4)
	
###2.获取pred_taken

1. 如果是非条件判断指令：
		
	一般设置pred_taken为true，除非当前指令为**返回指令且RAS为空**

		DPRINTF(Branch, "[tid:%i] Unconditional control.\n", tid);
		pred_taken = true;
		// Tell the BP there was an unconditional branch.
		uncondBranch(bp_history);
		
		if (inst->isReturn() && RAS[tid].empty()) {
		    DPRINTF(Branch, "[tid:%i] RAS is empty, predicting "
		            "false.\n", tid);
		    pred_taken = false;
		}
	
2. 条件判断指令：

	* 增加对预测的条件判断指令计数值(condPredicted)，执行lookup

			++condPredicted; 
			pred_taken = lookup(predPC.instAddr(), bp_history);
			
	* lookup的定义取决于算法：
		* 对于tournament算法
		* 对于2bit_local算法