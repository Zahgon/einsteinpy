import numpy as np
from matplotlib import pyplot as plt


class ShadowPlotter:
    """
    Class for plotting and visualising shadows
    """

    def __init__(self, shadow, is_line_plot=True):
        """
        Constructor for plotter.

        Parameters
        ----------
        shadow : ~einsteinpy.rays.Shadow
            The shadow object
        is_line_plot : bool, optional
            If the plot is a line plot or a contour plot. Defaults to True.
        """
        self.shadow = shadow
        self.is_intensity_plot = is_line_plot

    def plot(self):
        """
        Plots the shadow.
        """
        pass

    def show(self):
        """
        Shows the plot.
        """
        if self.is_intensity_plot:
            plt.show()
        else:
            xx = self.r1 * np.cos(self.theta1)
            yy = self.r1 * np.sin(self.theta1)
            plt.figure(figsize=(7, 7))
            plt.pcolormesh(xx, yy, self.values1, cmap=plt.cm.afmhot, shading="gouraud")
            plt.title("Schwarzschild Black Hole")
            plt.gca().set_aspect("equal", adjustable="box")
