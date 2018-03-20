# mplotutils

helper functions for cartopy and matplotlib


## Versions

### 0.2.0 (unreleased)

 * add `_color_palette` that selects colors from the whole range of the colormap. Previously we used the `seaborn` logic that excludes colors at the edge of the colorbar (closes GH:#1).
 * the colorbar functionality was entirely redesigned:
   * new top-level function `mpu.colorbar`
   * added `aspect` keyword which defines the ratio of long to short side
   * the default width/ height is now `aspect=20` (was `size=0.04`)
   * `pad` and `size` are now scaled by the width/ height of the axes (was width/ height of the figure)
   * `pad` now uses the matplotlib default (0.05 for vertical bars and 0.15 for horizontal colorbars)
 * add `_is_monotonic` to `infer_interval_breaks`

### 0.1.0 (13.03.2018)

 * Functionality as developped for [pyvis](https://github.com/C2SM/pyvis/) (see below), packed into a module.


## History

This package bases on functions developped for the [python visualisation workshop at C2SM](https://github.com/C2SM/pyvis/) (Part 3 -> `utils.py`).
`utils.py` in turn is based on [mutils](https://github.com/mathause/mutils). 

