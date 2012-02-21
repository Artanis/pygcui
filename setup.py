try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="pygcui", version="0.1-dev",
    author="Erik Youngren", author_email="artanis.00@gmail.com",
    url="https://github.com/Artanis/pygcui",
    license="Simplified BSD License",
    keywords=" pygame pygcurse widget user interface curses text",
    description="A user interface library for pygcurse.",
    packages=['pygcui'],
    )