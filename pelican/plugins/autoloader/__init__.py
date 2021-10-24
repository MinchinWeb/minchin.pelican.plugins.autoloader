from pelican import signals

from minchin.pelican.plugins.autoloader import __version__, initialize


def register():
    """Register the plugin with Pelican"""
    signals.initialized.connect(initialize)
