import warnings

import numpy as np
from astropy import units as u
from scipy.integrate import fixed_quad
from scipy.interpolate import interp1d
from scipy.optimize import newton


class Shadow:
    """
    Class for plotting the shadow of Schwarzschild Black Hole surrounded by a
    thin accreting emission disk as seen by a distant observer.
    """

    @u.quantity_input(mass=u.kg, fov=u.km)
    def __init__(self, mass, n_rays, fov, limit=0.001):
        self.mass = mass.to(u.kg)
        self.limit = limit
        self.n_rays = n_rays
        self.fov = fov.to(u.km)
        self.horizon = 2 * self.mass.value  # To be changed after 0.3.0
        self.b_crit = 3 * np.sqrt(3) * self.mass
        self.b = self._compute_B()
        self.z = list()
        self.bfin = list()
        for i in self.b:
            root = newton(self._root_equation, 0.1, args=(i,))
            if np.isreal(root):
                self.bfin.append(i)
                self.z.append([i, np.real(root)])
        self.z = np.array(self.z)
        self.k0 = self._intensity()
        self.k1 = self._intensity_from_event_horizon()
        self.intensity = self.k1 + self.k0
        # Just to make the plot symmetric on -x axis
        self.fb1 = list(self.b2) + list(self.bfin)
        self.fb2 = np.asarray(list(-np.asarray(self.b2)) + list(-np.asarray(self.bfin)))

    def _compute_B(self):
        """
        Returns an array of impact parameters
        """
        pass

    def _root_equation(self, r_tp, i):
        """
        Returns the root of the equation for ``r_tp`` (turning points) for some impact parameter
        """
        pass

    def _intensity_blue_sch(self, r, b):
        """
        Returns the integrand for the blue shifted intensity to be integrated.
        Reference : Cosimo Bambi, 10.1103/PhysRevD.87.107501
        """
        pass

    def _intensity_red_sch(self, r, b):
        """
        Returns the integrand for the red shifted intensity to be integrated.
        Reference : Cosimo Bambi, 10.1103/PhysRevD.87.107501
        """
        pass

    def _intensity(self):
        """
        Returns an array of the integrated values using ~scipy.integrate.quadrature as the
        intensities for the blue shifted and red shifted rays above the critical impact paratmeter
        from the distance to the emitter
        """
        pass

    def _intensity_from_event_horizon(self):
        """
        Returns an array of the integrated values using ~scipy.integrate.quadrature as the
        intensities for the blue shifted and red shifted rays below the critical impact paratmeter
        from the event horizon to the distance given.
        """
        pass

    def smoothen(self, points=500):
        """
        Sets the interpolated values for the intensities for smoothening of the plot
        using ~scipy.interpolate.interp1d
        """
        pass
