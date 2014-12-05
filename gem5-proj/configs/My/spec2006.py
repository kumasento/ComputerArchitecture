# Mybench.py
# Modified by Chao Zhang
# Used for SPEC cpu 2006 benchmark test.

import m5
from m5.objects import *

BenchRoot_dir='../spec/'
test_dir = '/run/run_base_test_alpha-fake.0000/'
ref_dir = '/run/run_base_ref_alpha-fake.0000/'

#400.perlbench
def perlbench():
    process = LiveProcess()
    process.cwd = BenchRoot_dir+'400.perlbench'+ref_dir
    process.cmd = [process.cwd+'perlbench_base.alpha-fake'] + ['-I./lib', 'checkspam.pl', '2500', '5', '25', '11', '150', '1', '1', '1', '1']
    return process

#401.bzip2
def bzip2():
    process = LiveProcess()
    process.cwd = BenchRoot_dir+'401.bzip2'+test_dir
    process.cmd = [process.cwd+'bzip2_base.alpha-fake'] + ['dryer.jpg', '2']
    return process 

#403.gcc
def gcc():
    process = LiveProcess()
    process.cwd = BenchRoot_dir+'403.gcc'+ref_dir
    process.cmd = [process.cwd+'gcc_base.alpha-fake'] + ['166.i', '-o', '166.s']
    return process

#410.bwaves
def bwaves():
    process = LiveProcess()
    process.cwd = BenchRoot_dir+'410.bwaves'+test_dir
    process.cmd = [process.cwd+'bwaves_base.alpha-fake'] + []
    return process

#416.gamess
def gamess():
    process = LiveProcess()
    process.cwd = BenchRoot_dir+'416.gamess'+ref_dir
    process.cmd = [process.cwd+'gamess_base.alpha-fake'] + ['-i', 'cytosine.2.config']
    return process;

#429.mcf
def mcf():
    process = LiveProcess()
    process.cwd = BenchRoot_dir+'429.mcf'+test_dir
    process.cmd = [process.cwd+'mcf_base.alpha-fake'] + ['inp.in']
    return process

#433.milc
def milc():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'433.milc'+ref_dir
    process.cmd = [process.cwd+'milc_base.alpha-fake'] + ['-i', 'su3imp.in']
    return process

#434.zeusmp // need more physical memory
def zeusmp():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'434.zeusmp'+test_dir
    process.cmd = [process.cwd+'zeusmp_base.alpha-fake'] + []
    return process

#435.gromacs
def gromacs():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'435.gromacs'+ref_dir
    process.cmd = [process.cwd+'gromacs_base.alpha-fake'] + ['-silent', '-deffnm', 'gromacs', '-nice', '0']
    return process

#436.cactusADM
def cactusADM():
    process = LiveProcess()
    process.cwd = BenchRoot_dir+'436.cactusADM'+ref_dir
    process.cmd = [process.cwd+'cactusADM_base.alpha-fake'] + ['benchADM.par']
    return process

#437.leslie3d
def leslie3d():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'437.leslie3d'+ref_dir
    process.cmd = [process.cwd+'leslie3d_base.alpha-fake'] + ['-i', 'leslie3d.in']
    return process

#444.namd
def namd():
    process = LiveProcess()
    process.cwd = BenchRoot_dir+'444.namd'+ref_dir
    process.cmd = [process.cwd+'namd_base.alpha-fake'] + ['--input', 'namd.input', '--iterations', '38', '--output', 'namd.out']
    return process

#445.gobmk
def gobmk():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'445.gobmk'+ref_dir
    process.cmd = [process.cwd+'gobmk_base.alpha-fake'] + ['-i', '13x13.tst', '--quiet', '--mode gtp']
    return process

#450.soplex
def soplex():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'450.soplex'+ref_dir
    process.cmd = [process.cwd+'soplex_base.alpha-fake'] + ['-s1', '-e', '-m45000', 'pds-50.mps']
    return process

#453.povray
def povray():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'453.povray'+test_dir
    process.cmd = [process.cwd+'povray_base.alpha-fake'] + ['SPEC-benchmark-test.ini']
    return process

#454.calculix
def calculix():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'454.calculix'+ref_dir
    process.cmd = [process.cwd+'calculix_base.alpha-fake'] + ['-i', 'hyperviscoplastic']
    return process

#456.hmmer
def hmmer():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'456.hmmer'+ref_dir
    process.cmd = [process.cwd+'hmmer_base.alpha-fake'] + ['--fixed', '0', '--mean', '500', '--num', '500000', '--sd', '350', '--seed', '0', 'retro.hmm']
    return process

#458.sjeng
def sjeng():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'458.sjeng'+test_dir
    process.cmd = [process.cwd+'sjeng_base.alpha-fake'] + ['test.txt']
    return process

#459.GemsFDTD
def GemsFDTD():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'459.GemsFDTD'+test_dir
    process.cmd = [process.cwd+'GemsFDTD_base.alpha-fake'] + ['']
    return process

#462.libquantum
def libquantum():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'462.libquantum'+ref_dir
    process.cmd = [process.cwd+'libquantum_base.alpha-fake'] + ['1397', '8']
    return process

#464.h264ref
def h264ref():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'464.h264ref'+ref_dir
    process.cmd = [process.cwd+'h264ref_base.alpha-fake'] + ['-d', 'foreman_ref_encoder_baseline.cfg']
    return process

#465.tonto
def tonto():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'465.tonto'+test_dir
    process.cmd = [process.cwd+'tonto_base.alpha-fake'] 
    return process

#470.lbm
def lbm():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'470.lbm'+ref_dir
    process.cmd = [process.cwd+'lbm_base.alpha-fake'] + ['3000', 'reference.dat', '0', '0', '100_100_130_ldc.of']
    return process

#471.omnetpp
def omnetpp():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'471.omnetpp'+test_dir
    process.cmd = [process.cwd+'omnetpp_base.alpha-fake'] + ['omnetpp.ini']
    return process

#473.astar
def astar():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'473.astar'+test_dir
    process.cmd = [process.cwd+'astar_base.alpha-fake'] + ['lake.cfg']
    return process

#481.wrf
def wrf():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'481.wrf'+ref_dir
    process.cmd = [process.cwd+'wrf_base.alpha-fake'] + ['']
    return process

#482.sphinx3
def sphinx3():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'482.sphinx3'+ref_dir
    process.cmd = [process.cwd+'sphinx_livepretend_base.alpha-fake'] + ['ctlfile . args.an4']
    return process

#998.specrand
def specrand_i():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'998.specrand'+test_dir
    process.cmd = [process.cwd+'specrand_base.alpha-fake'] + ['324342 24239']
    return process

#999.specrand
def specrand_f():
    process=LiveProcess()
    process.cwd = BenchRoot_dir+'999.specrand'+test_dir
    process.cmd = [process.cwd+'specrand_base.alpha-fake'] + ['324342 24239']
    return process
