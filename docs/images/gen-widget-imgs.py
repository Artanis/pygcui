# System Modules
import collections

# External Modules
import pygame
import pygcurse

# Local Modules

Schema = collections.namedtuple("Schema", "design width height fgcolor bgcolor")

design = {
    "button-up": Schema("[    Button    ]", 16, 1, "black", "gray"),
    "button-down": Schema("[    Button    ]", 16, 1, "gray",  "black"),
    "check-button-unchecked": Schema("[ ] Check Button", 16, 1, "black", "gray"),
    "check-button-checked": Schema("[*] Check Button", 16, 1, "black", "gray"),
    "radio-button-unchecked": Schema("( ) Radio Button", 16, 1, "black", "gray"),
    "radio-button-checked": Schema("(*) Radio Button", 16, 1, "black", "gray"),
    "entry": Schema("[_Entry________]", 16, 1, "black", "gray"),
    "combobox-menu": Schema("[ ComboBox  [v]]", 16, 1, "black", "gray"),
    "combobox-menu-active": Schema(width=16, height=5, fgcolor="black",
        bgcolor="gray",design=(
            "[ ComboBox  [v]]",
            "+--------------+",
            "| ComboBox     |",
            "| Item 2       |",
            "+--------------+")),
    "combobox-list": Schema(width=16, height=4, fgcolor='black',
        bgcolor='gray', design=(
            "+--------------+",
            "| Combo (list) |",
            "| Item 2       |",
            "+--------------+")),
    "expander-open": Schema(width=16, height=3, fgcolor='black',
        bgcolor='gray', design=(
            "[v] Expander    ",
            "################",
            "################")),
    "expander-close": Schema("[>] Expander   ", 16, 1, "black", "gray"),
    "frame": Schema(width=16, height=4, fgcolor='black', bgcolor='gray',
        design=(
            "+--Frame Label-+",
            "| Frame        |",
            "|         Body |",
            "+--------------+")),
    "range": Schema("[----------O---]", 16, 1, 'black', 'gray')
}


def main():
    for filename, schema in design.items():
        surface = pygcurse.PygcurseSurface(
            schema.width, schema.height, windowsurface="new_window")

        if schema.height > 1:
            for row, text in enumerate(schema.design):
                surface.putchars(text, x=0, y=row,
                    fgcolor=schema.fgcolor, bgcolor=schema.bgcolor)
        else:
            surface.putchars(schema.design,
                fgcolor=schema.fgcolor, bgcolor=schema.bgcolor)
        pygame.image.save(surface._windowsurface, filename+".png")

if __name__ == "__main__":
    main()
