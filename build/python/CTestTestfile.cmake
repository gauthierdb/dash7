# CMake generated Testfile for 
# Source directory: /home/gauthier/ComSys_customBlocks/gr-comsys/python
# Build directory: /home/gauthier/ComSys_customBlocks/gr-comsys/build/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(qa_diff_encoder "/bin/sh" "/home/gauthier/ComSys_customBlocks/gr-comsys/build/python/qa_diff_encoder_test.sh")
set_tests_properties(qa_diff_encoder PROPERTIES  _BACKTRACE_TRIPLES "/home/gauthier/ComSys_customBlocks/gr-comsys/cmake/Modules/GrTest.cmake;114;add_test;/home/gauthier/ComSys_customBlocks/gr-comsys/python/CMakeLists.txt;45;GR_ADD_TEST;/home/gauthier/ComSys_customBlocks/gr-comsys/python/CMakeLists.txt;0;")
add_test(qa_diff_decoder "/bin/sh" "/home/gauthier/ComSys_customBlocks/gr-comsys/build/python/qa_diff_decoder_test.sh")
set_tests_properties(qa_diff_decoder PROPERTIES  _BACKTRACE_TRIPLES "/home/gauthier/ComSys_customBlocks/gr-comsys/cmake/Modules/GrTest.cmake;114;add_test;/home/gauthier/ComSys_customBlocks/gr-comsys/python/CMakeLists.txt;46;GR_ADD_TEST;/home/gauthier/ComSys_customBlocks/gr-comsys/python/CMakeLists.txt;0;")
add_test(qa_pn9_whitening "/bin/sh" "/home/gauthier/ComSys_customBlocks/gr-comsys/build/python/qa_pn9_whitening_test.sh")
set_tests_properties(qa_pn9_whitening PROPERTIES  _BACKTRACE_TRIPLES "/home/gauthier/ComSys_customBlocks/gr-comsys/cmake/Modules/GrTest.cmake;114;add_test;/home/gauthier/ComSys_customBlocks/gr-comsys/python/CMakeLists.txt;47;GR_ADD_TEST;/home/gauthier/ComSys_customBlocks/gr-comsys/python/CMakeLists.txt;0;")
add_test(qa_crc_tagged_stream "/bin/sh" "/home/gauthier/ComSys_customBlocks/gr-comsys/build/python/qa_crc_tagged_stream_test.sh")
set_tests_properties(qa_crc_tagged_stream PROPERTIES  _BACKTRACE_TRIPLES "/home/gauthier/ComSys_customBlocks/gr-comsys/cmake/Modules/GrTest.cmake;114;add_test;/home/gauthier/ComSys_customBlocks/gr-comsys/python/CMakeLists.txt;48;GR_ADD_TEST;/home/gauthier/ComSys_customBlocks/gr-comsys/python/CMakeLists.txt;0;")
