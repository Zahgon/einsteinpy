import warnings

import numpy as np
from scipy import integrate


class RK4naive:
    """
    Class for Defining Runge-Kutta 4th Order ODE solving method
    """

    def __init__(self, fun, t0, y0, t_bound, stepsize):
        """
        Initialization

        Parameters
        ----------
        fun : function
            Should accept t, y as parameters, and return same type as y
        t0 : float
            Initial t
        y0 : ~numpy.array or float
            Initial y
        t_bound : float
            Boundary time - the integration won't continue beyond it. It also determines the direction of the integration.
        stepsize : float
            Size of each increment in t

        """
        self.t = t0
        self.y = y0
        self.t_bound = t_bound
        self.step_size = stepsize
        self._fun = fun
        self.direction = 1 * (self.t_bound >= t0) - 1 * (not self.t_bound < t0)

    def step(self):
        """
        Updates the value of self.t and self.y
        """
        pass


class RK45(integrate.RK45):
    """
    This Class inherits ~scipy.integrate.RK45 Class
    """

    def __init__(self, fun, t0, y0, t_bound, stepsize, rtol=None, atol=None):
        """
        Initialization

        Parameters
        ----------
        fun : function
            Should accept t, y as parameters, and return same type as y
        t0 : float
            Initial t
        y0 : ~numpy.array or float
            Initial y
        t_bound : float
            Boundary time - the integration won't continue beyond it. It also determines the direction of the integration.
        stepsize : float
            Size of each increment in t
        rtol : float
            Relative tolerance, defaults to 0.2*stepsize
        atol : float
            Absolute tolerance, defaults to rtol/0.8e3

        """
        vectorized = not isinstance(y0, float)
        self._t_bound = t_bound
        if rtol is None:
            rtol = 0.2 * stepsize
        if atol is None:
            atol = rtol / 0.8e3
        super(RK45, self).__init__(
            fun=fun,
            t0=t0,
            y0=y0,
            t_bound=self._t_bound,
            first_step=0.8 * stepsize,
            max_step=8.0 * stepsize,
            rtol=rtol,
            atol=atol,
            vectorized=vectorized,
        )

    def step(self):
        """
        Updates the value of self.t and self.y
        """
        pass
