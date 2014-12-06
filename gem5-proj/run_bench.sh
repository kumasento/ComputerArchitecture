#!/bin/bash

echo "-- benchmark name:", $1
echo "-- algorithm name:", $2

build/ALPHA/gem5.opt \
    --debug-flag=Branch \
    --outdir=../data/$1/$2 \
    configs/My/se.py \
    --bench=$1\
    --cpu-type=InOrderCPU \
    --cmd=./tests/test-progs/hello/bin/alpha/linux/hello \
    --caches \
    -I 1000000 \
    > ../data/tmp.out.txt
