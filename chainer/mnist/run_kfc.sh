#!/bin/sh
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --job-name=mnist
#SBATCH -t 0-0:20 # time (D-HH:MM) 


#source ./modules.sh

source /home/users/alex/apps.sh

mpirun \
  -output-proctable \
  -mca pml ob1 \
  -np 4 \
  -npernode 2 \
  -x PATH \
  -x LD_LIBRARY_PATH \
  -x LIBRARY_PATH \
   python3 mn_train_mnist.py --gpu --communicator hierarchical