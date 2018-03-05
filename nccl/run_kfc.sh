#!/bin/sh
#SBATCH --nodes=32
#SBATCH --ntasks-per-node=8
#SBATCH --job-name=chnrml_chk
#SBATCH -t 0-0:20 # time (D-HH:MM) 


mpirun \
  -output-proctable \
  -mca pml ob1 \
  -np 256 \
  -npernode 8 \
  -x PATH \
  -x LIBRARY_PATH \
  -x LD_LIBRARY_PATH \
  python3 ./check.py