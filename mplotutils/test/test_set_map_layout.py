import matplotlib.pyplot as plt
import numpy as np

from mplotutils import set_map_layout


def test_default_width():

    f, ax = plt.subplots()
    set_map_layout(ax)

    assert f.get_size_inches()[0] * 2.54 == 17.0


def test_no_borders():

    # width:height = 1:1
    f, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    f.subplots_adjust(left=0, bottom=0, right=1, top=1)
    set_map_layout(ax, 10)

    width, height = f.get_size_inches() * 2.54
    assert np.allclose((width, height), (10, 10))

    # width:height = 2:1
    f, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set(xlim=(0, 2), ylim=(0, 1))
    f.subplots_adjust(left=0, bottom=0, right=1, top=1)
    set_map_layout(ax, 10)

    width, height = f.get_size_inches() * 2.54
    assert np.allclose((width, height), (10, 5))

    # width:height = 1:2
    f, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set(xlim=(0, 1), ylim=(0, 2))
    f.subplots_adjust(left=0, bottom=0, right=1, top=1)
    set_map_layout(ax, 10)

    width, height = f.get_size_inches() * 2.54
    assert np.allclose((width, height), (10, 20))


def test_vert_borders():

    # width:height = 1:1
    f, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set(xlim=(0, 1), ylim=(0, 1))

    f.subplots_adjust(left=0, bottom=0.5, right=1, top=1)

    set_map_layout(ax, 10)

    width, height = f.get_size_inches() * 2.54
    assert np.allclose((width, height), (10, 20))

    # width:height = 1:1
    f, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set(xlim=(0, 1), ylim=(0, 1))

    f.subplots_adjust(left=0, bottom=0.0, right=1, top=0.8)

    set_map_layout(ax, 10)

    width, height = f.get_size_inches() * 2.54
    assert np.allclose((width, height), (10, 12.5))

    # width:height = 1:1
    f, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set(xlim=(0, 1), ylim=(0, 1))

    f.subplots_adjust(left=0, bottom=0.5, right=1, top=0.75)

    set_map_layout(ax, 10)

    width, height = f.get_size_inches() * 2.54
    assert np.allclose((width, height), (10, 40))


def test_horz_borders():

    # width:height = 1:1
    f, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set(xlim=(0, 1), ylim=(0, 1))

    f.subplots_adjust(left=0.5, bottom=0.0, right=1, top=1)

    set_map_layout(ax, 10)

    width, height = f.get_size_inches() * 2.54
    assert np.allclose((width, height), (10, 5))

    # width:height = 1:1
    f, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set(xlim=(0, 1), ylim=(0, 1))

    f.subplots_adjust(left=0.25, bottom=0.0, right=0.75, top=1)

    set_map_layout(ax, 10)

    width, height = f.get_size_inches() * 2.54
    assert np.allclose((width, height), (10, 5))
