===============
:class:`Widget`
===============


.. class:: Widget


Methods
=======

.. method:: Widget.size_request()

    A tuple containing the preferred size of the widget.

Attributes
==========

.. attribute:: Widget.fgcolor

    The color of text rendered by this widget. By default this is ``None``,
    preserving existing text color.

.. attribute:: Widget.bgcolor

    The background cell color rendered by this widget. By default this is
    ``None``, preserving existing background color.

Signals
=======

============== ================================================================
Signal Name    Description
============== ================================================================
button-press   Mouse button is pressed.
button-release Mouse button is released.
mouse-enter    Mouse pointer enters widget.
mouse-leave    Mouse pointer leaves widget.
focus-in       Widget receives focus.
focus-out      Widget loses focus. 
key-release    Key on keyboard is released.
key-press      Key on keyboard is pressed.
show           Widget requests to be displayed.
hide           Widget becomes hidden.
delete         Widget requests to be deleted.
============== ================================================================
