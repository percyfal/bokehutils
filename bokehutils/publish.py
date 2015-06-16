# Copyright (C) 2015 by Per Unneberg
import os
import mimetypes
import base64
from bokeh.resources import INLINE
from bokeh.templates import RESOURCES
from bokeh.embed import components
from bokeh.models.widget import Widget
from bokeh.util.string import encode_utf8


def static_html(template, resources=INLINE, as_utf8=True, **kw):
    """Render static html document.

    This is a minor modification of :py:meth:`bokeh.embed.file_html`.

    Args:
      template (Template): jinja2 HTML document template
      resources (Resources): a resource configuration for BokehJS assets
      as_utf (bool): render utf8 output
      kw: keyword argument list of bokeh components. Keywords must match
          with keywords in template

    Returns:
      html : standalone HTML document with embedded plot

    """
    plot_resources = RESOURCES.render(
        js_raw=resources.js_raw,
        css_raw=resources.css_raw,
        js_files=resources.js_files,
        css_files=resources.css_files,
    )

    with open(os.path.join(os.path.dirname(__name__),
                           os.pardir, 'static/basic.css')) as fh:
        css = "".join(fh.readlines())

    # Hack to get on-the-fly double mapping
    def _update(kw):
        tmp = {}
        for k, v in kw.items():
            if (isinstance(v, Widget)):
                tmp.update({k: [{'script': s, 'div': d}
                                for s, d in [components(v, resources)]][0]})
            elif (isinstance(v, dict)):
                if not v:
                    tmp.update(v)
                else:
                    v.update(_update(v))
            else:
                tmp.update({k: v})
        return tmp

    kw.update(_update(kw))
    if as_utf8:
        return encode_utf8(template.render(plot_resources=plot_resources,
                                           css=css, **kw))
    else:
        return template.render(plot_resources=plot_resources, css=css, **kw)


# This function is directly copied from snakemake.report
def data_uri(file, defaultenc="utf8"):
    """Craft a base64 data URI from file with proper encoding and mimetype."""
    mime, encoding = mimetypes.guess_type(file)
    if mime is None:
        mime = "text/plain"
        logger.info("Could not detect mimetype for {}, assuming "
                    "text/plain.".format(file))
    if encoding is None:
        encoding = defaultenc
    with open(file, "rb") as f:
        data = base64.b64encode(f.read())
    uri = ("data:{mime};charset={charset};filename={filename};base64,{data}"
           "".format(filename=os.path.basename(file),
                     mime=mime,
                     charset=encoding,
                     data=data.decode()))
    return uri
