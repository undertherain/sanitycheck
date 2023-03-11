ALL: test

test_mpi: test_mpi.c
	mpicc -o $@ $^

test: test_mpi
	@echo "------- testing MPI native"
	@echo
	mpirun -n 2 test_mpi
	@echo
	@echo "------- testing MPI Python bindings"
	@echo
	mpirun -n 2 python3 test_mpi.py