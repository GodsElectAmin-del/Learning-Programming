def plot_square(y_line): 
    #y_line = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        x = i * i + 3
        for ii in range(10):
            y_line[ii] = x
    #y_line = [0,0,0,0,0,0,0,0,0,0]
    #plt.plot(y_line, [1,2,3,4,5,6,7,8,9,10])
    return y_line

plot_square([0,0,0,0,0,0,0,0,0,0])
#plt.show()

# TODO how can i check if i have a perfect square lol
# TODO create a check if something is can be calculated by a * a // a = int(math.sqrt())
