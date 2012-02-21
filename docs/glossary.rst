Glossary of Terms
=================

.. glossary::
    :sorted:

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