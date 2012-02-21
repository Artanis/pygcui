==============
PygcUI Widgets
==============

:class:`Box` widgets
====================

A container for multiple widgets, organized into vertical or horizontal stacks.

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


:class:`Button` widget
======================

.. class:: Button(label=None)

:class:`CheckButton` widget
===========================

.. class:: CheckButton

:class:`CheckMenuItem` widget
=============================

.. class:: CheckMenuItem

:class:`ComboBox` widget
========================

.. class:: ComboBox

:class:`DrawingArea` widget
===========================

.. class:: DrawingArea

:class:`Entry` widget
=====================

.. class:: Entry

:class:`Expander` widget
========================

.. class:: Expander

:class:`Frame` widget
=====================

.. class:: Frame

:class:`Label` widget
=====================

.. class:: Label

:class:`Menu` widget
====================

.. class:: Menu

:class:`MenuBar` widget
=======================

.. class:: MenuBar

:class:`MenuItem` widget
========================

.. class:: MenuItem

:class:`RadioButton` widget
===========================

.. class:: RadioButton

:class:`RadioMenuItem` widget
=============================

.. class:: RadioMenuItem

:class:`Range` widget
=====================

.. class:: Range

:class:`ScrolledWindow` widget
==============================

.. class:: ScrolledWindow

:class:`SeparatorMenuItem` widget
=================================

.. class:: SeparatorMenuItem

:class:`Table` widget
=====================

.. class:: Table

:class:`TextView` widget
========================

.. class:: TextView

:class:`ToggleButton` widget
============================

.. class:: ToggleButton

:class:`Viewport` widget
========================

.. class:: Viewport

:class:`Window` widget
======================

Windows are top-level widgets, creating a :class:`pygcurse.PygcurseWindow`
instance and allocating space from that window to its children.

Essentially, this is a very thin wrapper, setting up some basic options, such
as disabling autoupdate, and calling :meth:`pygcurse.PygcurseWindow.update`
after rendering is complete.

.. class:: Window(width=80, height=25, caption=None, fullscreen=None)


