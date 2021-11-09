ALL: testfile.bin

generate_testfiles: generate_testfiles.f90
	gfortran $^ -o $@

testfile.bin: generate_testfiles
	./$^

testfile_attrs.bin: generate_testfiles
	./$^
