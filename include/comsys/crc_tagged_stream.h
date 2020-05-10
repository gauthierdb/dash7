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


#ifndef INCLUDED_COMSYS_CRC_TAGGED_STREAM_H
#define INCLUDED_COMSYS_CRC_TAGGED_STREAM_H

#include <comsys/api.h>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace comsys {

    /*!
     * \brief <+description of block+>
     * \ingroup comsys
     *
     */
    class COMSYS_API crc_tagged_stream : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<crc_tagged_stream> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of comsys::crc_tagged_stream.
       *
       * To avoid accidental use of raw pointers, comsys::crc_tagged_stream's
       * constructor is in a private implementation
       * class. comsys::crc_tagged_stream::make is the public interface for
       * creating new instances.
       */
      static sptr make(bool check, const std::string& tag);
    };

  } // namespace comsys
} // namespace gr

#endif /* INCLUDED_COMSYS_CRC_TAGGED_STREAM_H */

