PygcUI v0.1 incomplete
======================

PygcUI (**Pygc**\ urse **UI**) is a user interface library for Pygcurse.

API inspired by PyGTK. While mostly similar, GTK-style attribute access
(getters/setters and set/get property calls) is replaced by standard Python
attribute access, or, if necessary, property access.

`Documentation`_ can be found at the excellent `Read The Docs`_ website.

PygcUI will never include all of PyGTK's features. Some will not work in a text
interface, or have analogues through Pygcurse's or Pygame's feature sets. For
example, text mark-up will be extremely limited, being restricted to Pygcurse's
text-formatting; Drawing functions will not be included, as Pygcurse offers
some simple drawing capabilities, and the Pygame surfaces can be accessed and
drawn to. Other features only seem like they won't work correctly. Patches for
those are welcome.

PygcUI requires `Pygame`_ and and `Pygcurse`_.

.. _Documentation: http://pygcui.readthedocs.org/

.. _Read The Docs: http://readthedocs.org/

.. _Pygame: http://pygame.org

.. _Pygcurse: https://github.com/asweigart/pygcurse

=======
License
=======

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
