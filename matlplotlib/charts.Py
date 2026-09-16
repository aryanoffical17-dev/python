import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [5, 7, 8, 7, 6]

# plt.subplot(2,2,1)
# plt.plot(x, y, linestyle='-', marker='o', label="Line")
# plt.legend()

# plt.subplot(2,2,2)
# plt.scatter(x, y, color="red", label="Scatter")
# plt.legend()

# plt.subplot(2,2,3)
# plt.bar(x, y, color="green", label="Bar")
# plt.legend()

# plt.subplot(2,2,4)
# plt.hist(y, bins=5, color="purple", label="Hist")
# plt.legend()

# plt.tight_layout()
# plt.show()



# Data
expenses = [500, 300, 200, 150, 100]
categories = ["Rent", "Groceries", "Transport", "Entertainment", "Other"]

# Create Pie Chart
plt.pie(
    expenses,
    labels=categories,      # category names
    autopct="%.2f%%",      # show % with 1 decimal place
    startangle=90,          # rotate start angle
    shadow=True,            # add shadow
    explode=(0.1, 0, 0, 0, 0) # highlight "Rent" by separating it
)

plt.title("Monthly Expense Breakdown")
plt.show()
