from mplotutils import ylabel_map, xlabel_map

import numpy as np
import matplotlib.pyplot as plt

# test it does not error...
def test_works():


	f, ax = plt.subplots()
	ylabel_map('ylabel', ax=ax)
	xlabel_map('ylabel', ax=ax)




