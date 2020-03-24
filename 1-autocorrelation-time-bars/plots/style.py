import numpy as np
from matplotlib.colors import LinearSegmentedColormap, hsv_to_rgb


def get_default_colormap():
    colors = [hsv_to_rgb((x, 0.7, 0.95)) for x in np.linspace(0.0, 1.0, 101)]
    cmap = LinearSegmentedColormap.from_list('default_cmap', colors)
    return cmap


class Style():
    def __init__(self, tick_size: int = 12, label_size: int = 14, title_size: int = 15, suptitle_size: int = 16,
                 fill: bool = False, fill_alpha: float = 0.7, show_x: bool = True, show_y: bool = True,
                 percent: bool = False, fig_size: tuple = (16, 5), dpi: int = 150,
                 line_width: int = 1):

        self.tick_size = tick_size
        self.label_size = label_size
        self.title_size = title_size
        self.suptitle_size = suptitle_size
        self.fill = fill
        self.fill_alpha = fill_alpha
        self.show_x = show_x
        self.show_y = show_y
        self.fig_size = fig_size
        self.percent = percent
        self.dpi = dpi
        self.line_width = line_width


colormap = get_default_colormap()
