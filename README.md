# mplotutils

> *helper functions for cartopy and matplotlib*

This package solves two main problems for plots with maps created with cartopy. Because these plots have a fixed aspect ratio (1) colorbars will extend beyond the visible axes and (2) the distance between individual subplots will seemingly be random.


Without mplotutils         |  With mplotutils
:-------------------------:|:-------------------------:
<img src="docs/example_no_mpu.png" alt="Without mplotutils" width="250"/> | <img src="docs/example_mpu.png" alt="With mplotutils" width="250"/>

The code to create the examples can be found in [docs/example.py](docs/example.py).

## Installation

See [docs/installation.md](docs/installation.md).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## History

This package bases on functions developped for the [python visualisation workshop at C2SM](https://github.com/C2SM/pyvis/).
