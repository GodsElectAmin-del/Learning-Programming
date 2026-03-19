import matplotlib.pyplot as plt
from math import exp

def compare_lines():    
    x_line = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    y_line1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_line2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_line3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for idx, i in enumerate(x_line):
        y1 = i
        y2 = i * i
        y3 = exp(i)
        y_line1[idx] = y1
        y_line2[idx] = y2
        y_line3[idx] = y3
    plt.plot(x_line,y_line1)
    plt.plot(x_line,y_line2)
    plt.plot(x_line,y_line3)
compare_lines()
plt.legend(["line linear"],["line Polynomial"],["line Exponetial"])
plt.show()
