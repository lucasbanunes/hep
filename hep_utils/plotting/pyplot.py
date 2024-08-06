
"""Utils for plotting with matplotlib.pyplot"""
from typing import Any, Dict, Union, Tuple
import matplotlib as mpl
import matplotlib.pyplot as plt
from hep_utils.formulas import norm1
from hep_utils.constants import RINGS_LAYERS
import pandas as pd
import numpy as np
import numpy.typing as npt


def plot_rings_profile(df: Union[pd.DataFrame, npt.NDArray[np.float_]],
                       ax: mpl.Axes = None,
                       normalize: bool = True
                       ) -> Tuple[mpl.Axes,
                                  npt.NDArray[np.float_],
                                  npt.NDArray[np.float_]]:
    """
    Plots the mean profile of the rings in the calorimeter.

    Parameters
    ----------
    df : Union[pd.DataFrame, npt.NDArray[np.float_]]
        Dataframe containing the rings or the rings array
    ax : mpl.Axes, optional
        Ax to plot the data, by default None
    normalize : bool, optional
        If True, normalizes the rings with norm1, by default True

    Returns
    -------
    Tuple[mpl.Axes,npt.NDArray[np.float_],npt.NDArray[np.float_]]
        ax: mpl.Axes
            The ax where the data was plotted
        mean: npt.NDArray[np.float_]
            The mean profile of the rings
        std: npt.NDArray[np.float_]
            The standard deviation of the rings
    """
    if isinstance(df, pd.DataFrame):
        rings = df.values
    if normalize:
        rings = norm1(rings)
    mean = rings.mean(axis=0)
    std = rings.std(axis=0)
    if ax is None:
        ax = plt.gca()
    lines = ax.plot(np.arange(len(mean)), mean,
                    label='Overlapped Zee', marker='o', linestyle='-')
    ax.fill_between(np.arange(len(mean)), mean - std, mean + std,
                    facecolor=lines[0].get_color(), alpha=0.25)
    _, y_up = ax.get_ylim()
    for layer_name, idxs in RINGS_LAYERS.items():
        ax.axvline(idxs[0], color='black', linestyle='--')
        ax.text(idxs[0]+0.5, y_up*0.95, layer_name,
                verticalalignment='center', fontsize=10)
    ax.axhline(0, color='black', linestyle='--')
    ax.legend()
    ax.set_title('Rings mean profile')
    ax.set_xlim(0, len(mean))
    ax.set_xlabel('Ring index')
    ax.set_ylabel('Normalized energy')
    return ax, mean, std


def histplot(data: Union[pd.Series, npt.NDArray[np.number]],
             nbins: int = 100,
             ax: mpl.Axes = None,
             metrics: bool = False,
             legend_kwargs: Dict[str, Any] = {},
             ax_set: Dict[str, Any] = {},
             hist_kwargs: Dict[str, Any] = {}
             ) -> Tuple[mpl.Axes, Dict[str, Any]]:
    """
    Plots a histogram of the data.

    Parameters
    ----------
    data : Union[pd.Series, npt.NDArray[np.number]]
        Data to plot
    nbins : int, optional
        Number of equally spaced bins, by default 100.
        If bins arg is passed in hist_kwargs, this is ignored.
    ax : mpl.Axes, optional
        Ax to plot the data, by default plt.gca()
    metrics : bool, optional
        If True writes mean, std, min, max and samples values in the legend, by default False
    legend_kwargs : Dict[str, Any], optional
        Kwargs for mpl.Axes.legend, by default {}.
        Used only when metrics is True.
    ax_set : Dict[str, Any], optional
        Kwargs for mpl.Axes.set, by default {}
    hist_kwargs : Dict[str, Any], optional
        Kwargs for mpl.Axes.hist, by default {}

    Returns
    -------
    Tuple[mpl.Axes, Dict[str, Any]]
        mpl.Axes
            The ax where the data was plotted
        Dict[str, Any]
            Dictionary with the metrics of the data.
            Empty dict if metrics is False.
    """
    if ax is None:
        ax = plt.gca()
    min_val = data.min()
    max_val = data.max()
    if hist_kwargs.get('bins') is None:
        hist_kwargs['bins'] = np.linspace(min_val, max_val, nbins)
    ax.hist(data, **hist_kwargs)
    ax.set(**ax_set)
    if metrics:
        metrics_dict = {
            'Samples': len(data),
            'Mean': data.mean(),
            'Std': data.std(),
            'Min': min_val,
            'Max': max_val
        }
        for key, value in metrics_dict.items():
            ax.plot([], [], ' ', label=f'{key}: {value:.2f}')
        ax.legend(**legend_kwargs)
        return ax, metrics_dict
    else:
        return ax, {}
