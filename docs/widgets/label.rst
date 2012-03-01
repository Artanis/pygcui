==============
:class:`Label`
==============

Displays read-only text.

.. class:: Label(text=None)
    
Attributes
==========

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
