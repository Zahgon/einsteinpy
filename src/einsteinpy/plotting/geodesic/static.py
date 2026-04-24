import random
import warnings

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d


class StaticGeodesicPlotter:
    def __init__(self, ax=None, bh_colors=("#000", "#FFC"), draw_ergosphere=True):
        """
        Constructor

        Parameters
        ----------
        ax: ~matplotlib.axes.Axes
            Matplotlib Axes object
            To be deprecated in Version 0.5.0
            Since Version 0.4.0, `StaticGeodesicPlotter`
            automatically creates a new Axes Object.
            Defaults to ``None``
        bh_colors : tuple, optional
            2-Tuple, containing hexcodes (Strings) for the colors,
            used for the Black Hole Event Horizon (Outer) and Ergosphere (Outer)
            Defaults to ``("#000", "#FFC")``
        draw_ergosphere : bool, optional
            Whether to draw the ergosphere
            Defaults to `True`

        """
        self.ax = ax
        self.bh_colors = bh_colors
        self.draw_ergosphere = draw_ergosphere

        if ax is not None:
            warnings.warn(
                """
                Argument `ax` will be removed in Version 0.5.0.
                Since Version 0.4.0, `StaticGeodesicPlotter` automatically
                creates a new Axes Object.
                """,
                PendingDeprecationWarning,
            )

    def _draw_bh(self, a, figsize=(6, 6)):
        """
        Plots the Black Hole in 3D

        Parameters
        ----------
        a : float
            Dimensionless Spin Parameter of the Black Hole
            ``0 <= a <= 1``
        figsize : tuple, optional
            2-Tuple of Figure Size in inches
            Defaults to ``(6, 6)``

        """
        pass

    def _draw_bh_2D(self, a, figsize=(6, 6)):
        """
        Plots the Black Hole in 2D

        Parameters
        ----------
        a : float
            Dimensionless Spin Parameter of the Black Hole
            ``0 <= a <= 1``
        figsize : tuple, optional
            2-Tuple of Figure Size in inches
            Defaults to ``(6, 6)``

        """
        pass

    def plot(
        self,
        geodesic,
        figsize=(6, 6),
        color="#{:06x}".format(random.randint(0, 0xFFFFFF)),
        title: str = "",
        aspect: str = "auto",
    ):
        """
        Plots the Geodesic

        Parameters
        ----------
        geodesic : einsteinpy.geodesic.*
            Geodesic Object
        figsize : tuple, optional
            2-Tuple of Figure Size in inches
            Defaults to ``(6, 6)``
        color : str, optional
            Hexcode (String) for the color of the
            dashed lines, that represent the Geodesic
            Picks a random color by default
        title : str, optional
            Plot title
        aspect : {"auto", "equal", "equalxy", "equalyz", "equalxz"}
            Aspect ratio for plot axes
            Defaults to "auto"

        Raises
        ------
        ValueError
            If ``aspect`` does not take values from ``{"auto", "equal", "equalxy", "equalyz", "equalxz"}``

        """
        pass

    def plot2D(
        self,
        geodesic,
        coordinates=(1, 2),
        figsize=(6, 6),
        color="#{:06x}".format(random.randint(0, 0xFFFFFF)),
        title: str = "",
    ):
        """
        Plots the Geodesic in 2D

        Parameters
        ----------
        geodesic : einsteinpy.geodesic.*
            Geodesic Object
        coordinates : tuple, optional
            2-Tuple, containing labels for coordinates to plot
            Labels for ``X1, X2, X3`` are ``(1, 2, 3)``
            Defaults to ``(1, 2)`` (X, Y)
        figsize : tuple, optional
            2-Tuple of Figure Size in inches
            Defaults to ``(6, 6)``
        color : str, optional
            Hexcode (String) for the color of the
            dashed lines, that represent the Geodesic
            Picks a random color by default
        title: str, optional
            Plot title

        Raises
        ------
        IndexError
            If indices in ``coordinates`` do not take values from ``(1, 2, 3)``

        """
        pass

    def parametric_plot(
        self,
        geodesic,
        figsize=(8, 6),
        colors=("#00FFFF", "#FF00FF", "#FFFF00"),
        title: str = "",
    ):
        """
        Plots the coordinates of the Geodesic, against Affine Parameter

        Parameters
        ----------
        geodesic : einsteinpy.geodesic.*
            Geodesic Object
        figsize : tuple, optional
            2-Tuple of Figure Size in inches
            Defaults to ``(8, 6)``
        colors : tuple, optional
            3-Tuple, containing hexcodes (Strings) for the color
            of the lines, for each of the 3 coordinates
            Defaults to ``("#00FFFF", "#FF00FF", "#00FFFF")``
        title : str, optional
            Plot title

        """
        pass

    def animate(
        self, geodesic, interval=10, color="#{:06x}".format(random.randint(0, 0xFFFFFF))
    ):
        """
        Parameters
        ----------
        geodesic : einsteinpy.geodesic.*
            Geodesic Object
        interval : int, optional
            Time (in milliseconds) between frames
            Defaults to ``10``
        color : str, optional
            Hexcode (String) for the color of the
            dashed lines, that represent the Geodesic
            Picks a random color by default

        """
        pass

    def show(self, azim=-60, elev=30):
        """
        Adjusts the 3D view of the plot and \
        shows the plot during runtime. For Parametric Plots,
        only the plot is displayed.

        Parameters
        ----------
        azim : float, optional
            Azimuthal viewing angle
            Defaults to ``-60`` Degrees

        elev : float, optional
            Elevation viewing angle
            Defaults to ``30`` Degrees

        """
        figsize = self.fig.get_size_inches()
        fontsize = max(figsize) + 1.5
        if self.ax.name == "3d":
            self.ax.view_init(azim=azim, elev=elev)
        plt.legend(prop={"size": fontsize})

        plt.show()

    def clear(self):
        """
        Clears plot during runtime

        """
        pass

    def save(self, name="Geodesic.png"):
        """
        Saves plot locally
        Should be called before ``show()``, as
        ``show()`` erases current figure's contents.

        Parameters
        ----------
        name : str, optional
            Name of the file, with extension
            Defaults to ``Geodesic.png``

        """
        pass
