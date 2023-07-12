==========
AutoLoader
==========

``AutoLoader`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``AutoLoader`` is designed to autoload the other Pelican plugins in my
namespaces (``minchin.pelican.plugins`` and ``minchin.pelican.readers``).
It can also be extended to autoload
plugins in other namespaces, for example, to autoload the ``pelican.plugins``
namespace on versions of Pelican before 4.5 (when autoloading to those plugins
was added to the Pelican core).

.. image:: https://img.shields.io/pypi/v/minchin.pelican.plugins.autoloader.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.autoloader
    :alt: PyPI version number

.. image:: https://img.shields.io/badge/-Changelog-success?style=flat
    :target: https://github.com/MinchinWeb/minchin.pelican.plugins.autoloader/blob/master/CHANGELOG.rst
    :alt: Changelog

.. image:: https://img.shields.io/pypi/pyversions/minchin.pelican.plugins.autoloader?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.autoloader/
    :alt: Supported Python version

.. image:: https://img.shields.io/pypi/l/minchin.pelican.plugins.autoloader.svg?style=flat&color=green
    :target: https://github.com/MinchinWeb/minchin.pelican.plugins.autoloader/blob/master/LICENSE.txt
    :alt: License

.. image:: https://img.shields.io/pypi/dm/minchin.pelican.plugins.autoloader.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.autoloader/
    :alt: Download Count


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

  # pelicanconf.py

  PLUGINS = [
      # ...
      'minchin.pelican.plugins.autoloader',
      # ...
  ]

If you want to auto-load additional namespaces, you'll need to define the
``AUTOLOADER_NAMESPACES`` variable in your ``pelicanconf.py`` file:

.. code-block:: python

  # pelicanconf.py

  from minchin.pelican.plugins import autoloader

  AUTOLOADER_NAMESPACES = autoloader.DEFAULT_NAMESPACE_LIST + [
      "pelican.plugins",
      # other namespaces
  ]

If you need to disallow auto-loading of certain plugins, you'll need to define
the ``AUTOLOADER_PLUGIN_BLACKLIST`` variable in your ``pelicanconf.py`` file.
This only works when autoloading from defined namespaces. E.g.:

.. code-block:: python

  # pelicanconf.py

  from minchin.pelican.plugins import autoloader

  AUTOLOADER_PLUGIN_BLACKLIST = autoloader.DEFAULT_PLUGIN_BLACKLIST + [
      "pelican.plugins.misbehaving_plugin",
      # other plugins
  ]

Usage Notes
===========

- the plugins loaded by this plugin will not be shown when you run
  ``pelican-plugins``
