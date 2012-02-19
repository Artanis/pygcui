"""PygCUI is a user interface library for pygcurse.

API inspired by PyGTK. While mostly similar, GTK-style attribute access
(getters/setters and set/get property calls) is replaced by standard Python
attribute access, or, if necessary, property access.


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

import util
import local
from widgets import *

def main():
    window = Window(caption='Demo Window')
    frame_test = Frame(Label('Frame Label'))
    box = Box(orientation=local.VERTICAL)
    lbl_test1 = Label('Packed Label 1')
    lbl_test1.aligny = local.ALIGN_BOTTOM
    lbl_test2 = Label('Packed Label 2')
    lbl_test2.alignx = local.ALIGN_LEFT
    lbl_test3 = Label('Packed Label 3')
    lbl_test3.alignx = local.ALIGN_RIGHT
    lbl_test3.aligny = local.ALIGN_TOP

    box.pack_start(lbl_test1)
    box.pack_start(lbl_test2)
    box.pack_start(lbl_test3)
    frame_test.add(box)
    window.add(frame_test)

    window.render()
    input()
    pygame.quit()

if __name__ == "__main__":
    main()
