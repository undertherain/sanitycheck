#!/bin/sh
#SBATCH --nodes=32
#SBATCH --ntasks-per-node=8
#SBATCH --job-name=imagenet
#SBATCH -t 0-0:20 # time (D-HH:MM) 

#  -mca pml ob1 \

mpirun \
  -output-proctable \
  -np 256 \
  -npernode 8 \
  -x PATH \
  -x LIBRARY_PATH \
  -x LD_LIBRARY_PATH \
  python3 ./check.py