import matplotlib.pyplot as plt
import sklearn 
# import 

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker="o")
plt.title("Simple Line Plot")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")

# Save neatly cropped
plt.savefig("line_plot.png", bbox_inches="tight")
plt.show()
