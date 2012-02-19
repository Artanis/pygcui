"""PygCUI widgets

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

import logging
import collections
from itertools import repeat, accumulate

import pygame
import pygcurse

import util
import local

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s')

def mainloop():
    """Gather and dispatch events.

    TODO: Write.

    """
    running = True
    while running:
        pass

class Widget:
    """Base class for all pygui widgets.

    """
    def __init__(self):
        logging.info("new Widget {0!r}".format(self))
    
    def render(self, surface):
        pass


class Container(Widget):
    """Base class for widgets that contain other widgets.

    """
    def __init__(self):
        super().__init__()

    def add(self, widget):
        """Adds the widget to the container, using simple defaults for multiple-child containers.

        """
        logging.info('add {0!r} to {1!r}'.format(widget, self))

    def remove(self, widget):
        """Removes the widget from the container.

        """
        logging.info('remove {0!r} from {1!r}'.format(widget, self))

    def __iter__(self):
        """Returns an iterator for all non-internal child widgets contained.

        """
        pass


class Bin(Container):
    """Base class for containers with one child.

    """
    def __init__(self):
        super().__init__()
        self.child = None

    def add(self, widget):
        super().add(widget)
        self.child = widget

    def remove(self, widget):
        super().remove(widget)
        if self.child is widget:
            self.child = None

    def render(self, surface):
        super().render(surface)
        if self.child is not None:
            self.child.render(surface)

    def __iter__(self):
        if self.child is not None:
            return iter([self.child])
        else:
            return iter([])


class Button(Bin):
    """A push button that emits a signal when activated.

    """
    pass

class ToggleButton(Button):
    """A button that retains its state.

    """
    pass

class CheckButton(ToggleButton):
    """A toggle button styled as a checkbox and label.

    """
    pass

class RadioButton(CheckButton):
    """A toggle button that is mutually exclusive with other radio buttons in
    it's group.

    """
    pass

class ComboBox(Bin):
    """Choose from a list of items.

    TODO: Figure out how this will work. See Menu.

    """
    pass

class Expander(Bin):
    """A widget that can hide it's child.

    """
    pass


class Frame(Bin):
    """A bin with a decorative frame and optional label.

    """
    def __init__(self, label=None):
        self.label = label
        super().__init__()

    def render(self, surface):
        surface.fill(' ', bgcolor='gray')
        
        # render children
        child_width, child_height = surface.width-2, surface.height-2
        
        if child_width > 0 and child_height > 0:
        
            child_surface = pygcurse.PygcurseSurface(
                surface.width-2, surface.height-2)
        
            super().render(child_surface)
        
            child_surface.paste(None, surface,
                (1, 1, surface.right-1, surface.bottom-1))

        # render label
        lbl_width, lbl_height = self.label.size
        
        if lbl_width > surface.width - 2:
            lbl_width = surface.width - 2
        elif lbl_width+2 < surface.width:
            lbl_width = lbl_width + 2
        
        if lbl_width > 0 and lbl_height > 0:
            lbl_surface = pygcurse.PygcurseSurface(lbl_width, lbl_height)
            
            self.label.render(lbl_surface)
            
            lbl_surface.paste(None, surface,
                (surface.centerx - lbl_surface.width // 2, 0,
                lbl_surface.width, lbl_surface.height))

    def __repr__(self):
        return "<pygcui.Frame {0!r}>".format(str(self.label))


class Item(Bin):
    """Base class for MenuItem.

    Note: Probably will be removed.

    """
    pass

class MenuItem(Item):
    """Widget used as an item in menus.

    """
    pass

class CheckMenuItem(MenuItem):
    """A toggle-able menu item styled as a checkbox and label.

    """
    pass

class RadioMenuItem(CheckMenuItem):
    """A check menu item that is mutually exclusive with other radio menu items
    in it's group.

    """
    pass

class SeparatorMenuItem(MenuItem):
    """A widget that places a horizontal line in a menu.

    """
    pass

class ScrolledWindow(Bin):
    """Add scrollbars to the child widget.

    """
    pass

class Viewport(Bin):
    """Displays a portion of a larger widget.

    Can be used to allow scrolling of the larger widget. The larger widget
    will render at it's preferred size, and the Viewport will choose which
    part is copied to the allocated surface.

    """
    pass

class Window(Bin):
    """A top-level widget that contains one child.

    Creates a pygcurse.PygcurseWindow.

    """
    def __init__(self, width=80, height=25, caption=None, fullscreen=False):
        self._caption = caption
        self._width = width
        self._height = height
        super().__init__()
        self._windowsurface = pygcurse.PygcurseWindow(
            self._width, self._height, self._caption,
            fullscreen=fullscreen)
        self._windowsurface.autoupdate = False

    def render(self, surface=None):
        logging.debug("render {0!r}".format(self))
        super().render(self._windowsurface)
        self._windowsurface.update()

    def __repr__(self):
        return "<pygcui.Window {0!r} ({1}, {2})>".format(
            self._caption, self._width, self._height)


class Box(Container):
    """A class containing multiple widgets, organized into vertical or
    horizontal stacks.

    TODO: Respect homogeneity (currently forces homogeneous).

    """
    def __init__(self, orientation=local.HORIZONTAL):
        super().__init__()
        self.homogenous = True
        self.orientation = orientation
        self.spacing = 0
        self.children = collections.OrderedDict()

    def pack_start(self, child, expand=True, fill=True):
        logging.info(
            "packing {0!r} into {1!r} (start, expand={2}, fill={3})".format(
                child, self, expand, fill))
        
        self.children[child] = util.Packing(
            expand, fill, local.PACK_START)

    def pack_end(self, child, expand=True, fill=True):
        logging.info(
            "packing {0!r} into {1!r} (end, expand={2}, fill={3})".format(
                child, self, expand, fill))

        self.children[child] = util.Packing(
            expand, fill, local.PACK_END)
        self.children.move_to_end(child, last=False)

    def _child_allocations(self, width, height):
        if len(self.children) < 1:
            return []

        if self.orientation == local.HORIZONTAL:
            size = width
        else:
            size = height

        extra = size // len(self.children)
        n_extra = size % len(self.children)

        logging.debug(
            "allocating {0} of {1} to each of {2} children. {3} left.".format(
                extra, size, len(self.children), n_extra))

        sizes = [extra for n in self.children]

        for i, s in enumerate(sizes[:]):
            if n_extra < 1:
                break
            
            sizes[i] = sizes[i] + 1
            n_extra = n_extra - 1

        if self.orientation == local.HORIZONTAL:
            sizes = tuple(zip(
                (s-sizes[i] for i, s in enumerate(accumulate(sizes))),
                repeat(0, len(sizes)),
                sizes,
                repeat(height, len(sizes))))
        else:
            sizes = tuple(zip(
                repeat(0, len(sizes)),
                (s-sizes[i] for i, s in enumerate(accumulate(sizes))),
                repeat(width, len(sizes)),
                sizes))

        logging.debug("final allocations {0!r}".format(sizes))

        return sizes

    def add(self, widget):
        self.pack_start(widget)

    def remove(self, widget):
        try:
            del self.children[widget]
        except KeyError:
            raise ValueError((
                "Non-related widget. "
                "Widget must be a child of container."))

    def render(self, surface):
        super().render(surface)
        sizes = self._child_allocations(*surface.size)

        for child, region in zip(self.children, sizes):
            child_surface = pygcurse.PygcurseSurface(
                region[2], region[3])

            child.render(child_surface)
            child_surface.paste(None, surface, region)


    def __iter__(self):
        return iter(self.children)

class MenuShell(Container):
    """A base class for menus.

    """
    pass

class Menu(MenuShell):
    """A drop down menu.

    TODO: Figure out how this will work. See combobox.

    """
    pass

class MenuBar(MenuShell):
    """Displays MenuItems horizontally.

    """
    pass

class Table(Container):
    """Arranges widgets in a grid

    """
    pass

class TextView(Container):
    """Displays text.

    """
    pass


class DrawingArea(Widget):
    """Widget for custom user-interface elements.

    """
    pass


class Entry(Widget):
    """A single-line text entry field.

    """
    pass


class Label(Widget):
    """Displays a single line of non-editable text.

    """
    def __init__(self, text=None):
        self.text = text
        self.fgcolor = 'gray'
        self.bgcolor = 'black'
        self.alignx = local.ALIGN_CENTER
        self.aligny = local.ALIGN_MIDDLE

    @property
    def size(self):
        return (len(self.text), 1)

    def _calculate_align_x(self, width, surface_width):
        if self.alignx == local.ALIGN_LEFT:
            return 0
        elif self.alignx == local.ALIGN_RIGHT:
            return surface_width - width
        else: # self.alignx == local.ALIGN_CENTER:
            return (surface_width//2) - (width//2)

    def _calculate_align_y(self, height, surface_height):
        if self.aligny == local.ALIGN_TOP:
            return 0
        elif self.aligny == local.ALIGN_BOTTOM:
            return surface_height - 1
        else: # self.aligny == local.ALIGN_MIDDLE:
            return (surface_height//2) - (height//2)


    def render(self, surface):
        """Render the label to the given surface.

        """
        super().render(surface)
        
        w, h = self.size
        x = self._calculate_align_x(w, surface.width)
        y = self._calculate_align_y(h, surface.height)
        logging.debug('render label {0!r} in ({1}, {2}) at ({3}, {4})'.format(self, surface.width, surface.height, x, y))

        surface.putchars(self.text, x=x, y=y, bgcolor=self.bgcolor, fgcolor=self.fgcolor)

    def __str__(self):
        return self.text

    def __repr__(self):
        return "<pygcui.Label {0!r}>".format(self.text)


class Range(Widget):
    """Base class for widgets that allow the user to set a value in a
    range.

    """
    pass
