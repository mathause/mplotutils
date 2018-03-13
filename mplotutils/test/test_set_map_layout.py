from mplotutils import set_map_layout

import numpy as np
import matplotlib.pyplot as plt




def test_default_width():

    f, ax = plt.subplots()
    set_map_layout(ax)
    
    assert f.get_size_inches()[0] * 2.54 == 17.


def test_no_borders():

    # width:height = 1:1
    f, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set(xlim=(0, 1), ylim=(0, 1))
    f.subplots_adjust(left=0, bottom=0, right=1, top=1)
    set_map_layout(ax, 10)
    
    assert np.allclose(f.get_size_inches() * 2.54, (10, 10))


    # width:height = 2:1
    f, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set(xlim=(0, 2), ylim=(0, 1))
    f.subplots_adjust(left=0, bottom=0, right=1, top=1)
    set_map_layout(ax, 10)
    
    assert np.allclose(f.get_size_inches() * 2.54, (10, 5))

    # width:height = 1:2
    f, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set(xlim=(0, 1), ylim=(0, 2))
    f.subplots_adjust(left=0, bottom=0, right=1, top=1)
    set_map_layout(ax, 10)
    
    assert np.allclose(f.get_size_inches() * 2.54, (10, 20))