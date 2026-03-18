import matplotlib.pyplot as plt

def plot_square(): 
    y_line = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        x = (i * i) + 3
        y_line[i] = x
    plt.plot([1,2,3,4,5,6,7,8,9,10], y_line)

plot_square()
plt.show()

# TODO how can i check if i have a perfect square lol
# TODO create a check if something is can be calculated by a * a // a = int(math.sqrt())
