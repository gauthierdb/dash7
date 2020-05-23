"""
Custom Frame synchronizer:

This block will take in a stream of floats, it will search for the syncword until its found.
In the next step the block will read in the length that is in the header after the sync word.
After that the payload equal to the length in the header will be outputted.

Jaimie Vranckx & Mohammad Ali Amir & Maximiliaan Walravens
"""

import numpy as np
from gnuradio import gr
import pmt

class blk(gr.basic_block):  # use of basic block so that output and input dont have to be equal
    def __init__(self, sync_word=59088, whitening=True):  # only default arguments here
        gr.basic_block.__init__(
            self,
            name='Frame synchroniser',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.sync_word = np.uint16(sync_word) # sync word of 16 bits
        self.data_buffer = np.uint16(0) #buffer for data read inside the sync state
        self.header_buffer = np.uint8(0) #buffer for data read inside the header state
        self.header_counter = 0 #count for current position in header
        self.packet_counter = 0 #count for current position in packet
        self.state = 0 # current state
	self.whitening=whitening
	self.clear_header=np.uint8(0)

    def general_work(self, input_items, output_items):

	#print(len(input_items))

	# read in the buffers
        input0 = input_items[0]
        output0 = output_items[0]

	#initialize variables
        count = 0
	produced = 0

	#loop over inputs
 	while count<len(output0):
            if self.state == 0: #State 1: search for syncword
                while count < len(output0):
                    self.data_buffer = np.uint16(((self.data_buffer << 1) | gr.branchless_binary_slicer(np.float64(input0[count])) & 0x1)) 
			#shift bit into data buffer
                    count+=1

                    if (self.data_buffer) ^ self.sync_word == 0 : # if syncword found

 			#reset variables
			self.header_buffer = np.uint8(0)
			self.header_counter = 0

			# next state
                        self.state = 1
                        break

            elif self.state == 1: #State 2: get header
                while count < len(output0):
                    self.header_buffer = np.uint8(((self.header_buffer << 1) | gr.branchless_binary_slicer(np.float64(input0[count])) & 0x1))
		    output0[produced] = input0[count]
                    produced += 1
		    #print("{0:b}".format(np.uint8(self.header_buffer)))
                    count+=1
                    self.header_counter += 1

                    if self.header_counter == 8: # if full header found
			if(self.whitening):
				self.clear_header=self.header_buffer ^ np.uint8(255)
			else:
				self.clear_header=self.header_buffer	
		    	#print("FOUND IT")
			#print("{0:b}".format(self.header_buffer))
			#reset variables
			self.packet_counter=0

			# next state
                        self.state = 2
                        break

            elif self.state == 2: #State 2: read in payload
                if self.packet_counter == 0 :# if start of payload add tag for next blocks to know length
                    print("----------------- Debugging in Frame Sync ---------------")
	            print("I'm at the start of the payload, which is at pos: ")
                    print(self.nitems_written(0) + produced-8)
                    print("And i believe the length of the following payload is: ")
                    print(pmt.from_long(long(self.clear_header)+1))
                    print("---------------------------------------------------------")
                    
                    self.add_item_tag(0,  # Port number
                                      self.nitems_written(0) + produced-8,  # Offset
                                      pmt.intern("packet_len"),  # Key
                                      pmt.from_long(long(self.clear_header)+1)  # Value
		    			)
                    #print("Added a tag")
		    #print(long(self.clear_header))
                while count < len(output0):
                    if self.packet_counter < (self.clear_header)*8:	# read in buffer until length is reached
                        output0[produced] = input0[count]
			#if(count==len(output0)
                        produced += 1
                        count += 1
                        self.packet_counter += 1
                    else: # if payload is read in entirely
			#reset variables
			self.data_buffer = 0
			#print("Passed frame sync")
			# next state
                        self.state = 0
                        break
        if(produced > 0):
            print("Produced: " + str(produced))
    	self.consume_each(count) # set number of consumed inputs in buffer
    	return produced	# set nu;ber of produced outputs in output buffer

