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
import pmt

#import io
#from gnuradio import io_signature

class pn9_whitening(gr.sync_block):
    """
    docstring for block pn9_whitening
    """

    def __init__(self, verbose=False):
        gr.sync_block.__init__(self,
            name="pn9_whitening",
            in_sig=[numpy.uint8],
            out_sig=[numpy.uint8])
        self.currentFrameLength = 0  # How many frames do you know that are coming
        self.currentFrameIndex = 0   # What is the index of this frame?
        self.endOfFrame = False
        self.currentPacketLength = None # What is the byte length of the currrent frame
        self.currentPacketIndex = 0 # What is the current byte we're processing
        self.tags = ()  # This stores all tags that we know of. This is an index of the amount of frames
        self.PN9_MSB = 0x01
        self.PN9_LSB = 0xFF
        self.verbose = verbose
        self.hasStarted = False



    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # This is not always called on the start of a new frame, so first we need to check if we already started or not.
        if(self.hasStarted == False):
            self.PN9_MSB = 0x01
            self.PN9_LSB = 0xFF
            self.tags = self.get_tags_in_window(0, 0, len(input_items[0]))
            self.currentFrameLength = len(self.tags)
            self.currentFrameIndex = 0
            self.currentPacketIndex = 0

            if(self.currentFrameLength != 0):
                self.currentPacketLength = pmt.to_python(self.tags[self.currentFrameIndex].value)

            self.hasStarted = True

            if(self.verbose):
                print("----- PN9 first work function called -------")
                print("Currently, we know of " + str(self.currentFrameLength) + " Frames that are coming. These have the values: ")
                counter = 1
                for tag in self.tags:
                    value = pmt.to_python(tag.value)
                    print("Tag nr: " + str(counter))
                    print("val: " + str(value))
                    print("Offset: " + str(tag.offset))
                    counter = counter + 1

        # If we stopped the previous work function right at the end of a frame
        elif(self.endOfFrame):
            self.PN9_MSB = 0x01
            self.PN9_LSB = 0xFF

            self.tags = self.tags + self.get_tags_in_window(0, 0, len(input_items[0]))
            if(self.verbose):
                print("A new work function is called, we found " + str(len(self.tags) - self.currentFrameLength) + "New tags")

            # If we have no more frames from previous work (Which should always be the case)
            if(self.currentFrameIndex == self.currentFrameLength - 1):
                self.currentFrameIndex = self.currentFrameIndex + 1
                self.currentPacketIndex = 0
                self.currentPacketLength = pmt.to_python(self.tags[self.currentFrameIndex].value)

                if(self.verbose):
                    print("Starting the " + str(self.currentFrameIndex) + "th frame. This frame has length: " + str(pmt.to_python(self.tags[self.currentFrameIndex].value)))

            self.currentFrameLength = len(self.tags)
            self.endOfFrame = False

        else:
            #print(" !!! Work function was called without the previous frame being done !!!")
            #TODO: we might have to check if there are new tags that came with this function call
            self.tags = self.tags + self.get_tags_in_window(0,0,len(input_items[0]))
            self.currentFrameLength = len(self.tags)











        for i in range(0, len(output_items[0])):

            #You reached the end of a frame, but you still know what the next frame is
            if(self.endOfFrame):
                if(self.currentFrameIndex < self.currentFrameLength-1):
                    if(self.verbose):
                        print("Reached the end of frame " + str(self.currentFrameIndex) + " But there is a new frame of length " + str(pmt.to_python(self.tags[self.currentFrameIndex+1].value)))
                        print("There are still [" + str(self.currentFrameLength - self.currentFrameIndex+1) +"] frames to go that we know of.")
                    self.currentFrameIndex = self.currentFrameIndex + 1
                    self.currentPacketIndex = 0
                    self.currentPacketLength = pmt.to_python(self.tags[self.currentFrameIndex].value)
                    self.PN9_MSB = 0x01
                    self.PN9_LSB = 0xFF
                else:
                    print("Why is this called? this is value")
                    print(in0[i])
                    print("Tags that we saved at the start")
                    print("----------")
                    counter = 1
                    for tag in self.tags:
                        value = pmt.to_python(tag.value)
                        print("Tag nr: " + str(counter))
                        print("val: " + str(value))
                        print("Offset: " + str(tag.offset))
                        counter = counter + 1
                    print("----------")
                    print("and these are the tags if we check again rn")
                    print("----------")
                    tg = self.get_tags_in_window(0, 0, len(input_items[0]))
                    counter = 1
                    for tag in tg:
                        value = pmt.to_python(tag.value)
                        print("Tag nr: " + str(counter))
                        print("val: " + str(value))
                        print("Offset: " + str(tag.offset))
                        counter = counter + 1
                    print("----------")


            else:
                if(self.verbose):
                    print("We are currently on frame " + str(self.currentFrameIndex) + " with length " + str(self.currentPacketLength) + ". Current byte is " + str(self.currentPacketIndex))

            self.endOfFrame = False



            out[i] = in0[i] ^ self.PN9_LSB

            for j in range(0, 8):
                MSBPrevious = self.PN9_MSB
                # Your MSB (9th bit) becomes 1 if (0th bit XOR 5th bit)
                self.PN9_MSB = (self.PN9_LSB & 0x01) ^ ((self.PN9_LSB >> 5) & 0x01)
                # Your LSB is shifted 1 place and the 8th bit is set to the previous 9th bit
                self.PN9_LSB = ((self.PN9_LSB >> 1) & 0xFF) | ((MSBPrevious << 7) & 0x80)

            # If you reached the last byte of that packet, you need to check if there is another packed queued in work function
            # This is only the case if you already receveived its tag.
            if(self.currentPacketIndex == self.currentPacketLength - 1):
                if(self.verbose):
                    print("We reached the end of this frame because our index is " + str(self.currentPacketIndex) + " which is input byte " + str(hex(in0[i])) +" (HEX)")
                self.endOfFrame = True


            self.currentPacketIndex = self.currentPacketIndex + 1

        return len(output_items[0])

