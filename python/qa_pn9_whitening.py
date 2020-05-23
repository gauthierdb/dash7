#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2020 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
from gnuradio import gr, gr_unittest
from gnuradio import blocks

from pn9_whitening import pn9_whitening

import comsys_swig as comsys


class qa_pn9_whitening (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()
        self.tsb_key = "packet_len"


    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        input1 = (10, 0, 1, 2)
        #input1= [0, 0, 0, 0, 1, 0, 1, 0]
        #input2 = [ 0, 0, 0, 0, 0, 0, 0, 0]
        #input3 = [ 0, 0, 0, 0, 0, 0, 0, 1]
        #input4 = [0, 0, 0, 0, 0, 0, 1, 0]

        output1 = (245,225, 28, 152)
        #output1 = [1, 1, 1, 1, 0, 1, 0, 1]
        #output2 = [1, 1, 1, 0, 0, 0, 0, 1]
        #output3 = [0, 0, 0, 1, 1, 1, 0, 0]
        #output4 = [1, 0, 0, 1, 1, 0, 0, 0]

        src = blocks.vector_source_b(input1)
        src_tagged = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, len(input1), self.tsb_key)
        pn9 = pn9_whitening(False)
        dst = blocks.tsb_vector_sink_b(tsb_key = self.tsb_key)

        self.tb.connect(src, src_tagged, pn9, dst)
        self.tb.run()

        self.assertEquals(dst.data()[0], output1)

    def test_with_reset (self):
        input1 = (10, 0, 1, 2)
        #input1= [0, 0, 0, 0, 1, 0, 1, 0]
        #input2 = [ 0, 0, 0, 0, 0, 0, 0, 0]
        #input3 = [ 0, 0, 0, 0, 0, 0, 0, 1]
        #input4 = [0, 0, 0, 0, 0, 0, 1, 0]

        output1 = (245,225, 28, 152)
        #output1 = [1, 1, 1, 1, 0, 1, 0, 1]
        #output2 = [1, 1, 1, 0, 0, 0, 0, 1]
        #output3 = [0, 0, 0, 1, 1, 1, 0, 0]
        #output4 = [1, 0, 0, 1, 1, 0, 0, 0]

        src = blocks.vector_source_b(input1)
        src.set_max_noutput_items(2)
        src.set_min_output_buffer(2)
        src.set_max_output_buffer(2)

        src_tagged = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, len(input1), self.tsb_key)
        src_tagged.set_max_noutput_items(2)
        src_tagged.set_min_output_buffer(2)
        src_tagged.set_max_output_buffer(2)


        pn9 = pn9_whitening(True)


        dst = blocks.tsb_vector_sink_b(tsb_key = self.tsb_key)


        self.tb.connect(src, src_tagged, pn9, dst)
        self.tb.run()

        self.assertEquals(dst.data()[0], output1)



if __name__ == '__main__':
    gr_unittest.run(qa_pn9_whitening, "qa_pn9_whitening.xml")
