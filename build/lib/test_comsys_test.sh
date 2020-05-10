#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/gauthier/ComSys_customBlocks/gr-comsys/lib
export PATH=/home/gauthier/ComSys_customBlocks/gr-comsys/build/lib:$PATH
export LD_LIBRARY_PATH=/home/gauthier/ComSys_customBlocks/gr-comsys/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-comsys 
