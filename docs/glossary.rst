Glossary of Terms
=================

.. glossary::
    :sorted:

    color
    background color
    foreground color
        A color recognizable by Pygcurse.

        Any of the following forms:

        1. A pygame.Color object
        2. A 3-tuple ``(red, green, blue)``, where ``red``, ``green``, ``blue``
           are integers in the range 0-255.
        3. A 4-tuple ``(red, green, blue, alpha)``, where ``red``, ``green``,
           ``blue``, ``alpha`` are integers in the range 0-255.
        4. A Pygcurse color name. See Pygcurse for more information.


    expand
        Widgets packed into a multi-widget container with the ``expand``
        option are allocated any extra space the parent container is allocated.

        If multiple child widgets expand, the extra space is distributed among
        them evenly.

    fill
        Widgets packed into a multi-widget container with the ``fill`` and
        ``expand`` options (``fill`` has no effect without ``expand``) are
        allocated any extra space (such as the space allocated by
        :term:`expand`, instead of being padded with it.