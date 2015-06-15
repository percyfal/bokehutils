"""The templates module is modelled directly after
:py:mod:`bokeh.templates`

"""
from os.path import join, abspath, split
import jinja2

_templates_path = join(abspath(split(__file__)[0]), "_templates")

EXAMPLE = jinja2.Template(
    open(join(_templates_path, "example.html")).read()
)
