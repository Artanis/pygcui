============
:class:`Box`
============

:class:`Widget` > :class:`Container` > :class:`Box`

.. class:: Box(vertical=True)
    
    A container for multiple widgets, organized into a vertical or horizontal
    stack.

Methods
=======

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

Attributes
==========

.. attribute:: Box.vertical

    If True, causes the :class:`Box` to layout child widgets as a vertical
    stack. Otherwise, child widgets will be in a horizontal stack.

.. attribute:: Box.homogeneous

    If true, child widgets are forced to have the same amount of space,
    overriding the child's packing settings.
