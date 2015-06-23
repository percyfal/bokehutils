# Copyright (C) 2015 by Per Unneberg
import math
import pandas.core.common as com
from bokeh.palettes import brewer
import logging

logger = logging.getLogger(__name__)

MINSIZE = 3
MAXSIZE = 9  # FIXME: some palettes have 9 as max, some 11


def colorbrewer(size=MINSIZE, palette="PiYG", datalen=None):
    """Generate a colorblind-friendly color palette.

    Args:
      size (int): size of desired palette
      palette (str): name of palette
      datalen (int): length of data vector. If None, the palette size
                     will equal size, else the colors will be reused to fill
                     up a vector of length datalen

    Returns:
      palette (list): list of colors

    """
    size = max(MINSIZE, min(size, MAXSIZE))
    if datalen <= MAXSIZE and datalen >= MINSIZE:
        size = datalen
    colors = brewer[palette][size]
    if datalen > size:
        colors = colors * math.ceil(datalen / size)
        return colors[0:datalen]
    else:
        return colors
