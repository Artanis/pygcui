==============
PygcUI Widgets
==============

:class:`Box` widgets
====================

A container for multiple widgets, organized into a vertical or horizontal
stack.

.. class:: Box(vertical=True)
    
    Create a new :class:`Box` instance.

    .. method:: Box.pack_start(widget, expand=True, fill=True)

        Adds the widget to the Box. New widgets are packed towards the middle
        of the stack, after any other widgets added with :meth:`pack_start`,
        and before and widgets added with :meth:`pack_end`.

        The :term:`expand` and :term:`fill` arguments determine how extra
        space is allocated to the child widget.

    .. method:: Box.pack_end(widget, expand=True, fill=True)
        
        Adds the widget to the Box. New widgets are packed towards the middle
        of the stack, before any other widgets added with :meth:`pack_end`,
        and after any widgets added with :meth:`pack_start`

        The :term:`expand` and :term:`fill` arguments determine how extra
        space is allocated to the child widget.

    .. method:: Box.add(widget)

        Adds the widget using default options. Default options may not be
        ideal. Use :meth:`pack_start` or :meth:`pack_end` for full control over
        packing.

    .. method:: Box.remove(widget)

        Removes the specified widget from the Box.

    .. attribute:: Box.vertical

        If True, causes the :class:`Box` to layout child widgets as a vertical
        stack. Otherwise, child widgets will be in a horizontal stack.

    .. attribute:: Box.homogeneous

        If true, child widgets are forced to have the same amount of space,
        overriding the child's packing settings.


:class:`Button` widgets
=======================

A push button that emits a signal when activated.

.. image:: images/button-up.*

.. image:: images/button-down.*

.. class:: Button(label=None)
    
    .. method:: Button.clicked

        Emits a ``clicked`` signal.

    .. attribute:: Button.alignx

        Horizontal alignment of the label the button. Not to be confused with
        the alignment of the text within the label.

    .. attribute:: Button.aligny

        Vertical alignment of the label within the button. Not to be confused
        with the alignment of the text within the label.

    .. attribute:: Button.fgcolor

        The color of the button 

    .. attribute:: Button.bgcolor


=========== ===================================================================
Signal      Emitted
=========== ===================================================================
activate    Emitted when :meth:`Widget.activate` is called. Causes a
            ``clicked`` signal to be emitted.
clicked     Emits when mouse button is pressed and released over the button,
            or when :meth:`Button.clicked` is called.
=========== ===================================================================

:class:`CheckButton` widgets
============================

.. image:: images/check-button-unchecked.*

.. image:: images/check-button-checked.*

A :class:`ToggleButton` styled as a checkbox and label.

.. class:: CheckButton
    
    .. method:: CheckButton.clicked

        Emits a ``clicked`` signal.

    .. attribute:: CheckButton.active

        True if checkbox is checked. Changing this attribute causes the
        ``toggled`` signal to be emitted.

    .. .. attribute:: CheckButton.alignx

    .. .. attribute:: CheckButton.aligny

    .. attribute:: CheckButton.fgcolor

    .. attribute:: CheckButton.bgcolor

:class:`CheckMenuItem` widgets
==============================

A toggle-able menu item styled as a checkbox and label.

.. class:: CheckMenuItem

:class:`ComboBox` widgets
=========================

.. image:: images/combobox-menu.*

.. image:: images/combobox-menu-active.*

.. image:: images/combobox-list.*

A widget that allows the user to choose from a list of items.

.. class:: ComboBox

    .. attribute:: ComboBox.active

        Index of currently active item.

:class:`DrawingArea` widgets
============================

A widget for custom user-interface elements.

.. class:: DrawingArea()

    .. attribute:: DrawingArea.window

        A :class:`pygcurse.PygcurseSurface` to draw on.

:class:`Entry` widgets
======================

.. image:: images/entry.*

A single-line text entry field.

.. class:: Entry

:class:`Expander` widgets
=========================

.. image:: images/expander-close.*

.. image:: images/expander-open.*

A container that can hide it's child.

.. class:: Expander

:class:`Frame` widgets
======================

.. image:: images/frame.*

A frame displays a single child widget within a border, optionally with a
label at the top.

The borders do not collapse, so adjacent Frames will have a double border
between them.

.. class:: Frame(label=None)

    .. attribute:: Frame.label

        A :class:`Label` widgets. This label will be allocated 1 row, and any
        space required up to the corners of the frame.

        The label will render using it's own colors.

    .. attribute:: Frame.border_corners

        A single character to use for each corner of the frame, or a sequence
        of 4 characters ``(topleft, topright, bottomleft, bottomright)``. By
        default, a single space ``' '``.

    .. attribute:: Frame.border_vertical

        A single character to use for the vertical portion of the border. By
        default, a space ``' '``.

    .. attribute:: Frame.border_horizontal

        A single character to use for the horizontal portion of the border. By
        default, a space ``' '``.


    .. attribute:: Frame.fgcolor

        The :term:`foreground color` of the border. By default, the frame will
        only be rendered using the background color. If characters, such as
        box-drawing glyphs, are used, they will use this color.

    .. attribute:: Frame.bgcolor

        The :term:`background color` of the border.

    .. attribute:: Frame.align

        The alignment of the :attr:`Frame.label` widgets. Not to be confused
        with the alignment of the text within the label.

        :attr:`local.ALIGN_LEFT`
            The label is positioned in the top left corner of the Frame.

        :attr:`local.ALIGN_CENTER`
            The label is positioned in the center of the top border of the
            Frame. This is the default position.

        :attr:`local.ALIGN_RIGHT`
            The label is positioned near the right top corner of the Frame. 


:class:`Label` widgets
======================

Displays read-only text.

.. class:: Label(text=None)
    
    .. attribute:: Label.text

        The text of this label.

    .. attribute:: Label.fgcolor

        The :term:`foreground color` (text color) this label is rendered with.

    .. attribute:: Label.bgcolor

        The :term:`background color` (behind the text and filling any extra
        space) of the label.

    .. attribute:: Label.alignx

        How the label text is aligned horizontally.

        :attr:`local.ALIGN_LEFT`
            Label text is aligned to the left side of the allocated space,
            with the first character in the first column.
        
        :attr:`local.ALIGN_CENTER`
            Label text is aligned in the center.

        :attr:`local.ALIGN_RIGHT`
            Label text is aligned to the right, with the last character in the
            last column.

    .. attribute:: Label.aligny

        How the label text is positioned vertically.

        :attr:`local.ALIGN_TOP`
            Label text is positioned in the first row of the allocated space.

        :attr:`local.ALIGN_MIDDLE`
            Label text is positioned in the center.

        :attr:`local.ALIGN_BOTTOM`
            Label text is positioned in the last row.

    .. attribute:: Label.size

        A tuple ``(width, height)`` of the minimum size the label requires to
        fully display the label text in a single line.

:class:`Menu` widgets
=====================

A drop-down menu.

.. class:: Menu

:class:`MenuBar` widgets
========================

A widget that displays menu items horizontally.

.. class:: MenuBar

:class:`MenuItem` widgets
=========================

A widget for use in menus.

.. class:: MenuItem

:class:`RadioButton` widgets
============================

A toggle button that is mutually exclusive with other radio buttons in it's
group.

.. image:: images/radio-button-unchecked.*

.. image:: images/radio-button-checked.*

.. class:: RadioButton

    .. method:: RadioButton.clicked

    .. attribute:: RadioButton.active

    .. attribute:: RadioButton.alignx

    .. attribute:: RadioButton.aligny

    .. attribute:: RadioButton.fgcolor

    .. attribute:: RadioButton.bgcolor

:class:`RadioMenuItem` widgets
==============================

A check menu item that is mutually exclusive with other radio menu items in
it's group.

.. class:: RadioMenuItem

:class:`Range` widgets
======================

A widget for choosing from a number range.

.. image:: images/range.*

.. class:: Range

:class:`ScrolledWindow` widgets
===============================

Adds scrollbars to the child widget. Useful with a :class:`Viewport` to add
scrolling to larger widgets.

.. class:: ScrolledWindow

:class:`SeparatorMenuItem` widgets
==================================

Draws a horizontal line in a menu.

.. class:: SeparatorMenuItem

:class:`Table` widgets
======================

Arrange child widgets in a grid.

.. class:: Table

:class:`TextBuffer` objects
===========================

A TextBuffer is not a widget, but storage for text another widget displays.
Allows some minor text formatting, which the displaying widget may or may not
honor.

.. class:: TextBuffer

:class:`TextView` widgets
=========================

Render text from a :class:`TextBuffer`.

.. class:: TextView

:class:`ToggleButton` widgets
=============================

A button that retains it's state.

.. class:: ToggleButton
    
    .. method:: ToggleButton.clicked

    .. attribute:: ToggleButton.active

    .. attribute:: ToggleButton.alignx

    .. attribute:: ToggleButton.aligny

    .. attribute:: ToggleButton.fgcolor

    .. attribute:: ToggleButton.bgcolor

:class:`Viewport` widgets
=========================

A widget that renders it's child within any space it needs, but only displays
a portion of it.

.. class:: Viewport

:class:`Window` widgets
=======================

Windows are top-level widgets, creating a :class:`pygcurse.PygcurseWindow`
instance and allocating space from that window to its children.

Essentially, this is a very thin wrapper, setting up some basic options, such
as disabling autoupdate, and calling :meth:`pygcurse.PygcurseWindow.update`
after rendering is complete.

.. class:: Window(width=80, height=25, caption=None, fullscreen=None)


