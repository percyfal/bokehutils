import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

data = pd.DataFrame(
    [[1, 2, 'control', 'male'],
     [2, 4, 'control', 'female'],
     [3, 9, 'case', 'female'],
     [4, 14, 'case', 'male']],
    columns=['x', 'y', 'treatment', 'sex'],
)

source = ColumnDataSource(data)

fig = figure()
