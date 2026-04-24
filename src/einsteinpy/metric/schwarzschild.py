import numpy as np
from astropy import units as u

from einsteinpy import constant
from einsteinpy.metric import BaseMetric
from einsteinpy.utils import CoordinateError

_c = constant.c.value


class Schwarzschild(BaseMetric):
    """
    Class for defining Schwarzschild Geometry

    """

    @u.quantity_input(M=u.kg)
    def __init__(self, coords, M):
        """
        Constructor

        Parameters
        ----------
        coords : ~einsteinpy.coordinates.differential.*
            Coordinate system, in which Metric is to be represented
        M : ~astropy.units.quantity.Quantity
            Mass of gravitating body, e.g. Black Hole

        """
        super().__init__(
            coords=coords,
            M=M,
            name="Schwarzschild Metric",
            metric_cov=self.metric_covariant,
            christoffels=self._christoffels,
            f_vec=self._f_vec,
        )

    def metric_covariant(self, x_vec):
        """
        Returns Covariant Schwarzschild Metric Tensor \
        in chosen Coordinates

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Covariant Schwarzschild Metric Tensor in chosen Coordinates
            Numpy array of shape (4,4)

        """
        pass

    def _g_cov_s(self, x_vec):
        """
        Returns Covariant Schwarzschild Metric Tensor \
        in Schwarschild Coordinates

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Covariant Schwarzschild Metric Tensor
            Numpy array of shape (4,4)

        """
        pass

    def _christoffels(self, x_vec):
        """
        Returns Christoffel Symbols for Schwarzschild Metric in chosen Coordinates

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Christoffel Symbols for Schwarzschild Metric \
            in chosen Coordinates
            Numpy array of shape (4,4,4)

        Raises
        ------
        CoordinateError
            Raised, if the Christoffel Symbols are not \
            available in the supplied Coordinate System

        """
        pass

    def _ch_sym_s(self, x_vec):
        """
        Returns the Christoffel Symbols for Schwarzschild Metric
        in Schwarzschild Coordinates

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Christoffel Symbols for Schwarzschild Metric \
            in Schwarzschild Coordinates
            Numpy array of shape (4,4,4)

        """
        pass

    def _f_vec(self, lambda_, vec):
        """
        Returns f_vec for Schwarzschild Metric in chosen coordinates
        To be used for solving Geodesics ODE

        Parameters
        ----------
        lambda_ : float
            Parameterizes current integration step
            Used by ODE Solver

        vec : array_like
            Length-8 Vector, containing 4-Position & 4-Velocity

        Returns
        -------
        ~numpy.ndarray
            f_vec for Schwarzschild Metric in chosen coordinates
            Numpy array of shape (8)

        Raises
        ------
        CoordinateError
            Raised, if ``f_vec`` is not available in \
            the supplied Coordinate System

        """
        pass

    def _f_vec_s(self, lambda_, vec):
        """
        Returns f_vec for Schwarzschild Metric
        To be used for solving Geodesics ODE

        Parameters
        ----------
        lambda_ : float
            Parameterizes current integration step
            Used by ODE Solver

        vec : array_like
            Length-8 Vector, containing 4-Position & 4-Velocity

        Returns
        -------
        ~numpy.ndarray
            f_vec for Schwarzschild Metric
            Numpy array of shape (8)

        """
        pass
