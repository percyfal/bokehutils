import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

data = pd.DataFrame(
    [[1, 2, 3, 'control', 'male'],
     [2, 4, 2, 'control', 'female'],
     [3, 9, 11, 'case', 'female'],
     [4, 14, 3, 'case', 'male']],
    columns=['x', 'y', 'z', 'treatment', 'sex'],
)

source = ColumnDataSource(data)

fig = figure()
