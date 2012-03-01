===============
:class:`Button`
===============

A push button that emits a signal when activated.

.. image:: images/button-up.*

.. image:: images/button-down.*

.. class:: Button(label=None)

Methods
=======
    
.. method:: Button.clicked

    Emits a ``clicked`` signal.

.. attribute:: Button.alignx

    Horizontal alignment of the label the button. Not to be confused with
    the alignment of the text within the label.

Attributes
==========

.. attribute:: Button.aligny

    Vertical alignment of the label within the button. Not to be confused
    with the alignment of the text within the label.

.. attribute:: Button.fgcolor

    The color of the button 

.. attribute:: Button.bgcolor

Signals
=======

=========== ===================================================================
Signal      Emitted
=========== ===================================================================
activate    Emitted when :meth:`Widget.activate` is called. Causes a
            ``clicked`` signal to be emitted.
clicked     Emits when mouse button is pressed and released over the button,
            or when :meth:`Button.clicked` is called.
=========== ===================================================================
