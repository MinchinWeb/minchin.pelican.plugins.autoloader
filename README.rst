==========
AutoLoader
==========

|pypi|

.. |pypi| image:: https://img.shields.io/pypi/v/minchin.pelican.plugins.autoloader.svg
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.autoloader
    :alt: PyPI Version

``AutoLoader`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``AutoLoader`` is designed to autoload the other Pelican plugins in my
namespace (``minchin.pelican.plugins``). It can also be extended to autoload
plugins in other namespaces, for example, to autoload the ``pelican.plugins``
namespace on versions of Pelican before 4.5 (when autoloading to those plugins
was added to the Pelican core).
    
Installation
============

The easiest way to install ``AutoLoader`` is through the use of pip. This
will also install the required dependencies automatically.

.. code-block:: sh

  pip install minchin.pelican.plugins.autoloader

Further configuration will depend on the version of Pelican you are running. On
version 4.5 or newer and you haven't defined ``PLUGINS`` in your
``pelicanconf.py``, nothing more in needed. On earlier versions of Pelican, or
if you've defined ``PLUGINS``, you'll need to add the autoloader to your list
of plugins in your ``pelicanconf.py`` file:

.. code-block:: python

  PLUGINS = [
      # ...
      'minchin.pelican.plugins.autoloader',
      # ...
  ]

if you want to auto-load additional namespaces, you'll need to define the
``AUTOLOADER_NAMESPACES`` variable in your ``pelicanconf.py`` file:

.. code-block:: python

  from minchin.pelican.plugins import autoloader

  AUTOLOADER_NAMESPACES = autoloader.DEFAULT_NAMESPACE_LIST + [
      "pelican.plugins",
      # other namespaces
  ]

Usage Notes
===========

- the plugins loaded by this plugin will not be shown when you run
  ``pelican-plugins``


