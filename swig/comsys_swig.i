/* -*- c++ -*- */

#define COMSYS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "comsys_swig_doc.i"

%{
#include "comsys/diff_encoder.h"
#include "comsys/diff_decoder.h"
#include "comsys/crc_tagged_stream.h"
%}


%include "comsys/diff_encoder.h"
GR_SWIG_BLOCK_MAGIC2(comsys, diff_encoder);
%include "comsys/diff_decoder.h"
GR_SWIG_BLOCK_MAGIC2(comsys, diff_decoder);

%include "comsys/crc_tagged_stream.h"
GR_SWIG_BLOCK_MAGIC2(comsys, crc_tagged_stream);
