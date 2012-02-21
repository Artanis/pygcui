"""Utility functions and objects for PygCUI

Copyright (c) 2012, Erik Youngren
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of Erik Youngren.

"""

from collections import namedtuple

import local

def highlighted(highlighted):
    return dict(
        fgcolor='black' if highlighted else 'white',
        bgcolor='white' if highlighted else 'black')

def calculate_align_x(align, width, surface_width):
    if align == local.ALIGN_LEFT:
        return 0
    elif align == local.ALIGN_RIGHT:
        return surface_width - width
    else: # align == local.ALIGN_CENTER:
        return (surface_width//2) - (width//2)

def calculate_align_y(align, height, surface_height):
    if align == local.ALIGN_TOP:
        return 0
    elif align == local.ALIGN_BOTTOM:
        return surface_height - 1
    else: # align == local.ALIGN_MIDDLE:
        return (surface_height//2) - (height//2)

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ...

    http://docs.python.org/py3k/library/itertools.html#itertools-recipes

    TODO: What liscensing is on recipies from Python documentation?

    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

Packing = namedtuple('Packing', 'expand fill type')
