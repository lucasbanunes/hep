from typing import Union, Tuple
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
    _type_
        _description_
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
