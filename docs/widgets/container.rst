=========================
:class:`Container` widget
=========================

:class:`Widget` > :class:`Container`

.. class:: Container
    
    Base class for widgets that contain other widgets.

Methods
=======

.. method:: Container.add(widget)

.. method:: Container.remove(widget)

Attributes
==========

.. attribute:: Container.children
    
    Non-internal children of the container.

Signals
=======

=============== ===============================================================
Signal Name     Description
=============== ===============================================================
add             A child widget is added to the container.
remove          A child widget is removed from the container.
=============== ===============================================================
