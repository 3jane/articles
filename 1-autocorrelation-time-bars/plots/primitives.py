import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from .style import Style, colormap

from typing import Optional

from copy import deepcopy


def curve(y: np.array, x: np.array = None, threshold: float = 0, title: Optional[str] = None,
          xlabel: Optional[str] = None, ylabel: Optional[str] = None,
          pos_legend_label: Optional[str] = None, neg_legend_label: Optional[str] = None,
          pos_color: tuple = colormap(0.56), neg_color: tuple = colormap(0.045),
          style: 'Style' = Style(), return_fig: bool = False, ax=None):

    x = x if x is not None else list(range(y.size))
    y = deepcopy(y)

    if style.percent:
        y = y*100
        threshold = threshold*100

    fig, ax1 = plt.subplots(figsize=style.fig_size, dpi=style.dpi, facecolor="w") if ax is None else (None, ax)
    configure_axis(ax1, style)

    ax1.set_title(title, fontsize=style.title_size)
    ax1.set_xlabel(xlabel, fontsize=style.label_size, labelpad=15)
    ax1.set_ylabel(ylabel, fontsize=style.label_size, labelpad=15)

    if np.any(y >= threshold):
        y_pos = np.where(y >= threshold, y, np.nan)
        y_pos[_edges_of_nans(y_pos)] = threshold
        ax1.plot(x, y_pos, color=pos_color, linewidth=style.line_width, label=pos_legend_label)
        if style.fill:
            ax1.fill_between(x, threshold, y_pos, facecolor=pos_color, alpha=style.fill_alpha)

    if np.any(y < threshold):
        y_neg = np.where(y < threshold, y, np.nan)
        y_neg[_edges_of_nans(y_neg)] = threshold
        ax1.plot(x, y_neg, color=neg_color, linewidth=style.line_width, label=neg_legend_label)
        if style.fill:
            ax1.fill_between(x, threshold, y_neg, facecolor=neg_color, alpha=style.fill_alpha)

    if ax is None:
        if return_fig:
            return (fig, ax1)
        else:
            fig.tight_layout()
            fig.show()



def bars(y: np.array, x: np.array = None, threshold: float = 0, title: Optional[str] = None,
         xlabel: Optional[str] = None, ylabel: Optional[str] = None, style: 'Style' = Style(),
         pos_color: tuple = colormap(0.56), neg_color: tuple = colormap(0.045),
         pos_legend_label: Optional[str] = None, neg_legend_label: Optional[str] = None,
         return_fig: bool = False, ax=None):

    x = x if x is not None else list(range(y.size))
    y = deepcopy(y)

    if style.percent:
        y = y*100
        threshold = threshold*100

    fig, ax1 = plt.subplots(figsize=style.fig_size, facecolor="w") if ax is None else (None, ax)
    configure_axis(ax1, style)

    ax1.set_title(title, fontsize=style.title_size)
    ax1.set_xlabel(xlabel, fontsize=style.label_size, labelpad=15)
    ax1.set_ylabel(ylabel, fontsize=style.label_size, labelpad=15)

    if np.any(y >= threshold):
        y_pos = np.where(y >= threshold, y-threshold, np.nan)
        ax1.bar(x, height=y_pos, bottom=threshold, color=pos_color, linewidth=style.line_width, label=pos_legend_label)

    if np.any(y < threshold):
        y_neg = np.where(y < threshold, y-threshold, np.nan)
        ax1.bar(x, height=y_neg, bottom=threshold, color=neg_color, linewidth=style.line_width, label=neg_legend_label)

    if ax is None:
        if return_fig:
            return (fig, ax1)
        else:
            fig.tight_layout()
            fig.show()


def area(y1: np.array, y2: np.array, x: np.array = None, title: Optional[str] = None,
         xlabel: Optional[str] = None, ylabel: Optional[str] = None, style: 'Style' = Style(),
         color: tuple = colormap(0.56), legend_label: Optional[str] = None, return_fig: bool = False, ax=None):

    x = x if x is not None else list(range(y1.size))
    y1 = deepcopy(y1)
    y2 = deepcopy(y2)

    if style.percent:
        y1 = y1*100
        y2 = y2*100

    fig, ax1 = plt.subplots(figsize=style.fig_size, facecolor="w") if ax is None else (None, ax)
    configure_axis(ax1, style)

    ax1.set_title(title, fontsize=style.title_size)
    ax1.set_xlabel(xlabel, fontsize=style.label_size, labelpad=15)
    ax1.set_ylabel(ylabel, fontsize=style.label_size, labelpad=15)

    ax1.plot(x, y1, color=color, linewidth=style.line_width, label=legend_label)
    ax1.plot(x, y2, color=color, linewidth=style.line_width)
    ax1.fill_between(x, y1, y2, facecolor=color, alpha=style.fill_alpha)

    if ax is None:
        if return_fig:
            return (fig, ax1)
        else:
            fig.tight_layout()
            fig.show()



def second_index(ax, x2: np.array, xlabel: Optional[str] = None, style: 'Style' = Style(), rotation: int = 0):
    x1 = list(ax.lines[0].get_xdata())

    x1_tick_locs = ax.get_xticks()
    x1_tick_loc_ids = [(x1.index(l) if l in x1 else None) for l in x1_tick_locs]
    x2_tick_labels = [(x2[i] if i is not None else None) for i in x1_tick_loc_ids]

    ax2 = ax.twiny()
    ax2.set_frame_on(False)
    ax2.set_xticks(x1_tick_locs)
    ax2.set_xticklabels(x2_tick_labels)
    ax2.set_xlim(ax.get_xlim())
    ax2.xaxis.set_ticks_position('bottom')
    ax2.xaxis.set_label_position('bottom')
    ax2.spines['bottom'].set_position(('outward', 20))

    ax2.set_xlabel(xlabel, fontsize=style.label_size, labelpad=15)

    [lbl.set_rotation(rotation) for lbl in ax2.get_xticklabels()]


def configure_axis(ax, style: 'Style'):
    ax.set_frame_on(False)
    ax.grid(color='lightgray', linestyle='-.', linewidth=0.5)

    formatter = ticker.PercentFormatter(decimals=0) if style.percent else ticker.FormatStrFormatter('%.2f')
    ax.yaxis.set_major_formatter(formatter)
    if not style.show_x:
        ax.xaxis.set_major_formatter(ticker.NullFormatter())
    if not style.show_y:
        ax.yaxis.set_major_formatter(ticker.NullFormatter())
    ax.tick_params(axis='both', which='major', labelsize=style.tick_size)

#######
# Utility functions
#######


def _edges_of_nans(array: np.array):
    # display(array)
    # > [1, nan, nan, 2, 3, nan, 1, nan, nan, nan]
    isnan = np.concatenate(([0], np.isnan(array), [0]))
    # > [0 0 1 1 0 0 1 0 1 1 1 0]
    changes = np.abs(np.diff(isnan))
    # > [0 1 0 1 0 1 1 1 0 0 1]
    ranges = np.where(changes == 1)[0].reshape(-1, 2)
    # > [[ 1  3], [ 5  6], [ 7 10]]
    ranges[:, 1] = ranges[:, 1] - 1
    # > [[1 2], [5 5], [7 9]]
    edges = np.unique(ranges.ravel())
    # > [1 2 5 7 9]
    return edges