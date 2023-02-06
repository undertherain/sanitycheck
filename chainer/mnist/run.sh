#!/bin/sh
#$ -cwd
#$ -l f_node=2
#$ -l h_rt=00:10:00
#$ -N mnist
#$ -m abe
#$ -M alex@smg.is.titech.ac.jp

#source ./modules.sh

source /home/1/drozd-a-aa/apps.sh

mpirun \
  -output-proctable \
  -mca pml ob1 \
  -np 8 \
  -npernode 4 \
  -x PATH \
  -x LD_LIBRARY_PATH \
  -x LIBRARY_PATH \
   python3 mn_train_mnist.py --gpu