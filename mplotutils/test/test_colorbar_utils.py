
from pytest import raises

from mplotutils.colorbar_utils import (resize_colorbar_vert,
                                       resize_colorbar_horz,
                                       _parse_shift_shrink)

import matplotlib.pyplot as plt
import numpy as np


def test_parse_shift_shrink():

    # test code for _parse_shift_shrink
    assert _parse_shift_shrink('symmetric', None) == (0., 0.)

    assert _parse_shift_shrink('symmetric', 1) == (0.5, 1)
    
    assert _parse_shift_shrink(1, None) == (1, 1)
    
    assert _parse_shift_shrink(1, 1) == (1, 1)

    assert _parse_shift_shrink(0.5, 0.5) == (0.5, 0.5)

    with raises(AssertionError):
        _parse_shift_shrink(-0.1, 0)

    with raises(AssertionError):
        _parse_shift_shrink(1.1, 0)

    with raises(AssertionError):
        _parse_shift_shrink(0, -0.1)

    with raises(AssertionError):
        _parse_shift_shrink(0, 1.1)


def _easy_cbar_vert(**kwargs):

    f, ax = plt.subplots()
    
    f.subplots_adjust(left=0, bottom=0, right=0.8, top=1)

    # simplest 'mappable'
    h = ax.pcolormesh([[0, 1]])
    
    # create colorbar
    cbax = f.add_axes([0, 0, 0.1, 0.1])

    cbar = plt.colorbar(h, orientation='vertical', cax=cbax)

    func = resize_colorbar_vert(cbax, ax, **kwargs)
    f.canvas.mpl_connect('draw_event', func)

    f.canvas.draw()

    return f, cbar


def test_resize_colorbar_vert():


    # test pad=0, size=0.2
    f, cbar = _easy_cbar_vert(size=0.2, pad=0)
    
    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.8, 0, 0.2, 1.]

    np.testing.assert_allclose(res, exp)

    # -----------------------------------------------------------

    f.subplots_adjust(left=0, bottom=0.1, right=0.8, top=0.9)
    f.canvas.draw()

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.8, 0.1, 0.2, 0.8]

    np.testing.assert_allclose(res, exp)
    
    # ===========================================================

    # pad=0.05, size=0.1

    f, cbar = _easy_cbar_vert(size=0.1, pad=0.05)

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.85, 0, 0.1, 1.]

    np.testing.assert_allclose(res, exp)

    # ===========================================================

    # shift='symmetric', shrink=0.1 
    # --> colorbar is 10 % smaller, and centered

    f, cbar = _easy_cbar_vert(size=0.2, pad=0., shrink=0.1)

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.8, 0.05, 0.2, 0.9]

    np.testing.assert_allclose(res, exp)

    # ===========================================================

    # shift=0., shrink=0.1
    # --> colorbar is 10 % smaller, and aligned with the bottom

    f, cbar = _easy_cbar_vert(size=0.2, pad=0., shrink=0.1, shift=0.)

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.8, 0.0, 0.2, 0.9]

    np.testing.assert_allclose(res, exp)

    # ===========================================================
    
    # shift=0.1, shrink=None
    # --> colorbar is 10 % smaller, and aligned with the top

    f, cbar = _easy_cbar_vert(size=0.2, pad=0., shrink=None, shift=0.1)

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.8, 0.1, 0.2, 0.9]

    np.testing.assert_allclose(res, exp)

# =============================================================================
# =============================================================================

def _easy_cbar_horz(**kwargs):

    f, ax = plt.subplots()
    
    f.subplots_adjust(left=0, bottom=0.2, right=1, top=1)

    # simplest 'mappable'
    h = ax.pcolormesh([[0, 1]])
    
    # create colorbar
    cbax = f.add_axes([0, 0, 0.1, 0.1])

    cbar = plt.colorbar(h, orientation='horizontal', cax=cbax)

    func = resize_colorbar_horz(cbax, ax, **kwargs)
    f.canvas.mpl_connect('draw_event', func)

    f.canvas.draw()

    return f, cbar


def test_resize_colorbar_horz():


    # test pad=0, size=0.2
    f, cbar = _easy_cbar_horz(size=0.2, pad=0)
    
    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0, 0, 1, 0.2]

    # adding atol because else 5e-17 != 0
    np.testing.assert_allclose(res, exp, atol=1e-08)

    # -----------------------------------------------------------

    f.subplots_adjust(left=0.1, bottom=0.2, right=0.9, top=1)
    f.canvas.draw()

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.1, 0, 0.8, 0.2]

    np.testing.assert_allclose(res, exp, atol=1e-08)
    
    # ===========================================================

    # pad=0.05, size=0.1

    f, cbar = _easy_cbar_horz(size=0.1, pad=0.05)

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.0, 0.05, 1, 0.1]

    np.testing.assert_allclose(res, exp, atol=1e-08)

    # ===========================================================

    # shift='symmetric', shrink=0.1 
    # --> colorbar is 10 % smaller, and centered

    f, cbar = _easy_cbar_horz(size=0.2, pad=0., shrink=0.1)

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.05, 0, 0.9, 0.2]

    np.testing.assert_allclose(res, exp, atol=1e-08)

    # ===========================================================

    # shift=0., shrink=0.1
    # --> colorbar is 10 % smaller, and aligned with lhs

    f, cbar = _easy_cbar_horz(size=0.2, pad=0., shrink=0.1, shift=0.)

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.0, 0, 0.9, 0.2]

    np.testing.assert_allclose(res, exp, atol=1e-08)

    # ===========================================================
    
    # shift=0.1, shrink=None
    # --> colorbar is 10 % smaller, and aligned with rhs

    f, cbar = _easy_cbar_horz(size=0.2, pad=0., shrink=None, shift=0.1)

    pos = cbar.ax.get_position()
    res = [pos.x0, pos.y0, pos.width, pos.height]
    exp = [0.1, 0, 0.9, 0.2]

    np.testing.assert_allclose(res, exp, atol=1e-08)