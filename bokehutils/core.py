# Copyright (C) 2015 by Per Unneberg
from functools import wraps
from bokeh.models import ColumnDataSource
from bokeh.plotting import Plot
import logging

logger = logging.getLogger(__name__)


def inspect_args(func):
    @wraps(func)
    def check(*args, **kw):
        arglist = list(args)
        try:
            fig = kw.pop('fig') if 'fig' in kw else arglist.pop(0)
            x = kw.pop('x') if 'x' in kw else arglist.pop(0)
            y = kw.pop('y') if 'y' in kw else arglist.pop(0)
        except IndexError:
            logger.error("missing arguments to {}".format(func))
            raise
        assert isinstance(fig, Plot), \
            "argument %r does not match %s" % (fig, Plot)
        assert isinstance(x, str), \
            "argument %r does not match %s" % (x, str)
        assert isinstance(y, str), \
            "argument %r does not match %s" % (y, str)

        try:
            df = kw.pop('df') if 'df' in kw else arglist.pop(0) if arglist else None
            source = kw.pop('source') if 'source' in kw else arglist.pop(0) if arglist else None
        except IndexError:
            logger.error("missing arguments to {}".format(func))
            raise
        if source is None and df is None:
            raise TypeError(__name__ + """: both source and df None;
        you need to pass at least a data source or a data frame""")

        if source is not None:
            df = source.to_df()
        elif source is None:
            source = ColumnDataSource(df)
        else:
            raise

        if x not in source.column_names:
            raise TypeError("x: '{}' not in {}".format(x, source.column_names))
        if y not in source.column_names:
            raise TypeError("y: '{}' not in {}".format(y, source.column_names))

        return func(fig=fig, x=x, y=y, df=df, source=source, *arglist, **kw)

    return check

