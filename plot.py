import pandas as pd
import matplotlib.pyplot as plt

#to read the tsv file
values= pd.read_csv("/home/dharneesh/fython/proj/v_plot_3/sorted_file.tsv", sep = '\t', header = None)

#to define the column heading
values.columns =['freq','dist', 'len']

#assigning columns
x_values=values['dist']
y_values=values['len']
gradient=values['freq']
colours='Greens'

#to create scatter plot
plt.scatter(x_values, y_values, c=gradient, cmap=colours,vmin=0, vmax=100)

#labelling
plt.xlabel('Distance')
plt.ylabel('Length')
plt.title('V-Plot Analysis')

#assigning the gradient to color bar
plt.colorbar(label='freq')

#to display
plt.show()

