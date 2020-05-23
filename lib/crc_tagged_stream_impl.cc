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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "crc_tagged_stream_impl.h"
#include <bitset>
#include <iostream>
using namespace std;
namespace gr {
  namespace comsys {

    crc_tagged_stream::sptr
    crc_tagged_stream::make(bool check, const std::string& tag)
    {
      return gnuradio::get_initial_sptr
        (new crc_tagged_stream_impl(check, tag));
    }

    /*
     * The private constructor
     */
    crc_tagged_stream_impl::crc_tagged_stream_impl(bool check, const std::string& tag)
      : gr::tagged_stream_block("crc_tagged_stream",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)), tag),
      d_check(check)
    {
      d_crc_length = 2;
      d_buffer = std::vector<char>(4096);
    }

    /*
     * Our virtual destructor.
     */
    crc_tagged_stream_impl::~crc_tagged_stream_impl()
    {
    }

    int
    crc_tagged_stream_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
    {
      // If d_check, we remove the CRC, if not, we add the crc
      if(d_check){
        return ninput_items[0] - d_crc_length;
      } else {
        return ninput_items[0] + d_crc_length;
      }
    }

    unsigned short crc_tagged_stream_impl::calculate_crc16(const unsigned char* in, size_t packet_length){
        unsigned short crc = 0;
        d_crc_impl.reset();
        d_crc_impl.process_bytes(in, packet_length);
        crc = d_crc_impl();
        return crc;
    }

    int
    crc_tagged_stream_impl::work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char* in = (const unsigned char*) input_items[0];
      unsigned char* out = (unsigned char*) output_items[0];
      size_t packet_length = ninput_items[0];
      int packet_size_diff = d_check ? -d_crc_length : d_crc_length; //  +/- 2
      unsigned short crc;
      //cout<<"packet length"<<std::endl;
      //cout<<packet_length<<std::endl;
      //cout<<"-----------"<<std::endl;
      if(d_check){
        // Too small packet -> auto drop
        if(packet_length <= d_crc_length){
            return 0;
        }else{

           d_crc_impl.process_bytes(in, packet_length - d_crc_length);
           crc = calculate_crc16(in, packet_length - d_crc_length);
           /*
           cout<<"----------- Checking CRC values -------------"<<std::endl;
           cout<<"input char array"<<std::endl;
           cout<<in<<std::endl;
           cout<<"crc of the input: "<<std::endl;
           cout<<(in + packet_length - d_crc_length)<<std::endl;
           cout<<"pointer to this crc:"<<std::endl;
           cout<<(*(in + packet_length - d_crc_length))<<std::endl;
           cout<<"converted to short & displayed as one digit, this becomes"<<std::endl;
           cout<<(*(unsigned short*)(in + packet_length - d_crc_length))<<std::endl;
           cout<<"in binary, this is"<<std::endl;
           cout<<bitset<16>(*(unsigned short*)(in + packet_length - d_crc_length))<<std::endl;
           cout<<"which should be identical with the current crc. Here they are printed side by side"<<std::endl;
           cout<<bitset<16>(crc)<<std::endl;
           cout<<bitset<16>(*(unsigned short*)(in + packet_length - d_crc_length))<<std::endl;
            */
           if(crc != *(unsigned short*)(in + packet_length - d_crc_length)){
                //cout<<"They are not identical. Packet dropped!"<<std::endl;
                return 0;
            }

        }
        memcpy( (void*)out, (const void*)in, packet_length - d_crc_length);
        //cout<<"They are identical! transmitting the following packet"<<std::endl;
        //cout<<out<<std::endl;
        //cout<<"-------------------------------------------------------"<<std::endl;

      }else{
        //cout<<"---input CRC----"<<endl;
        //cout<<in<<endl;
        crc = calculate_crc16(in, packet_length);
        //cout<<"CRC:"<<crc<<endl;
        //cout<<bitset<16>(crc)<<endl;
        //std::cout<< packet_length + packet_size_diff <<std::endl;
        memcpy((void*)out, (const void*)in, packet_length);
        memcpy((void*)(out + packet_length), &crc, d_crc_length);

      }
      return packet_length + packet_size_diff;


      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
    }

  } /* namespace comsys */
} /* namespace gr */

