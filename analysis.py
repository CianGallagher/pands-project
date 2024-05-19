# Pandas, matplotlib, and seaborn imported - these libraries are used to plot and manipulate the data more easily.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the Iris dataset directly from the source github repository and assigning to variable df
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')

# Columns defined
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# summary.txt output
with open('summary.txt', 'w') as file:
    # .write() used to write the arguments into the txt file. Statistics summary produced using pandas .describe() method.
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
    df[column].hist(bins=30, edgecolor='black', color='cornflowerblue')
    # Using string literals to apply current column in naming convention.
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(f'{column}_histogram.png')
    # Closing to avoid issues with overlap or memory issues.
    plt.close()

# pairplot_scatter.png output - Seaborn includes a built in pair function for plotting, added to dependencies.
sns.pairplot(df, hue='class', markers=['o', 's', 'D'])
plt.savefig('pairplot_scatter.png')
plt.close()

# pairplot_violin.png output - Extra plot - Seaborn also has a built in violin plot function - This is really interesting as it not only illustrates the data sets numerical data but it also looks like a flower.
# NOT SURE HOW USEFUL THIS PLOT IS APART FROM THE FACT IT LOOKS LIKE A FLOWER...
for feature in df.columns[:-1]:
    plt.figure()
    sns.violinplot(x='class', y=feature, data=df, style='whitegrid')
    plt.title(f'{feature} distribution by species')
    plt.xlabel('Species')
    plt.ylabel(feature)
    plt.savefig(f'{feature}_violin.png')
    plt.close()