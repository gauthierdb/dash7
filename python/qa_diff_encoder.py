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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from gnuradio import digital
import comsys_swig as comsys

class qa_diff_encoder (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    # This test will compare the dataIn and dataOut for:
    # dataIn -> encoder -> decoder -> dataOut
    def test_001_t (self):
        modulus = 2
        initial_state = 1
        src_data = (1, 0, 1, 1, 0, 0, 0, 1)
        src = blocks.vector_source_b(src_data)
        enc = comsys.diff_encoder(modulus, initial_state)
        dec = comsys.diff_decoder(modulus, initial_state)
        dst = blocks.vector_sink_b()
        self.tb.connect(src, enc)
        self.tb.connect(enc, dec)
        self.tb.connect(dec, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertEquals(result_data, src_data)


if __name__ == '__main__':
    gr_unittest.run(qa_diff_encoder, "qa_diff_encoder.xml")
