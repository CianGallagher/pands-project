# Pandas and pyplot import - these libraries are used to plot and analyse the data.
import pandas as pd
import matplotlib.pyplot as plt

# Loading the Iris dataset directly from the source github repository and assigning to variable df, s
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')

# Columns defined
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Import to be tested once library install issues resolved


