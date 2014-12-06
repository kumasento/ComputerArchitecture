#!/bin/bash

benchs=("462.libquantum" \
        "400.perlbench" \
        "403.gcc" \
        "471.omnetpp" \
        "429.mcf" \
        "473.astar" \
        "401.bzip2")

algorithm=$1

for bench in ${benchs[@]}; do
    echo "[$algorithm]: running benchmark $bench..." 
    build/ALPHA/gem5.opt \
        --debug-flag=Branch \
        --outdir=../data/$bench/$1 \
        configs/My/se.py \
        --bench=$bench\
        --cpu-type=InOrderCPU \
        --cmd=./tests/test-progs/hello/bin/alpha/linux/hello \
        --caches \
        -I 1000000 \
        > ../data/tmp.out.txt
done
