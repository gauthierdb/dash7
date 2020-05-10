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
import pmt
from comsys import crc_tagged_stream
import comsys_swig as comsys


class qa_crc_tagged_stream (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()
        self.tsb_key = "packet_len"

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # ADDING CRC
        input1 = (49, 50, 51, 52, 53, 54, 55, 56, 57) # Unicode 1-9
        input1_tagger = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, len(input1), self.tsb_key)
        src = blocks.vector_source_b(input1)
        crc = crc_tagged_stream(False, self.tsb_key)
        dst = blocks.tsb_vector_sink_b(tsb_key = self.tsb_key)
        output1 = (49, 50, 51, 52, 53, 54, 55, 56, 57, 177, 41) #unicode 0x29B1

        self.tb.connect(src, input1_tagger, crc, dst)
        self.tb.run ()
        self.assertEquals(dst.data()[0], output1)


    def test_002_t(self):
        # FORTH & BACK
        input1 = (49, 50, 51, 52, 53, 54, 55, 56, 57)  # Unicode 1-9
        input1_tagger = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, len(input1), self.tsb_key)
        src = blocks.vector_source_b(input1)
        crc = crc_tagged_stream(False, self.tsb_key)
        crc_check = crc_tagged_stream(True, self.tsb_key)
        dst = blocks.tsb_vector_sink_b(tsb_key=self.tsb_key)

        self.tb.connect(src, input1_tagger, crc, crc_check, dst)
        self.tb.run()
        self.assertEquals(dst.data()[0], input1)


'''
    def test_003_t(self):
        packets = list(range(9))
        tag1 = gr.tag_t()
        tag1.offset = 0
        pack_len = 9
        tag1.key = pmt.string_to_symbol("packet_len")
        tag1.value = pmt.from_long(pack_len)

        #data, repeat, vlen, tags
        src = blocks.vector_source_b(packets)
        crc = crc_tagged_stream(False, self.tsb_key)
'''

if __name__ == '__main__':
    gr_unittest.run(qa_crc_tagged_stream, "qa_crc_tagged_stream.xml")
