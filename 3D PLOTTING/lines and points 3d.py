from mpl_toolkits import mplot3d    #using matplotlib toolkits

import numpy as np      #numpy is used for lines and points
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection="3d")

z_line = np.linspace(0, 15, 1000)      #linspace(start,stop,number)
x_line = np.cos(z_line)
y_line = np.sin(z_line)
ax.plot3D(x_line, y_line, z_line, 'gray')  #gray is colour ,draws line

z_points = 15 * np.random.random(100)      #points at x,y and z
x_points = np.cos(z_points) + 0.1 * np.random.randn(100)
y_points = np.sin(z_points) + 0.1 * np.random.randn(100)
ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv');  #scatters points

plt.show()

#scatter3(X,Y,Z) displays circles at the locations specified by the vectors X, Y, and Z.
#scatter3(X,Y,Z,S) draws each circle with the size specified by S. To plot each circle with equal size, specify S as a scalar. To plot each circle with a specific size, specify S as a vector.
#scatter3(X,Y,Z,S,C) draws each circle with the color specified by C.
#If C is a RGB triplet or character vector or string containing a color name, then all circles are plotted with the specified color.
#If C is a three column matrix with the number of rows in C equal to the length of X, Y, and Z, then each row of C specifies an RGB color value for the corresponding circle.
#If C is a vector with length equal to the length of X, Y, and Z, then the values in C are linearly mapped to the colors in the current colormap.
#scatter3(___,'filled') fills in the circles, using any of the input argument combinations in the previous syntaxes.
#scatter3(___,markertype) specifies the marker type.
#scatter3(___,Name,Value) modifies the scatter chart using one or more name-value pair arguments.
#scatter3(ax,___) plots into the axes specified by ax instead of into the current axes (gca). The ax option can precede any of the input argument combinations in the previous syntaxes.
#h = scatter3(___) returns the Scatter object. Use h to modify properties of the scatter chart after it is created.
