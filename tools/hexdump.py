#!/bin/env python
# -*- coding: utf-8 -*-

# Hex dumper
# Copyright (c) 2009-2020, Mario Vilas
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice,this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Compatibility with Python 2.5.
from __future__ import with_statement

from winappdbg import HexDump

# Compatibility with Python 2.6 and earlier.
if hasattr(int, "bit_length"):
    def bit_length(num):
        return num.bit_length()
else:
    import math
    def bit_length(num):
        return int(math.log(num, 2))

def main(argv):
    print("Hex dumper using WinAppDbg")
    print("by Mario Vilas (mvilas at gmail.com)")
    print
    if len(argv) != 2:
        import os
        script = os.path.basename(argv[0])
        print("  %s <filename>" % script)
        return
    with open(argv[1], 'rb') as fd:
        fd.seek(0, 2)
        size = fd.tell()
        fd.seek(0, 0)
        if bit_length(size) > 32:
            width = 8
        else:
            width = 16
        address = 0
        while 1:
            data = fd.read(16)
            if not data:
                break
            print(HexDump.hexblock(data, address = address, width = width),)
            address = address + len(data)

if __name__ == '__main__':
    import sys
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    main(sys.argv)
