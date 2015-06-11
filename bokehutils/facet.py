# Copyright (C) 2015 by Per Unneberg
import pandas.core.common as com
from bokehutils.core import InspectArgs
from bokehutils.geom import points, dotplot, lines
from bokeh.palettes import brewer
import logging

logger = logging.getLogger(__name__)

@InspectArgs()
def facet_grid(fig, x, y, df=None, source=None, groups=None, **kwargs):
    if not groups:
        logger.warn("no groups defined; returning without modifying figure")
        return
    try:
        grouped = df.groupby(groups)
    except:
        raise
    for name, group in grouped:
        print (name, group)
    print(fig.renderers)
