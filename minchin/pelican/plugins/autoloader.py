import importlib
import logging
import pkgutil

import semantic_version

from pelican import __version__ as pelican_version
from pelican import signals

__title__ = "minchin.pelican.plugins.autoloader"
__version__ = "1.0.3-dev"
__description__ = "Pelican plugin, used to auto-load my other plugins."
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


def initialize(pelican_instance):
    if "AUTOLOADER_SIGNAL_INITALIZED" not in pelican_instance.settings.keys():
        logger.debug("%s loading plugins in the selected namespaces." % LOG_PREFIX)

        if "AUTOLOADER_NAMESPACES" in pelican_instance.settings:
            namespace_list = pelican_instance.settings["AUTOLOADER_NAMESPACES"]
        else:
            namespace_list = DEFAULT_NAMESPACE_LIST

        if pelican_namespace_plugin_support():
            # only namespace plugins otherwise; Pelican 4.5.0 or newer

            for ns in namespace_list:
                logger.debug("%s     %s" % (LOG_PREFIX, ns))

                ns_module = importlib.import_module(ns)
                # this differs from Pelican's built-in namespace plugin finder,
                # in that we don't require plugins to be their own modules
                namespace_plugins = {
                    name: importlib.import_module(name)
                    for _, name, _ in pkgutil.iter_modules(
                        ns_module.__path__, ns_module.__name__ + "."
                    )
                }
                for plugin_name, plugin_pkg in namespace_plugins.items():
                    logger.debug("%s         %s" % (LOG_PREFIX, plugin_name))
                    # manually register plugins
                    try:
                        plugin_pkg.register()
                    except Exception as e:
                        logger.error(
                            "Cannot register plugin `%s`\n%s", plugin_pkg.__name__, e
                        )

        else:
            if "PLUGINS" not in pelican_instance.settings.keys():
                pelican_instance.settings["PLUGINS"] = list()

            for ns in namespace_list:
                logger.debug("%s     %s" % (LOG_PREFIX, ns))
                ns_module = importlib.import_module(ns)
                plugin_iter = pkgutil.iter_modules(
                    ns_module.__path__, ns_module.__name__ + "."
                )

                for k in plugin_iter:
                    pelican_instance.settings["PLUGINS"].append(k.name)
                    logger.debug(
                        '%s         "%s" appended to PLUGINS' % (LOG_PREFIX, k.name)
                    )
            # force update of plugins
            pelican_instance.init_plugins()

        pelican_instance.settings["AUTOLOADER_SIGNAL_INITALIZED"] = True
        # needed, in case any of these plugins are calling the "initialized" signal
        logger.debug("%s signal: initalized" % LOG_PREFIX)
        signals.initialized.send(pelican_instance)
    else:
        # avoid recurssion
        pass


def register():
    """Register the plugin with Pelican"""
    signals.initialized.connect(initialize)
