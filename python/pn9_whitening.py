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
from gnuradio import gr


class pn9_whitening(gr.sync_block):
    """
    docstring for block pn9_whitening
    """

    def __init__(self):
        gr.sync_block.__init__(self,
            name="pn9_whitening",
            in_sig=[numpy.uint8],
            out_sig=[numpy.uint8])
        self.PN9_MSB = 0x01
        self.PN9_LSB = 0xFF



    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        for i in range(0, len(output_items[0])):
            #print("current input:")
            #print(in0[i])
            #print("current LSB:")
            #print(self.PN9_LSB)
            #print("current output:")
            #print(in0[i] ^ self.PN9_LSB)
            #print("--------------")
            out[i] = in0[i] ^ self.PN9_LSB

            for j in range(0, 8):
                MSBPrevious = self.PN9_MSB
                # Your MSB (9th bit) becomes 1 if (0th bit XOR 5th bit)
                self.PN9_MSB = (self.PN9_LSB & 0x01) ^ ((self.PN9_LSB >> 5) & 0x01)
                # Your LSB is shifted 1 place and the 8th bit is set to the previous 9th bit
                self.PN9_LSB = ((self.PN9_LSB >> 1) & 0xFF) | ((MSBPrevious << 7) & 0x80)

        return len(output_items[0])

