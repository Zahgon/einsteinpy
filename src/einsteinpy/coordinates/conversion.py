from einsteinpy.coordinates.utils import (
    bl_to_cartesian_fast,
    cartesian_to_bl_fast,
    cartesian_to_spherical_fast,
    spherical_to_cartesian_fast,
)
from einsteinpy.metric import BaseMetric


class CartesianConversion:
    """
    Class for conversion to and from Cartesian Coordinates in SI units

    """

    def __init__(self, t, x, y, z, v_x=None, v_y=None, v_z=None):
        """
        Constructor

        Parameters
        ----------
        t : float
            Time
        x : float
            x-Component of 3-Position
        y : float
            y-Component of 3-Position
        z : float
            z-Component of 3-Position
        v_x : float, optional
            x-Component of 3-Velocity
        v_y : float, optional
            y-Component of 3-Velocity
        v_z : float, optional
            z-Component of 3-Velocity

        """
        self.t_si = t
        self.x_si = x
        self.y_si = y
        self.z_si = z
        self.v_x_si = v_x
        self.v_y_si = v_y
        self.v_z_si = v_z
        self._velocities_provided = not (
            (v_x is None) or (v_y is None) or (v_z is None)
        )

    def values(self):
        """
        Returns components of the coordinates in SI units

        Returns
        -------
        tuple
            4-Tuple, containing ``t, x, y, z`` in SI units
            or 7-tuple, containing ``t, x, y, z, v_x, v_y, v_z`` \
            in SI units

        """
        pass

    def convert_spherical(self, **kwargs):
        """
        Converts to Spherical Polar Coordinates

        Other Parameters
        ----------------
        **kwargs : dict
            Keyword Arguments

        Returns
        -------
        tuple
            4-Tuple or 7-Tuple, containing the components in \
            Spherical Polar Coordinates

        """
        pass

    def convert_bl(self, **kwargs):
        """
        Converts to Boyer-Lindquist Coordinates

        Parameters
        ----------
        **kwargs : dict
            Keyword Arguments
            Expects two arguments, ``M and ``a``, as described below

        Other Parameters
        ----------------
        M : float
            Mass of the gravitating body, \
            around which, spacetime has been defined
        a : float
            Spin Parameter of the gravitating body, \
            around which, spacetime has been defined

        Returns
        -------
        tuple
            4-Tuple or 7-Tuple, containing the components in \
            Boyer-Lindquist Coordinates

        Raises
        ------
        KeyError
            If ``kwargs`` does not contain both ``M`` \
            and ``a`` as keyword arguments

        """
        pass


class SphericalConversion:
    """
    Class for conversion to and from Spherical Polar Coordinates in SI units

    """

    def __init__(self, t, r, theta, phi, v_r=None, v_th=None, v_p=None):
        """
        Constructor

        Parameters
        ----------
        t : float
            Time
        r : float
            r-Component of 3-Position
        theta : float
            theta-Component of 3-Position
        phi : float
            phi-Component of 3-Position
        v_r : float, optional
            r-Component of 3-Velocity
        v_th : float, optional
            theta-Component of 3-Velocity
        v_p : float, optional
            phi-Component of 3-Velocity

        """
        self.t_si = t
        self.r_si = r
        self.th_si = theta
        self.p_si = phi
        self.v_r_si = v_r
        self.v_th_si = v_th
        self.v_p_si = v_p
        self._velocities_provided = not (
            (v_r is None) or (v_th is None) or (v_p is None)
        )

    def values(self):
        """
        Returns components of the coordinates

        Returns
        -------
        tuple
            4-Tuple containing ``t, r, theta, phi`` in SI units
            or 7-tuple, containing ``t, r, theta, phi, v_r, v_th, v_p`` \
            in SI units

        """
        pass

    def convert_cartesian(self, **kwargs):
        """
        Converts to Cartesian Coordinates

        Other Parameters
        ----------------
        **kwargs : dict
            Keyword Arguments

        Returns
        -------
        tuple
            4-Tuple or 7-Tuple, containing the components in \
            Cartesian Coordinates

        """
        pass

    def convert_bl(self, **kwargs):
        """
        Converts to Boyer-Lindquist Coordinates

        Parameters
        ----------
        **kwargs : dict
            Keyword Arguments
            Expects two arguments, ``M and ``a``, as described below

        Other Parameters
        ----------------
        M : float
            Mass of the gravitating body, \
            around which, spacetime has been defined
        a : float
            Spin Parameter of the gravitating body, \
            around which, spacetime has been defined

        Returns
        -------
        tuple
            4-Tuple or 7-Tuple, containing the components in \
            Boyer-Lindquist Coordinates

        Raises
        ------
        KeyError
            If ``kwargs`` does not contain both ``M`` \
            and ``a`` as keyword arguments

        """
        pass


class BoyerLindquistConversion:
    """
    Class for conversion to and from Boyer-Lindquist Coordinates in SI units

    """

    def __init__(self, t, r, theta, phi, v_r=None, v_th=None, v_p=None):
        """
        Constructor

        Parameters
        ----------
        t : float
            Time
        r : float
            r-Component of 3-Position
        theta : float
            theta-Component of 3-Position
        phi : float
            phi-Component of 3-Position
        v_r : float, optional
            r-Component of 3-Velocity
        v_th : float, optional
            theta-Component of 3-Velocity
        v_p : float, optional
            phi-Component of 3-Velocity

        """
        self.t_si = t
        self.r_si = r
        self.th_si = theta
        self.p_si = phi
        self.v_r_si = v_r
        self.v_th_si = v_th
        self.v_p_si = v_p
        self._velocities_provided = not (
            (v_r is None) or (v_th is None) or (v_p is None)
        )

    def values(self):
        """
        Returns components of the coordinates

        Returns
        -------
        tuple
            4-Tuple containing ``t, r, theta, phi`` in SI units
            or 7-tuple, containing ``t, r, theta, phi, v_r, v_th, v_p`` \
            in SI units

        """
        pass

    def convert_cartesian(self, **kwargs):
        """
        Converts to Cartesian Coordinates

        Parameters
        ----------
        **kwargs : dict
            Keyword Arguments
            Expects two arguments, ``M and ``a``, as described below

        Other Parameters
        ----------------
        M : float
            Mass of the gravitating body, \
            around which, spacetime has been defined
        a : float
            Spin Parameter of the gravitating body, \
            around which, spacetime has been defined

        Returns
        -------
        tuple
            4-Tuple or 7-Tuple, containing the components in \
            Cartesian Coordinates

        Raises
        ------
        KeyError
            If ``kwargs`` does not contain both ``M`` \
            and ``a`` as keyword arguments

        """
        pass

    def convert_spherical(self, **kwargs):
        """
        Converts to Spherical Polar Coordinates

        Parameters
        ----------
        **kwargs : dict
            Keyword Arguments
            Expects two arguments, ``M and ``a``, as described below

        Other Parameters
        ----------------
        M : float
            Mass of the gravitating body, \
            around which, spacetime has been defined
        a : float
            Spin Parameter of the gravitating body, \
            around which, spacetime has been defined

        Returns
        -------
        tuple
            4-Tuple or 7-Tuple, containing the components in \
            Spherical Polar Coordinates

        Raises
        ------
        KeyError
            If ``kwargs`` does not contain both ``M`` \
            and ``a`` as keyword arguments

        """
        pass
