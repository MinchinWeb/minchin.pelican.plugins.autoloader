==========
AutoLoader
==========

``AutoLoader`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``AutoLoader`` is designed to autoload the other Pelican plugins in my
namespace (``minchin.pelican.plugins``). It can also be extended to autoload
plugins in other namespaces, for example, to autoload the ``pelican.plugins``
namespace on versions of Pelican before 4.5 (when autoloading to those plugins
was added to the Pelican core).

.. image:: https://img.shields.io/pypi/v/minchin.pelican.plugins.autoloader.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.autoloader
    :alt: PyPI version number

.. image:: https://img.shields.io/pypi/pyversions/minchin.pelican.plugins.autoloader?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.autoloader/
    :alt: Supported Python version

.. image:: https://img.shields.io/pypi/l/minchin.pelican.plugins.autoloader.svg?style=flat&color=green
    :target: https://github.com/MinchinWeb/minchin.pelican.plugins.autoloader/blob/master/LICENSE
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

Known Issues
============

The release process (``minchin.releaser``) depends on ``invoke``, which has yet
to release a version that will run on Python 3.10. Therefore, releases must be
generated on Python 3.9 or earlier, but the code should otherwise run on Python
3.10.
