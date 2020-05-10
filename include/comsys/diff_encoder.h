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


#ifndef INCLUDED_COMSYS_DIFF_ENCODER_H
#define INCLUDED_COMSYS_DIFF_ENCODER_H

#include <comsys/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace comsys {

    /*!
     * \brief <+description of block+>
     * \ingroup comsys
     *
     */
    class COMSYS_API diff_encoder : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<diff_encoder> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of comsys::diff_encoder.
       *
       * To avoid accidental use of raw pointers, comsys::diff_encoder's
       * constructor is in a private implementation
       * class. comsys::diff_encoder::make is the public interface for
       * creating new instances.
       */
      static sptr make(unsigned int modulus, unsigned int initial_state);
    };

  } // namespace comsys
} // namespace gr

#endif /* INCLUDED_COMSYS_DIFF_ENCODER_H */

