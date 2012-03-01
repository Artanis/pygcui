===============
:class:`Window`
===============

Windows are top-level widgets, creating a :class:`pygcurse.PygcurseWindow`
instance and allocating space from that window to its children.

Essentially, this is a very thin wrapper, setting up some basic options, such
as disabling autoupdate, and calling :meth:`pygcurse.PygcurseWindow.update`
after rendering is complete.

.. class:: Window(width=80, height=25, caption=None, fullscreen=None)
