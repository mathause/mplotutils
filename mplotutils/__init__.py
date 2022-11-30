# flake8: noqa

from . import cartopy_utils, colorbar_utils, mpl_utils
from .cartopy_utils import *
from .colorbar_utils import *
from .mpl_utils import *

try:
    from importlib.metadata import version as _get_version
except ImportError:
    # importlib.metadata not available in python 3.7
    import pkg_resources

    _get_version = lambda pkg: pkg_resources.get_distribution(pkg).version

try:
    __version__ = _get_version("mplotutils")
except Exception:
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "999"
