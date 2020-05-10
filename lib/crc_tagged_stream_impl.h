/* -*- c++ -*- */
/* 
 * Copyright 2020 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_COMSYS_CRC_TAGGED_STREAM_IMPL_H
#define INCLUDED_COMSYS_CRC_TAGGED_STREAM_IMPL_H

#include <boost/crc.hpp>
#include <comsys/crc_tagged_stream.h>

namespace gr {
  namespace comsys {

    class crc_tagged_stream_impl : public crc_tagged_stream
    {
     private:
        bool d_check;
        boost::crc_optimal<16, 0x1021, 0xFFFF, 0x0000, false, false> d_crc_impl;
        unsigned int d_crc_length;
        std::vector<char> d_buffer;
        unsigned short calculate_crc16(const unsigned char* in, size_t packet_length);
      // Nothing to declare in this block.

     protected:
      int calculate_output_stream_length(const gr_vector_int &ninput_items);

     public:
      crc_tagged_stream_impl(bool check, const std::string& tag);
      ~crc_tagged_stream_impl();

      // Where all the action really happens

      int work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace comsys
} // namespace gr

#endif /* INCLUDED_COMSYS_CRC_TAGGED_STREAM_IMPL_H */

