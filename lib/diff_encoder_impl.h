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

#ifndef INCLUDED_COMSYS_DIFF_ENCODER_IMPL_H
#define INCLUDED_COMSYS_DIFF_ENCODER_IMPL_H

#include <comsys/diff_encoder.h>

namespace gr {
  namespace comsys {

    class diff_encoder_impl : public diff_encoder
    {
     private:
      unsigned int d_modulus;
      unsigned int d_last_out;


     public:
      diff_encoder_impl(unsigned int modulus, unsigned int initial_state);
      ~diff_encoder_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace comsys
} // namespace gr

#endif /* INCLUDED_COMSYS_DIFF_ENCODER_IMPL_H */

