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

# histogram.png output
# Run the for loop over all columns apart from the final one 'class' as this gives the reader no useful information.
for column in df.columns[:-1]:
    # Plots each loop  
    plt.figure()
    # Formatting of histogram
    df[column].hist(bins=50, edgecolor='black')
    # Using string literals to apply current column in naming convention.
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(f'{column}_histogram.png')
    plt.close()
