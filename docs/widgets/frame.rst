==============
:class:`Frame`
==============

.. image:: images/frame.*

A frame displays a single child widget within a border, optionally with a
label at the top.

The borders do not collapse, so adjacent Frames will have a double border
between them.

.. class:: Frame(label=None)

Attributes
==========

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
