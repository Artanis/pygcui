=========
Box Model
=========

Like GTK+ 2 and 3, PygcUI builds layouts by placing widgets in other widgets,
allowing those parent widgets to control how screen space is allocated to the
child widgets. A top-level widget (such as :class:`Window`) creates the
display screen, and allocates the space to its children.

Space Allocation
================
An empty window widget (the octothorpes represent the window-manager's
border decoration)::
    
    ## Window Caption ################# X ##
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    #                                      # 
    ########################################

Quite boring. And a window only takes one child, so, to get a more interesting layout, the space the window provides must be sliced into pieces. The :class:`Box` is the primary method for allocating space to multiple child widgets, and is quite powerful.

Add one vertical Box to the window, and two labels to the box to give it something to work with::
    
    ## Window Caption ################# X ##
    #+------------------------------------+#
    #|                                    |#
    #|                                    |#
    #|              Label 1               |#
    #|                                    |#
    #|                                    |#
    #+------------------------------------+#
    #|                                    |#
    #|                                    |#
    #|              Label 2               |#
    #|                                    |#
    #|                                    |#
    #+------------------------------------+# 
    ########################################

The box split the space evenly between the two labels, as indicated by the
example borders. By default, widgets will :term:`expand` into extra space
owned by the parent widget :term:`fill` all of that space.

If a widget in a box is not set to expand, the box will only allocate it
the vertical space it requires::
    
    ## Window Caption ################# X ##
    #+------------------------------------+#
    #|              Label 1               |#
    #+------------------------------------+#
    #|                                    |#
    #|                                    |#
    #|                                    |#
    #|                                    |#
    #|              Label 2               |#
    #|                                    |#
    #|                                    |#
    #|                                    |#
    #|                                    |#
    #+------------------------------------+# 
    ########################################

If a widget is set to not fill, it will only be allocated the space it requires to render within, rather than the entire space it ended up with::
    
    ## Window Caption ################# X ##
    #+------------------------------------+#
    #|              Label 1               |#
    #+------------------------------------+#
    #|                                    |#
    #|                                    |#
    #|                                    |#
    #|             +-------+              |#
    #|             |Label 2|              |#
    #|             +-------+              |#
    #|                                    |#
    #|                                    |#
    #|                                    |#
    #+------------------------------------+# 
    ########################################

That space is still 'consumed' by the child widget, just not provided to it for
rendering.

This expand and fill property of the box is useful for several layouts.
The `Label 1` widget could be replaced by a heading, or menu bar. The `Label 2`
widget could then be a section or application body.

Turning this on its side, with a horizontal Box, you can create columns
instead of segments::
    
    ## Window Caption ################# X ##
    #+--------------------------+---------+#
    #|                          |         |#
    #|                          |         |#
    #|                          |         |#
    #|                          |         |#
    #|                          |         |#
    #|                          |         |#
    #|                          |         |#
    #|                          |         |#
    #|                          |         |#
    #|                          |         |#
    #|                          |         |#
    #+--------------------------+---------+# 
    ########################################

Boxes can be nested of course, allowing for fairly complex layouts::
    
    ## Window Caption ################# X ##
    #+--------------------------+---------+#
    #|+------------------------+|+-------+|#
    #||                        |||       ||#
    #||                        ||+-------+|#
    #||                        |||       ||#
    #||                        |||       ||#
    #||                        |||       ||#
    #||                        |||       ||#
    #||                        |||       ||#
    #|+------------------------+||       ||#
    #||                        |||       ||#
    #|+------------------------+|+-------+|#
    #+--------------------------+---------+# 
    ########################################

Color Inheritance
=================
With the exception of :class:`Window`, all widgets use ``None`` for their
foreground and background :term:`color`\ s, which preserves the colors
previously painted to their allocated cells. If a widget paints new colors to
its cells, those colors will propagate to its children, as well.
