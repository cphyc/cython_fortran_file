ALL: testfile.bin

generate_testfile: generate_testfile.f90
	gfortran $^ -o $@

testfile.bin: generate_testfile
	./$^