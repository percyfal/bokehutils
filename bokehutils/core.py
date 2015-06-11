# Copyright (C) 2015 by Per Unneberg
from functools import wraps
from bokeh.models import ColumnDataSource
from bokeh.plotting import Plot
import logging

logger = logging.getLogger(__name__)

class InspectArgs(object):
    """Decorator class to inspect arguments

    Will check for existence of fig, x, y, and make sure that note df
    and source are None simultaneously.

    Args:

      allow_y_list (bool): check for existence of y and convert it
      into a list to apply for all y.

    """
    
    def __init__(self, allow_y_list=False):
        self.allow_y_list = allow_y_list

    def __call__(self, f):
        @wraps(f)
        def check(*args, **kw):
            arglist = list(args)
            try:
                fig = kw.pop('fig') if 'fig' in kw else arglist.pop(0)
                x = kw.pop('x') if 'x' in kw else arglist.pop(0)
                y = kw.pop('y') if 'y' in kw else arglist.pop(0)
            except IndexError:
                logger.error("missing arguments to {}".format(f))
                raise
            assert isinstance(fig, Plot), \
                "argument %r does not match %s" % (fig, Plot)
            assert isinstance(x, str), \
                "argument %r does not match %s" % (x, str)
            if self.allow_y_list:
                if isinstance(y, list):
                    assert (all([isinstance(yy, str) for yy in y])), \
                    "argument %r does not match list(%s)" % (y, str)
                else:
                    assert (isinstance(y, str)), \
                        "argument %r does not match %s" % (y, str)
                    y = [y]
            else:
                assert isinstance(y, str), \
                    "argument %r does not match %s" % (y, str)
            try:
                df = kw.pop('df') if 'df' in kw else arglist.pop(0) if arglist else None
                source = kw.pop('source') if 'source' in kw else arglist.pop(0) if arglist else None
            except IndexError:
                logger.error("missing arguments to {}".format(f))
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
            if isinstance(y, str):
                if y not in source.column_names:
                    raise TypeError("y: '{}' not in {}".format(y, source.column_names))
            else:
                if any(yy not in source.column_names for yy in y):
                    raise TypeError("some y: '{}' not in {}".format(y, source.column_names))
            return f(fig=fig, x=x, y=y, df=df, source=source, *arglist, **kw)
        return check


def inspect_fig_arg(func):
    """Decorator to inspect fig argument to a function.

    Will check for existence of fig.

    """
    @wraps(func)
    def check(*args, **kw):
        arglist = list(args)
        try:
            fig = kw.pop('fig') if 'fig' in kw else arglist.pop(0)
        except IndexError:
            logger.error("missing arguments to {}".format(func))
            raise
        assert isinstance(fig, Plot), \
            "argument %r does not match %s" % (fig, Plot)
        return fig
    return check
