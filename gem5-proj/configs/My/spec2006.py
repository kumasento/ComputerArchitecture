#Mybench.py
#Modified by Shuihan 
#Used for SPEC cpu 2006 benchmark test.

import m5
from m5.objects import *

BenchRoot_dir='../cpu2006/'
binary_dir = '/run/run_base_ref_alpha-fake.0000/'
Output_dir = '../'

#400.perlbench
def perlbench():
    process = LiveProcess()
    process.executable =  BenchRoot_dir+'400.perlbench'+binary_dir+'perlbench_base.alpha-fake'
    process.cmd = [process.executable] + ['-I./lib', 'attrs.pl']
    process.output = 'attrs.out'
    return process

#401.bzip2
def bzip2():
    process = LiveProcess()
    process.executable = BenchRoot_dir+'401.bzip2'+binary_dir+'bzip2_base.alpha-fake'
    data= BenchRoot_dir+'401.bzip2'+binary_dir+'chicken.jpg'
    process.cmd = [process.executable] + [data, '30']
    process.output = 'chicken.jpg.out'
    return process 

#403.gcc
def gcc():
    process = LiveProcess()
    process.executable =  BenchRoot_dir+'403.gcc'+binary_dir+'gcc_base.alpha-fake'
    data= BenchRoot_dir+'403.gcc'+binary_dir+'166.i'
    output='./cccp.s'
    process.cmd = [process.executable] + [data]+['-o',output]
    process.output = 'ccc.out'
    return process

#410.bwaves
def bwaves():
    process = LiveProcess()
    process.executable =  BenchRoot_dir+'410.bwaves'+binary_dir+'bwaves_base.alpha-fake'
    process.cmd = [process.executable]
    return process

#416.gamess
def gamess():
    process = LiveProcess()
    process.executable =  BenchRoot_dir+'416.gamess'+binary_dir+'gamess_base.alpha-fake'
    process.cmd = [process.executable]
    process.input= BenchRoot_dir+'416.gamess'+binary_dir+'cytosine.2.config'
    process.output='cytosine.2.config.out'
    return process;

#429.mcf
def mcf():
    process = LiveProcess()
    process.executable =  BenchRoot_dir+'429.mcf'+binary_dir+'mcf_base.alpha-fake'
    data= BenchRoot_dir+'429.mcf'+binary_dir+'inp.in'
    process.cmd = [process.executable] + [data]
    process.output = 'inp.out'
    return process

#433.milc
def milc():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'433.milc'+binary_dir+'milc_base.alpha-fake'
    stdin= BenchRoot_dir+'433.milc'+binary_dir+'su3imp.in'
    process.cmd = [process.executable]
    process.input=stdin
    process.output='su3imp.out'
    return process

#434.zeusmp // need more physical memory
def zeusmp():
    process=LiveProcess()
    process.executable =  BenchRoot_dir+'434.zeusmp'+binary_dir+'zeusmp_base.alpha-fake'
    process.cmd = [process.executable]
    process.output = 'zeusmp.stdout'
    return process

#435.gromacs
def gromacs():
    process = LiveProcess()
    process.executable = BenchRoot_dir+'435.gromacs'+binary_dir+'gromacs_base.alpha-fake'
    data= BenchRoot_dir+'435.gromacs'+binary_dir+'gromacs.tpr'
    process.cmd = [process.executable] + ['-silent','-deffnm',data,'-nice','0']
    return process

#436.cactusADM
def cactusADM():
     process = LiveProcess()
     process.executable =  BenchRoot_dir+'436.cactusADM'+binary_dir+'cactusADM_base.alpha-fake'
     data=BenchRoot_dir+'436.cactusADM'+binary_dir+'benchADM.par'
     process.cmd = [process.executable] + [data]
     process.output = 'benchADM.out'
     return process

#437.leslie3d
def leslie3d():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'437.leslie3d'+binary_dir+'leslie3d_base.alpha-fake'
    stdin= BenchRoot_dir+'437.leslie3d'+binary_dir+'leslie3d.in'
    process.input=stdin
    process.output='leslie3d.stdout'
    process.cmd = [process.executable] + ['<',stdin]
    return process

#444.namd
def namd():
    process = LiveProcess()
    process.executable = BenchRoot_dir+'444.namd'+binary_dir+'namd_base.alpha-fake'
    input= BenchRoot_dir+'444.namd'+binary_dir+'namd.input'
    process.cmd = [process.executable] + ['--input',input,'--iterations','1','--output','namd.out']
    process.output='namd.stdout'
    return process

#445.gobmk
def gobmk():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'445.gobmk'+binary_dir+'gobmk_base.alpha-fake'
    stdin= BenchRoot_dir+'445.gobmk'+binary_dir+'nngs.tst'
    process.cmd = [process.executable]+['--quiet','--mode','gtp', '<',stdin]
    process.input=stdin
    process.output='nngs.tst.out'
    return process

#450.soplex
def soplex():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'450.soplex'+binary_dir+'soplex_base.alpha-fake'
    data= BenchRoot_dir+'450.soplex'+binary_dir+'ref.mps'
    process.cmd = [process.executable]+['-m3500',data]
    process.output = 'ref.out'
    return process

#453.povray
def povray():
    process=LiveProcess()
    process.executable =  BenchRoot_dir+'453.povray'+binary_dir+'povray_base.alpha-fake'
    data=BenchRoot_dir+'453.povray'+binary_dir+'SPEC-benchmark-ref.ini'
    process.cmd = [process.executable]+[data]
    process.output = 'SPEC-benchmark-ref.stdout'
    return process

#454.calculix
def calculix():
    process=LiveProcess()
    process.executable =  BenchRoot_dir+'454.calculix'+binary_dir+'calculix_base.alpha-fake'
    data=BenchRoot_dir+'454.calculix'+binary_dir+'hyperviscoplastic'
    process.cmd = [process.executable]+['-i',data]
    process.output = 'beampic.log'
    return process

#456.hmmer
def hmmer():
    process=LiveProcess()
    process.executable =  BenchRoot_dir+'456.hmmer'+binary_dir+'hmmer_base.alpha-fake'
    data=BenchRoot_dir+'456.hmmer'+binary_dir+'retro.hmm'
    process.cmd = [process.executable]+['--fixed', '0', '--mean', '500', '--num', '500000', '--sd', '350', '--seed', '0', data]
    process.output = 'retro.out'
    return process

#458.sjeng
def sjeng():
    process=LiveProcess()
    process.executable =  BenchRoot_dir+'458.sjeng'+binary_dir+'sjeng_base.alpha-fake'
    data=BenchRoot_dir+'458.sjeng'+binary_dir+'ref.txt'
    process.cmd = [process.executable]+[data]
    process.output = 'ref.out'
    return process

#459.GemsFDTD
def GemsFDTD():
    process=LiveProcess()
    process.executable =  BenchRoot_dir+'459.GemsFDTD'+binary_dir+'GemsFDTD_base.alpha-fake'
    process.cmd = [process.executable]
    process.output = 'ref.log'
    return process

#462.libquantum
def libquantum():
    process=LiveProcess()
    process.executable =  BenchRoot_dir+'462.libquantum'+binary_dir+'libquantum_base.alpha-fake'
    process.cmd = [process.executable],'1397','8'
    process.output = 'test.out'
    return process

#464.h264ref
def h264ref():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'464.h264ref'+binary_dir+'h264ref_base.alpha-fake'
    data=BenchRoot_dir+'464.h264ref'+binary_dir+'foreman_ref_encoder_baseline.cfg'
    process.cmd = [process.executable]+['-d',data]
    process.output = 'foreman_ref_encoder_baseline.out'
    return process

#470.lbm
def lbm():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'470.lbm'+binary_dir+'lbm_base.alpha-fake'
    data=BenchRoot_dir+'470.lbm'+binary_dir+'100_100_130_cf_a.of'
    process.cmd = [process.executable]+['20', 'reference.dat', '0', '1' ,data]
    process.output = 'lbm.out'
    return process

#471.omnetpp
def omnetpp():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'471.omnetpp'+binary_dir+'omnetpp_base.alpha-fake'
    data=BenchRoot_dir+'471.omnetpp'+binary_dir+'omnetpp.ini'
    process.cmd = [process.executable]+[data]
    process.output = 'omnetpp.out'
    return process

#473.astar
def astar():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'473.astar'+binary_dir+'astar_base.alpha-fake'
    process.cmd = [process.executable]+['rivers.cfg']
    process.output = 'rivers.out'
    return process

#481.wrf
def wrf():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'481.wrf'+binary_dir+'wrf_base.alpha-fake'
    process.cmd = [process.executable]
    process.output = 'ref.out'
    return process

#482.sphinx3
def sphinx3():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'482.sphinx3'+binary_dir+'sphinx_livepretend_base.alpha-fake'
    process.cmd = [process.executable]+['ctlfile', '.', 'args.an4']
    process.output = 'an4.out'
    return process

#998.specrand
def specrand_i():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'998.specrand'+binary_dir+'specrand_base.alpha-fake'
    process.cmd = [process.executable] + ['324342','24239']
    process.output = 'rand.24239.out'
    return process

#999.specrand
def specrand_f():
    process=LiveProcess()
    process.executable = BenchRoot_dir+'999.specrand'+binary_dir+'specrand_base.alpha-fake'
    process.cmd = [process.executable] + ['324342','24239']
    process.output = 'rand.24239.out'
    return process
