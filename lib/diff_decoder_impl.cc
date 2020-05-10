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
#include "diff_decoder_impl.h"

namespace gr {
  namespace comsys {

    diff_decoder::sptr
    diff_decoder::make(unsigned int modulus, unsigned int initial_state)
    {
      return gnuradio::get_initial_sptr
        (new diff_decoder_impl(modulus, initial_state));
    }

    /*
     * The private constructor
     */
    diff_decoder_impl::diff_decoder_impl(unsigned int modulus, unsigned int initial_state)
      : gr::sync_block("diff_decoder",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1,  sizeof(unsigned char))),
          d_initial_state(initial_state),
          d_modulus(modulus)
    {}

    /*
     * Our virtual destructor.
     */
    diff_decoder_impl::~diff_decoder_impl()
    {
    }

    int
    diff_decoder_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const unsigned char *in = (const unsigned char*) input_items[0];
      unsigned char *out = (unsigned char*) output_items[0];
      unsigned init_state = d_initial_state;

      out[0] = (in[0] - init_state) % d_modulus;

      for(int i = 1; i < noutput_items; i++){
            out[i] = (in[i] - in[i-1]) % d_modulus;
            //last_out = out[i];
      }
      //d_last_out = last_out;

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace comsys */
} /* namespace gr */

