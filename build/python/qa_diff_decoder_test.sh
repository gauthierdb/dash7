#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/gauthier/ComSys_customBlocks/gr-comsys/python
export PATH=/home/gauthier/ComSys_customBlocks/gr-comsys/build/python:$PATH
export LD_LIBRARY_PATH=/home/gauthier/ComSys_customBlocks/gr-comsys/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/gauthier/ComSys_customBlocks/gr-comsys/build/swig:$PYTHONPATH
/usr/bin/python2 /home/gauthier/ComSys_customBlocks/gr-comsys/python/qa_diff_decoder.py 
