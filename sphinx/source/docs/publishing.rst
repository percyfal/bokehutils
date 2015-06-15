Publishing static documents
===========================

One of the great features of Bokeh is that you don't have to run a
server to show interactive plots. It's actually easy to embed them in
the html document. 


Currently :py:mod:`bokehutils.publish` has two utility functions
that extends the functionality of :py:mod:`bokeh.embed`. First,
:meth:`~bokehutils.publish.static_html` takes a jinja template and a
list of keyword arguments with Bokeh components and renders a static
html document. Second, based on :meth:`snakemake.report.data_uri`,
there is a function for creating base64 data URIs from files, so that
also the raw data on which plots are based can be attached to the
document.


Examples
---------

.. bokeh-plot::
    :source-position: above

    import os
    from bokeh.sampledata.iris import flowers
    from bokeh.models import ColumnDataSource
    from bokeh.plotting import figure, show
    from bokehutils.facet import facet_grid
    from bokehutils.geom import lines, points
    from bokehutils.publish import static_html
    from bokehutils.templates import EXAMPLE, _templates_path

    source = ColumnDataSource(flowers)
    f = figure()
    points(f, "sepal_length", "sepal_width", source=source)
    gp = facet_grid(f, "sepal_length", "sepal_width", 
                    flowers, groups="species",
		    width=300, height=300,
		    share_x_range=True,
		    share_y_range=True)

    fig = figure(width=300, height=300)
    points(fig, "sepal_length", "sepal_width", source=source)

    with open(os.path.join(_templates_path, os.pardir, os.pardir, "sphinx", "_build", "html", "docs", "myplots.html"), "w") as fh:
        fh.write(static_html(EXAMPLE, **{'gridplot': gp, 'figure': fig}))

    show(gp)
