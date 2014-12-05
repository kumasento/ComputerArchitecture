# configuration scrpts learning
# from blank

# import everything needed
import optparse
import sys
import os
import m5
from m5.defines import buildEnv
from m5.objects import *
from m5.util import addToPath

addToPath('../common')

import Options
import Simulation
import CacheConfig
from Caches import *
import spec2006
import MemConfig

# insert self defination options
parser = optparse.OptionParser()
Options.addCommonOptions(parser)
Options.addSEOptions(parser)
(options, args) = parser.parse_args() 
#print help(options)

#option setting

##options.cpu_type = 'detailed'
#options.cpu_type = 'inorder'
## arm_detailed uses the o3_ARM_v7a cache, else Cache.
#options.caches = 'caches'
##options.l1d_size = '64kB' #'32kB'
##options.l1i_size = '64kB' #'32kB'
#options.l1d_size = '1024B' #'32kB'
#options.l1i_size = '1024B' #'32kB'
#
##options.l2cache = 'True'
##options.l2_size = '1MB' #'2MB' #'512kB'
#options.l2cache = 'True'
#options.l2_size = '1kB' #'2MB' #'512kB'
#
#options.l3cache = 'True'
#options.l3_size = '8MB'

#system setting after options setting

apps = []
multiprocesses = []
numThreads = 1

if options.bench:
    apps = options.bench.split("-")
    for app in apps:
#       pdb.set_trace()
        if app == '400.perlbench':
            process = spec2006.perlbench()
        elif app == '401.bzip2':
            process = spec2006.bzip2()
        elif app == '403.gcc':
            process = spec2006.gcc()
        elif app == '410.bwaves':
            process = spec2006.bwaves()
        elif app == '416.gamess':
            process = spec2006.gamess()
        elif app == '429.mcf':
            process = spec2006.mcf()
        elif app == '433.milc':
            process = spec2006.milc()
        elif app == '434.zeusmp':
            process = spec2006.zeusmp()
        elif app == '435.gromacs':
            process = spec2006.gromacs()
        elif app == '436.cactusADM':
            process = spec2006.cactusADM()
        elif app == '437.leslie3d':
            process = spec2006.leslie3d()
        elif app == '444.namd':
            process = spec2006.namd()
        elif app == '445.gobmk':
            process = spec2006.gobmk()
        elif app == '450.soplex':
            process = spec2006.soplex()
        elif app == '453.povray':
            process = spec2006.povray()
        elif app == '454.calculix':
            process = spec2006.calculix()
        elif app == '456.hmmer':
            process = spec2006.hmmer()
        elif app == '458.sjeng':
            process = spec2006.sjeng()
        elif app == '459.GemsFDTD':
            process = spec2006.GemsFDTD()
        elif app == '462.libquantum':
            process = spec2006.libquantum()
        elif app == '464.h264ref':
            process = spec2006.h264ref()
        elif app == '465.tonto':
            process = spec2006.tonto()
        elif app == '470.lbm':
            process = spec2006.lbm()
        elif app == '471.omnetpp':
            process = spec2006.omnetpp()
        elif app == '473.astar':
            process = spec2006.astar()
        elif app == '481.wrf':
            process = spec2006.wrf()
        elif app == '482.sphinx3':
            process = spec2006.sphinx3()
        elif app == '998.specrand':
            process = spec2006.specrand_i()
        elif app == '999.specrand':
            process = spec2006.specrand_f()
        #else:
            #process = LiveProcess()
            #process.executable = '/home/chao/Research/gem5_stable/tests/test-progs/myhello/'+app
            #process.cmd = [process.executable]

        else:
            print "unkown benchamarks"
            sys.exit(1)
        multiprocesses.append(process)

(CPUClass, test_mem_mode, FutureClass) = Simulation.setCPUClass(options)
CPUClass.numThreads = numThreads
np = options.num_cpus
system = System(cpu = [CPUClass(cpu_id=i) for i in xrange(np)],
                mem_mode = test_mem_mode,
                mem_ranges = [AddrRange(options.mem_size)],
                cache_line_size = options.cacheline_size)
        

system.voltage_domain = VoltageDomain(voltage = options.sys_voltage)

system.clk_domain = SrcClockDomain(clock =  options.sys_clock,
                                   voltage_domain = system.voltage_domain)


system.cpu_voltage_domain = VoltageDomain()

system.cpu_clk_domain = SrcClockDomain(clock = options.cpu_clock,
                                       voltage_domain =
                                       system.cpu_voltage_domain)

for cpu in system.cpu:
    cpu.clk_domain = system.cpu_clk_domain

# Sanity check
if options.fastmem and (options.caches or options.l2cache):
    fatal("You cannot use fastmem in combination with caches!")

# assign workload
if options.smt:
    assert(options.cpu_type == "detailed" or options.cpu_type == "inorder")

#
#if options.num_cpus > 1 and options.smt == False:
#    for i in xrange(np):
#        system.cpu[i].workload = multiprocesses[i]
#elif options.num_cpus == 1 and options.smt == True:
#    system.cpu[0].createThreads()
#    system.cpu[0].workload = multiprocesses
#elif options.num_cpus == 1:
#    system.cpu[0].workload = multiprocesses[0]

for i in xrange(np):
    if options.smt:
        system.cpu[i].workload = multiprocesses
    elif len(multiprocesses) == 1:
        system.cpu[i].workload = multiprocesses[0]
    else:
        system.cpu[i].workload = multiprocesses[i]

    if options.fastmem:
        system.cpu[i].fastmem = True

    if options.simpoint_profile:
        system.cpu[i].simpoint_profile = True
        system.cpu[i].simpoint_interval = options.simpoint_interval

    if options.checker:
        system.cpu[i].addCheckerCpu()

    system.cpu[i].createThreads()


#Run
#root = Root(full_system = False, system = system)
#m5.instantiate(root)
#exit_event = m5.simulate()
#print 'Exiting @ tick', m5.curTich(), 'because', exit_event.getCause()

MemClass = Simulation.setMemClass(options)
system.membus = CoherentBus()
system.system_port = system.membus.slave
CacheConfig.config_cache(options, system)
MemConfig.config_mem(options, system)

root = Root(full_system = False, system = system)
Simulation.run(options, root, system, FutureClass)
