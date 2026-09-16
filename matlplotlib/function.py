import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, label="Line" ,linestyle='-',marker='s')          # Line plot
plt.scatter(x, y, color="red")        # Scatter plot
plt.bar(x, y, alpha=0.5, label="Bar") # Bar plot

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Plots Example")
plt.legend()
plt.grid()
plt.show()



# important 

    # plt.plot(x,y ,color='color name' , linestyple ='line_style',linewidth = '4' marker = 'marker symbol , lable='label name')
