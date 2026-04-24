import warnings

import numpy as np
from astropy import units as u
from matplotlib import pyplot as plt


class SchwarzschildEmbedding:
    """
    Class for Utility functions for Schwarzschild Embedding surface to
    implement gravitational lensing

    Attributes
    ----------
    input_units : list
        list of input units of M
    units_list : list
        customized units to handle values of M and render plots
        within grid range
    r_init : ~astropy.units.m

    """

    def __init__(self, M):
        """
        Constructor
        Initialize mass and embedding initial radial coordinate in appropiate units
        in order to render the plots of the surface in finite grid. The initial r
        is taken to be just greater than schwarzschild radius but it is important
        to note that the embedding breaks at r < 9m/4.

        Parameters
        ----------
        M : ~astropy.units.kg
            Mass of the body

        """
        self.input_units = [M.unit]
        self.units_list = [u.kg * 10e22, u.m / M.to(u.kg * 10e22).value]
        M = M.to(self.units_list[0])
        self.M = M
        self.r_init = (((3 * self.M.value + 0.0001) / self.M.value) * u.m).to(
            self.units_list[1]
        )

    def gradient(self, r):
        """
        Calculate gradient of Z coordinate w.r.t r to update the value of r and
        thereby get value of spherical radial coordinate R.

        Parameters
        ----------
        r : float
            schwarzschild coordinate at which gradient is supposed to be obtained

        Returns
        -------
        float
            gradient of Z w.r.t r at the point r (passed as argument)

        """
        pass

    def radial_coord(self, r):
        """
        Returns spherical radial coordinate (of the embedding) from given schwarzschild
        coordinate.

        Parameters
        ----------
        r : float

        Returns
        -------
        float
            spherical radial coordinate of the 3d embedding

        """
        pass

    def get_values(self, alpha):
        """
        Obtain the Z coordinate values and corrosponding R values for range of
        r as 9m/4 < r < 9m.

        Parameters
        ----------
        alpha : float
            scaling factor to obtain the step size for incrementing r

        Returns
        -------
        tuple
            (list, list) : values of R (x_axis) and Z (y_axis)

        """
        pass

    def get_values_surface(self, alpha):
        """
        Obtain the same values as of the get_values function but reshapes them to obtain
        values for all points on the solid of revolution about Z axis (as the
        embedding is symmetric in angular coordinates).

        Parameters
        ----------
        alpha : float
            scaling factor to obtain the step size for incrementing r

        Returns
        -------
        tuple
            (~numpy.array of X, ~numpy.array of Y, ~numpy.array of Z) values in cartesian coordinates
            obtained after applying solid of revolution

        """
        pass
