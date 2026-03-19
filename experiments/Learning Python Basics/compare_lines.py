#creating all numbers from [0,0.1 .. 2] because i am lazy
i = 0
x = 0
theValue = 0
my_list = [0 for _ in range(21)]
for i in range(21):
    my_list[i] = theValue
    x = x + 0.1
    theValue = round(x,2)
print(my_list)
    ##my_list = [for in _ range(20)]