#!/usr/bin/bash
#PJM -L "rscgrp=small"
#PJM -L elapse=24:00:00
#PJM -L "node=300"
#PJM --mpi "proc=300"
#PJM -j
#PJM -g ra000012
#PJM -S
#PJM -o logs/%n.%j.stdout
#PJM -e logs/%n.%j.stderr
#PJM --spath logs/%n.%j.stat
#PJM -x PJM_LLIO_GFSCACHE=/vol0004
#PJM --llio localtmp-size=40Gi
#PJM -m b,e
#PJM --mail-list alexander.drozd@gmail.com
mpirun  main