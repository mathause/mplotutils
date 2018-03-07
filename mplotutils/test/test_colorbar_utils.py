
from pytest import raises

from mplotutils import (resize_colorbar_vert,
                        resize_colorbar_horz,
                        _parse_shift_shrink)




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
