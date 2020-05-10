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

        res_data = output1

        src = blocks.vector_source_b(input1)
        pn9 = pn9_whitening()
        dst = blocks.vector_sink_b()

        self.tb.connect(src, pn9, dst)
        self.tb.run(1)

        result_data = dst.data()
        self.assertEquals(result_data, res_data)


if __name__ == '__main__':
    gr_unittest.run(qa_pn9_whitening, "qa_pn9_whitening.xml")
