# Copyright (C) 2015 by Per Unneberg

import logging

logger = logging.getLogger(__name__)

def aes(x, y=None, **kwargs):
    """aes - map aestethics a la ggplot.

    Would be nice to have this functionality. However, it would
    require

    1. getting hold of the correct glyph renderer
    2. getting the glyph of this renderer

    3. since a glyph has one color, this means we have to generate a
       renderer for each factor

    See `styling glyphs <http://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#glyphs>`_
    
    """
    pass
