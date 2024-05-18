# Pandas and pyplot import - these libraries are used to plot and analyse the data.
import pandas as pd
import matplotlib.pyplot as plt

# Loading the Iris dataset directly from the source github repository and assigning to variable df
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')

# Columns defined
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Import to be tested once library install issues resolved on linux laptop
with open('summary.txt', 'w') as file:
    # Statistics summary
    file.write("Statistics Summary:\n")
    file.write(df.describe().to_string())


