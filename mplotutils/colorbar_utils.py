
def resize_colorbar_vert(cbax, ax1, ax2=None, size=0.04, pad=0.05,
                         shift='symmetric', shrink=None):
    """
    automatically resize colorbars on draw
    
    See below for Example
    
    Parameters
    ----------
    
    cbax : colorbar Axes
        Axes of the colorbar.
    ax1 : Axes
        Axes to adjust the colorbar to.
    ax2 : Axes, optional 
        If the colorbar should span more than one Axes. Default: None.
    size : float
        Width of the colorbar in Figure coordinates. Default: 0.04.
    pad : float
        Distance of the colorbar to the axes in Figure coordinates.
         Default: 0.05.
    shift : 'symmetric' or float in 0..1
        Fraction of the total height that the colorbar is shifted upwards.
        See Note. Default: 'symmetric'
    shrink : None or float in 0..1
        Fraction of the total height that the colorbar is shrunk.
        See Note. Default: None.
        
    Note
    ----   
    
    shift='symmetric', shrink=None  -> colorbar extends over the whole height
    shift='symmetric', shrink=0.1   -> colorbar is 10 % smaller, and centered
    shift=0., shrink=0.1            -> colorbar is 10 % smaller, and aligned
                                       with the bottom
    shift=0.1, shrink=None          -> colorbar is 10 % smaller, and aligned
                                       with the top   
    
    Exaples
    -------
    # example with 1 axes
    
    f = plt.figure()
    ax = plt.axes(projection=ccrs.PlateCarree())
    h = ax.pcolormesh([[0, 1]])
    
    ax.coastlines()

    cbax = f.add_axes([0, 0, 0.1, 0.1])
    cbar = plt.colorbar(h, orientation='vertical', cax=cbax)

    func = resize_colorbar_vert(cbax, ax)
    f.canvas.mpl_connect('draw_event', func)

    ax.set_global()

    plt.draw()
    
    
    # =========================
    # example with 2 axes
    
    f, axes = plt.subplots(2, 1, subplot_kw=dict(projection=ccrs.Robinson()))

    for ax in axes:
        ax.coastlines() 
        ax.set_global()
        h = ax.pcolormesh([[0, 1]])
    
    cbax = f.add_axes([0, 0, 0.1, 0.1])
    cbar = plt.colorbar(h, orientation='vertical', cax=cbax)
        
    func = resize_colorbar_vert(cbax, axes[0], axes[1], size=0.04, pad=.04,
                                shrink=None, shift=0.1)
    
    f.canvas.mpl_connect('draw_event', func)

    cbax.set_xlabel('[°C]', labelpad=10)

    plt.draw()
    
    # =========================
    # example with 3 axes & 2 colorbars
    
    f, axes = plt.subplots(3, 1, subplot_kw=dict(projection=ccrs.Robinson()))

    for ax in axes:
        ax.coastlines() 
        ax.set_global()

    h0 = ax.pcolormesh([[0, 1]])
    h1 = ax.pcolormesh([[0, 1]])
    h2 = ax.pcolormesh([[0, 1]], cmap='Blues')

    cbax = f.add_axes([0, 0, 0.1, 0.1])
    cbar = plt.colorbar(h1, orientation='vertical', cax=cbax)
    func = utils.resize_colorbar_vert(cbax, axes[0], axes[1])
    f.canvas.mpl_connect('draw_event', func)

    cbax = f.add_axes([0, 0, 0.1, 0.11])
    cbar = plt.colorbar(h2, orientation='vertical', cax=cbax)
    func = utils.resize_colorbar_vert(cbax, axes[2])
    f.canvas.mpl_connect('draw_event', func)

    plt.draw()
    
    
    See also
    --------
    resize_colorbar_horz
    """
    
    shift, shrink = _parse_shift_shrink(shift, shrink)

    # swap axes if ax1 is above ax2
    if ax2 is not None:
        posn = ax1.get_position()
        posn2 = ax2.get_position()

        ax1, ax2 = (ax1, ax2) if posn.y0 < posn2.y0 else (ax2, ax1)
    
    
    # inner function is called by event handler
    def inner(event=None): 
        
        posn = ax1.get_position()
        
        # determine total height of all axes
        if ax2 is not None:    
            posn2 = ax2.get_position()
            full_height = posn2.y0 - posn.y0 + posn2.height
        else:
            full_height = posn.height
        
        # calculate position
        left = posn.x0 + posn.width + pad
        bottom = posn.y0 + shift * full_height
        width = size
        height = full_height - shrink * full_height
        
        pos = [left, bottom, width, height]
        
        cbax.set_position(pos)
        
    return inner

# ====================================


def resize_colorbar_horz(cbax, ax1, ax2=None, size=0.05, pad=0.05,
                         shift='symmetric', shrink=None):
    """
    automatically resize colorbars on draw
    
    See below for Example
    
    Parameters
    ----------
    cbax : colorbar Axes
        Axes of the colorbar.
    ax1 : Axes
        Axes to adjust the colorbar to.
    ax2 : Axes, optional 
        If the colorbar should span more than one Axes. Default: None.
    size : float
        Height of the colorbar in Figure coordinates. Default: 0.04.
    pad : float
        Distance of the colorbar to the axes in Figure coordinates.
         Default: 0.1.
    shift : 'symmetric' or float in 0..1
        Fraction of the total width that the colorbar is shifted to the right.
        See Note. Default: 'symmetric'
    shrink : None or float in 0..1
        Fraction of the total width that the colorbar is shrunk.
        See Note. Default: None.
        
    Note
    ----   
    
    shift='symmetric', shrink=None -> colorbar extends over the whole width
    shift='symmetric', shrink=0.1  -> colorbar is 10 % smaller, and centered
    shift=0., shrink=0.1           -> colorbar is 10 % smaller, and aligned
                                      with the left hand side
    shift=0.1, shrink=None         -> colorbar is 10 % smaller, and aligned
                                      with the right hand side
    
    Exaples
    -------
    # example with 1 axes
    
    f = plt.figure()
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.coastlines()

    cbax = f.add_axes([0, 0, 0.1, 0.1])
    cbar = plt.colorbar(h, orientation='horizontal', cax=cbax)

    func = utils.resize_colorbar_horz(cbax, ax)
    f.canvas.mpl_connect('draw_event', func)

    ax.set_global()

    plt.draw()
    
    
    # =========================
    # example with 2 axes
    
    f, axes = plt.subplots(1, 2, subplot_kw=dict(projection=ccrs.Robinson()))

    for ax in axes:
        ax.coastlines() 
        ax.set_global()

        h = ax.pcolormesh([[0, 1]])

    cbax = f.add_axes([0, 0, 0.1, 0.1])
    cbar = plt.colorbar(h, orientation='horizontal', cax=cbax)

    func = resize_colorbar_horz(cbax, axes[0], axes[1], size=0.04, pad=.04, 
                                shrink=None, shift=0.1)

    f.canvas.mpl_connect('draw_event', func)

    cbax.set_ylabel('[°C]', labelpad=10, rotation=0, ha='right', va='center')

    plt.draw()
    
    # =========================
    # example with 3 axes & 2 colorbars
    
    f, axes = plt.subplots(1, 3, subplot_kw=dict(projection=ccrs.Robinson()))

    for ax in axes:
        ax.coastlines() 
        ax.set_global()

    h0 = ax.pcolormesh([[0, 1]])
    h1 = ax.pcolormesh([[0, 1]])
    h2 = ax.pcolormesh([[0, 1]], cmap='Blues')


    cbax = f.add_axes([0, 0, 0.1, 0.1])
    cbar = plt.colorbar(h1, orientation='horizontal', cax=cbax)
    func = utils.resize_colorbar_horz(cbax, axes[0], axes[1], size=0.04)
    f.canvas.mpl_connect('draw_event', func)

    cbax = f.add_axes([0, 0, 0.1, 0.11])
    cbar = plt.colorbar(h2, orientation='horizontal', cax=cbax)
    func = utils.resize_colorbar_horz(cbax, axes[2], size=0.04)
    f.canvas.mpl_connect('draw_event', func)

    plt.draw()
    
    
    See also
    --------
    resize_colorbar_vert
    """
        
    shift, shrink = _parse_shift_shrink(shift, shrink)
    
    if ax2 is not None:
        posn = ax1.get_position()
        posn2 = ax2.get_position()

        # swap axes if ax1 is right ax2
        ax1, ax2 = (ax1, ax2) if posn.x0 < posn2.x0 else (ax2, ax1)
    
    
    def inner(event=None): 
        
        posn = ax1.get_position()
        
        if ax2 is not None:
            posn2 = ax2.get_position()
            full_width = posn2.x0 - posn.x0 + posn2.width
        else:
            full_width = posn.width
        
        left = posn.x0 + shift * full_width
        bottom = posn.y0 - (pad + size)
        width = full_width - shrink * full_width
        height = size
        
        pos = [left, bottom, width, height]
        
        cbax.set_position(pos)
        
    return inner

# ====================================


def _parse_shift_shrink(shift, shrink):

    if shift == 'symmetric':
        if shrink is None:
            shrink = 0

        shift = shrink / 2.
    
    else:
        if shrink is None:
            shrink = shift
            
            
    assert (shift >= 0.) & (shift <= 1.), "'shift' must be in 0...1"
    assert (shrink >= 0.) & (shrink <= 1.), "'shrink' must be in 0...1"

    if shift > shrink:
        msg = ("Warning: 'shift' is larger than 'shrink', colorbar\n" 
               "will extend beyond the axes!")
        print(msg)
    
    return shift, shrink

# ==================================================================================================
