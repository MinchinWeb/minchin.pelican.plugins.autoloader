import importlib
import logging
import pkgutil

import semantic_version

from pelican import __version__ as pelican_version
from pelican import signals


__title__ = "minchin.pelican.plugins.autoloader"
__version__ = "0.1.0+dev.0"
__description__ = "Pelican plug, used to auto-load my other plugins."
__author__ = "W. Minchin"
__email__ = "w_minchin@hotmail.com"
__url__ = "https://github.com/MinchinWeb/minchin.pelican.plugins.autoloader"
__license__ = "MIT License"

LOG_PREFIX = "[AutoLoader]"
DEFAULT_NAMESPACE_LIST = [
    "minchin.pelican.plugins",
]

logger = logging.getLogger(__name__)


def pelican_namespace_plugin_support():
    """
    Determine if the installed version of Pelican natively supports namespace
    plugins.

    In short, the Pelican version must be greater than or equal to 4.5.0.

    Return:
        bool: if namespace plugins are supported
    """

    pelican_semver = semantic_version.Version(pelican_version)
    if pelican_semver.major > 4:
        return True
    elif pelican_semver.major == 4 and pelican_semver.minor >= 5:
        return True
    else:
        return False


def initialize(pelican):
    logger.debug("%s loading plugins in the selected namespaces." % LOG_PREFIX)

    if "AUTOLOADER_NAMESPACES" in pelican.settings:
        namespace_list = pelican.settings["AUTOLOADER_NAMESPACES"]
    else:
        namespace_list = DEFAULT_NAMESPACE_LIST

    if pelican_namespace_plugin_support():
        # only namespace plugins otherwise; Pelican 4.5.0 or newer

        # imports here, as they won't exist in earlier versions of Pelican
        from pelican.plugins._utils import get_namespace_plugins

        for ns in namespace_list:
            logger.debug("%s     %s" % (LOG_PREFIX, ns))

            ns_module = importlib.import_module(ns)
            namespace_plugins = get_namespace_plugins(ns_module)
            pelican.plugins.extend(list(namespace_plugins.values()))

        pelican.init_plugins()

    else:
        if "PLUGINS" not in pelican.settings.keys():
            pelican.settings["PLUGINS"] = list()

        for ns in namespace_list:
            logger.debug("%s     %s" % (LOG_PREFIX, ns))
            ns_module = importlib.import_module(ns)
            plugin_iter = pkgutil.iter_modules(ns_module.__path__, ns_module.__name__ + ".")

            for k in plugin_iter:
                pelican.settings["PLUGINS"].append(k.name)
                logger.debug('%s "%s" appended to PLUGINS' % (LOG_PREFIX, k.name))
        # force update of plugins
        pelican.init_plugins()

def register():
    """Register the plugin with Pelican"""
    signals.initialized.connect(initialize)
