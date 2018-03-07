import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib.colors import from_levels_and_colors

# =============================================================================


def from_levels_and_cmap(levels, cmap, extend='neither'):
    """
    
    Parameters
    ----------
    levels : sequence of numbers
        The quantization levels used to construct the :class:`BoundaryNorm`.
        Values ``v`` are quantizized to level ``i`` if
        ``lev[i] <= v < lev[i+1]``.
    cmap : string
        Valid colormap identifier.
    extend : {'neither', 'min', 'max', 'both'}, optional
        The behaviour when a value falls out of range of the given levels.
        See :func:`~matplotlib.pyplot.contourf` for details.

    ..note::
      Adapted from xarray.

    """
    
    if extend == 'both':
        ext_n = 2
    elif extend in ['min', 'max']:
        ext_n = 1
    else:
        ext_n = 0

    # subtract 1 because there is one less level than numbers
    pal = sns.color_palette(cmap, n_colors=len(levels) + ext_n - 1)
    cmap, norm = from_levels_and_colors(levels, pal, extend=extend)
    
    return cmap, norm


# =============================================================================


def set_map_layout(axes, width=17.0):
    """
    set figure height, given width

    Needs to be called after all plotting is done.
       
    Parameters
    ----------
    axes : ndarray of (Geo)Axes
        Array with all axes of the figure.
    width : float
        Width of the full figure in cm. Default 17

    ..note: currently only works if all the axes have the same aspect
    ratio.
    """

    if isinstance(axes, plt.Axes):
        ax = axes
    else:
        # assumes the first of the axes is representative for all
        ax = axes.flat[0]
    
    # read figure data
    f = ax.get_figure()

    bottom = f.subplotpars.bottom
    top = f.subplotpars.top
    left = f.subplotpars.left
    right = f.subplotpars.right
    hspace = f.subplotpars.hspace
    wspace = f.subplotpars.wspace

    # data ratio is the aspect
    aspect = ax.get_data_ratio()
    # get geometry tells how many subplots there are
    nrow, ncol, __ = ax.get_geometry()


    # width of one plot, taking into account
    # left * wf, (1-right) * wf, ncol * wp, (1-ncol) * wp * wspace
    wp = (width - width * (left + (1-right))) / (ncol + (ncol-1) * wspace) 

    # height of one plot
    hp = wp * aspect

    # height of figure
    height = (hp * (nrow + ((nrow - 1) * hspace))) / (1. - (bottom + (1 - top)))


    f.set_figwidth(width / 2.54)
    f.set_figheight(height / 2.54)

# =============================================================================


def _get_label_attr(labelpad, size, weight):

    if labelpad is None:
        labelpad = mpl.rcParams['axes.labelpad']

    if size is None:
        size = mpl.rcParams['axes.labelsize']

    if weight is None:
        weight = mpl.rcParams['axes.labelweight']
    
    return labelpad, size, weight

