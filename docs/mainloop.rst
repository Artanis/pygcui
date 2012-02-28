=============
The Main Loop
=============

The main loop gathers events and other input from various sources, for
example, from the Pygame event queue, or from file-like objects.

Keyboard input is handled by the widget currently in focus. Mouse events are
handled by the widget the mouse pointer is in.

.. class:: MainLoop(top=None)