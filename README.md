# pands-project
<h1>Programming and Scripting - Spring semester 2024 Project</h1>

<h2>Summary</h2>

The Iris data set is a classical data set used in statistics and machine learning, popularised by statistician Ronald A. Fisher. The Iris data set is derived from observations made by botanist Edgar Anderson for his seminal paper 'The Species Problem In Iris'. This paper appears from pages 457-509 in volume 23 of the Annals of the Missouri Botanical Garden 1936[1]. The goal of Andersons' original paper was to investigate and distinguish between similarly structured Iris species by using more a nuanced approach than just clear cut physical characteristics which at the time was the status quo in botany.

The Iris data set includes 150 records of iris flowers with four features: 

- sepal length in centimetres.
- sepal width in centimetres.
- petal length in centimetres.
- petal width in centimetres.

The iris flowers are also classified by species into three types: 

- Iris Setosa.
- Iris Versicolor.
- Iris Virginica.

<h2>Dependencies</h2>

* Python - General purpose programming language.
* Pandas - Python data analysis library.
* Matplotlib.pyplot - Collection of matplotlib functions.
* Seaborn - Python data visualization library based on matplotlib.

<h2>Running the Analysis</h2>

1. Open your prefered terminal and navigate to a location you wish to save this analysis, for this project bash was used.
2. Download/clone the repository by entering the following into your terminal - git clone https://github.com/CianGallagher/pands-project.git
3. Install the above dependencies. This may differ depending on your Operating System (OS) but once they have been installed on your system the script can be run. For this project the homebrew/pip package managers were used.  
4. In the terminal run 'python .\analysis.py'. Please note that on some systems you may need to specify your version of python e.g. 'python3 analysis.py'.

<h2>Script details and output</h2>

<h2>References</h2>

- The Species Problem In Iris - http://biostor.org/reference/11559 [1]

- Markdown quick reference - https://wordpress.com/support/markdown-quick-reference/ 

- Reading in a CSV file from a raw github user - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html 

- Python write() function - https://www.w3schools.com/python/python_file_write.asp

- matplotlib plotting histogram each loop - https://stackoverflow.com/questions/50773877/create-for-loop-to-plot-histograms-for-individual-columns-of-dataframe-with-seab 

- matplotlib colors - https://matplotlib.org/stable/gallery/color/named_colors.html

- String Literals for histogram naming- https://baalkikhaal.github.io/2021/03/05/Handling-string-literals-in-matplotlib.html

- seaborn.pairplot - https://seaborn.pydata.org/generated/seaborn.pairplot.html

- seaborn.violinplot - https://www.geeksforgeeks.org/violinplot-using-seaborn-in-python/

- seaborn styles https://seaborn.pydata.org/generated/seaborn.set_style.html