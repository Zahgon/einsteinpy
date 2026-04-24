import os
import random

import numpy as np
from plotly import graph_objects as go
from plotly.offline import plot as saveplot


class InteractiveGeodesicPlotter:
    def __init__(self, bh_colors=("#000", "#FFC"), draw_ergosphere=True):
        """
        Constructor

        Parameters
        ----------
        bh_colors : tuple, optional
            2-Tuple, containing hexcodes (Strings) for the colors,
            used for the Black Hole Event Horizon (Outer) and Ergosphere (Outer)
            Defaults to ``("#000", "#FFC")``
        draw_ergosphere : bool, optional
            Whether to draw the ergosphere
            Defaults to ``True``

        """
        self.fig = go.Figure()
        self.bh_colors = bh_colors
        self.draw_ergosphere = draw_ergosphere

    def _draw_bh(self, a):
        """
        Plots the Black Hole

        Parameters
        ----------
        a : float
            Dimensionless Spin Parameter of the Black Hole
            ``0 <= a <= 1``

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
        color="#{:06x}".format(random.randint(0, 0xFFFFFF)),
        title: str = "Geodesic Plot",
        aspect: str = "auto",
        aspect_ratio: dict = dict(x=1, y=1, z=1),
    ):
        """
        Plots the Geodesic

        Parameters
        ----------
        geodesic : einsteinpy.geodesic.*
            Geodesic Object
        color : str, optional
            Hexcode (String) for the color of the
            dashed lines, that represent the Geodesic
            Picks a random color by default
        title : str, optional
            Plot title
        aspect : {"auto", "data", "manual", "cube"}
            Aspect ratio for plot axes
            Defaults to "auto"
        aspect_ratio : dict, optional
            Aspect ratio to define if aspect type is "manual"
            Defaults to ``dict(x=1, y=1, z=1)``

        Raises
        ------
        ValueError
            If ``aspect`` does not take values from ``{"auto", "data", "manual", "cube"}``

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
            2-Tuple, containing labels for coordinates & momenta to plot
            Labels for ``X1, X2, X3, P1, P2, P3`` are ``(1, 2, 3, 4, 5, 6)``
            Defaults to ``(1, 2)`` (X, Y)
        figsize : tuple, optional
            2-Tuple of Figure Size in inches
            Defaults to ``(6, 6)``
        color : str, optional
            Hexcode (String) for the color of the
            dashed lines, that represent the Geodesic
            Picks a random color by default
        title : str, optional
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
        colors=("#00FFFF", "#FF00FF", "#FFFF00"),
        title: str = "Parametric Plot",
    ):
        """
        Plots the coordinates of the Geodesic, against Affine Parameter

        Parameters
        ----------
        geodesic : einsteinpy.geodesic.*
            Geodesic Object
        colors : tuple, optional
            3-Tuple, containing hexcodes (Strings) for the color
            of the lines, for each of the 3 coordinates
            Defaults to ``("#00FFFF", "#FF00FF", "#FFFF00")``
        title : str, optional
            Plot title

        """
        pass

    def show(self):
        """
        Shows plot during runtime

        Returns
        -------
        ~plotly.graph_objects.Figure

        """
        return self.fig

    def clear(self):
        """
        Clears plot during runtime

        """
        pass

    def save(self, name="Geodesic.png"):
        """
        Saves plot locally

        Parameters
        ----------
        name : str, optional
            Name of the file, with extension
            Defaults to ``Geodesic.png``

        """
        pass
