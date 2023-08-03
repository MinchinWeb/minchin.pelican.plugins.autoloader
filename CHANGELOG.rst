AutoLoader Changelog
====================

1.2.1 -- 2023-08-03
-------------------

- **bug**: don't break if no plugins exist in the namespace you are trying to load from.

1.2.0 -- 2023-07-11
-------------------

- **feature**: include autoloading from additional "private" namespace of
  ``minchin.pelican.readers``.

1.1.0 -- 2022-04-09
-------------------

- **feature**: allow autoloading of specificed plugins to be skipped via
  ``AUTOLOADER_PLUGIN_BLACKLIST`` variable (on Pelican 4.5+ only).
- **bug**: don't try and initialize ``pelican.plugins._utils`` or
  ``pelican.plugins.signals``

1.0.3 - 2022-03-20
------------------

- **support**: update to ``minchin.releaser`` 0.8.2, and thus officially support
  Python 3.10.

1.0.2 - 2021-10-24
------------------

- **feature**: original implementation
- **support**: first release to PyPI under `minchin.pelican.plugins.autoloader`_

.. _minchin.pelican.plugins.autoloader: https://pypi.org/project/minchin.pelican.plugins.autoloader/
