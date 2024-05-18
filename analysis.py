# Pandas and pyplot import - these libraries are used to plot and analyse the data.
import pandas as pd
import matplotlib.pyplot as plt

# Loading the Iris dataset directly from the source github repository and assigning to variable df
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')

# Columns defined
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# summary.txt output
with open('summary.txt', 'w') as file:
    # Statistics summary using .describe() method
    file.write("Statistics Summary:\n") 
    file.write(df.describe().to_string())
    # Species count by [class]
    file.write('\n\nSpecies:\n')
    file.write(df['class'].value_counts().to_string())


