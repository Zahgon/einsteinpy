import random

from einsteinpy.plotting.geodesic.interactive import InteractiveGeodesicPlotter
from einsteinpy.plotting.geodesic.static import StaticGeodesicPlotter


def in_ipynb():
    pass


class GeodesicPlotter(in_ipynb()):  # type: ignore
    """
    Class for automatically switching between Matplotlib and Plotly depending on platform used.
    """
