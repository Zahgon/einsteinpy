import numpy as np
from astropy import units as u

from einsteinpy import constant
from einsteinpy.metric import BaseMetric
from einsteinpy.utils import CoordinateError

_c = constant.c.value
_G = constant.G.value
_Cc = constant.coulombs_const.value


class KerrNewman(BaseMetric):
    """
    Class for defining Kerr-Newman Goemetry

    """

    @u.quantity_input(M=u.kg, a=u.one, Q=u.C, q=u.C / u.kg)
    def __init__(self, coords, M, a, Q, q=0.0 * u.C / u.kg):
        """
        Constructor

        Parameters
        ----------
        coords : ~einsteinpy.coordinates.differential.*
            Coordinate system, in which Metric is to be represented
        M : ~astropy.units.quantity.Quantity
            Mass of gravitating body, e.g. Black Hole
        a : ~astropy.units.quantity.Quantity
            Spin Parameter
        Q : ~astropy.units.quantity.Quantity
            Charge on gravitating body, e.g. Black Hole
        q : ~astropy.units.quantity.Quantity, optional
            Charge, per unit mass, of the test particle
            Defaults to ``0 C / kg``

        """
        super().__init__(
            coords=coords,
            M=M,
            a=a,
            Q=Q,
            name="Kerr-Newman Metric",
            metric_cov=self.metric_covariant,
            christoffels=self._christoffels,
            f_vec=self._f_vec,
        )
        self.q = q
        # Precomputed list of tuples, containing indices \
        # of non-zero Christoffel Symbols for Kerr-Newman Metric \
        # in Boyer-Lindquist Coordinates
        self._nonzero_christoffels_list_bl = [
            (0, 0, 1),
            (0, 0, 2),
            (0, 1, 3),
            (0, 2, 3),
            (0, 1, 0),
            (0, 2, 0),
            (0, 3, 1),
            (0, 3, 2),
            (1, 0, 0),
            (1, 1, 1),
            (1, 2, 2),
            (1, 3, 3),
            (2, 0, 0),
            (2, 1, 1),
            (2, 2, 2),
            (2, 3, 3),
            (1, 0, 3),
            (1, 1, 2),
            (2, 0, 3),
            (2, 1, 2),
            (1, 2, 1),
            (1, 3, 0),
            (2, 2, 1),
            (2, 3, 0),
            (3, 0, 1),
            (3, 0, 2),
            (3, 1, 0),
            (3, 1, 3),
            (3, 2, 0),
            (3, 2, 3),
            (3, 3, 1),
            (3, 3, 2),
        ]

    def metric_covariant(self, x_vec):
        """
        Returns Covariant Kerr-Newman Metric Tensor \
        in chosen Coordinates

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Covariant Kerr-Newman Metric Tensor in chosen Coordinates
            Numpy array of shape (4,4)

        Raises
        ------
        CoordinateError
            Raised, if the metric is not available in \
            the supplied Coordinate System

        """
        pass

    def _g_cov_bl(self, x_vec):
        """
        Returns Covariant Kerr-Newman Metric Tensor \
        in Boyer-Lindquist coordinates

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Covariant Kerr-Newman Metric Tensor \
            in Boyer-Lindquist coordinates
            Numpy array of shape (4,4)

        """
        pass

    def _dg_dx_bl(self, x_vec):
        """
        Returns derivative of each Kerr-Newman Metric component \
        w.r.t. coordinates in Boyer-Lindquist Coordinate System

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        dgdx : ~numpy.ndarray
            Array, containing derivative of each Kerr-Newman \
            Metric component w.r.t. coordinates \
            in Boyer-Lindquist Coordinate System
            Numpy array of shape (4,4,4)
            dgdx[0], dgdx[1], dgdx[2] & dgdx[3] contain \
            derivatives of metric w.r.t. t, r, theta & phi respectively

        """
        pass

    def _christoffels(self, x_vec):
        """
        Returns Christoffel Symbols for Kerr-Newman Metric in chosen Coordinates

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Christoffel Symbols for Kerr-Newman \
            Metric in chosen Coordinates
            Numpy array of shape (4,4,4)

        Raises
        ------
        CoordinateError
            Raised, if the Christoffel Symbols are not \
            available in the supplied Coordinate System

        """
        pass

    def _ch_sym_bl(self, x_vec):
        """
        Returns Christoffel Symbols for Kerr-Newman Metric \
        in Boyer-Lindquist Coordinates

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Christoffel Symbols for Kerr-Newman Metric \
            in Boyer-Lindquist Coordinates
            Numpy array of shape (4,4,4)

        """
        pass

    def _f_vec(self, lambda_, vec):
        """
        Returns f_vec for Kerr-Newman Metric in chosen coordinates
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
            f_vec for Kerr-Newman Metric in chosen coordinates
            Numpy array of shape (8)

        Raises
        ------
        CoordinateError
            Raised, if ``f_vec`` is not available in \
            the supplied Coordinate System

        """
        pass

    def _f_vec_bl(self, lambda_, vec):
        """
        Returns f_vec for Kerr-Newman Metric \
        in Boyer-Lindquist Coordinates
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
            f_vec for Kerr-Newman Metric in Boyer-Lindquist Coordinates
            Numpy array of shape (8)

        """
        pass

    def em_potential_covariant(self, x_vec):
        """
        Returns Covariant Electromagnetic 4-Potential
        Specific to Kerr-Newman Geometries

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Covariant Electromagnetic 4-Potential
            Numpy array of shape (4,)

        """
        pass

    def em_potential_contravariant(self, x_vec):
        """
        Returns Contravariant Electromagnetic 4-Potential
        Specific to Kerr-Newman Geometries

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Contravariant Electromagnetic 4-Potential
            Numpy array of shape (4,)

        """
        pass

    def em_tensor_covariant(self, x_vec):
        """
        Returns Covariant Electromagnetic Tensor
        Specific to Kerr-Newman Geometries

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Covariant Electromagnetic Tensor
            Numpy array of shape (4, 4)

        """
        pass

    def em_tensor_contravariant(self, x_vec):
        """
        Returns Contravariant Electromagnetic Tensor
        Specific to Kerr-Newman Geometries

        Parameters
        ----------
        x_vec : array_like
            Position 4-Vector

        Returns
        -------
        ~numpy.ndarray
            Contravariant Electromagnetic Tensor
            Numpy array of shape (4, 4)

        """
        pass
