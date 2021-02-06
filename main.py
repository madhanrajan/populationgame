
x = 50
y = 50

z_pop = 1


x_tim = []
y_tim = []

time_step = range(1000)

import random

for i in time_step:
    if x > 0:

        if random.randint(0,1):
            x += 1
            if z_pop >= 0:
                z_pop -= 1
            elif y >= 0:
                y -= 1
            else:
                x -= 3
                z_pop += 2
        
    else:
        x =0


    if y > 0:
        if random.randint(0,1):
            y += 1
            if z_pop >= 0:
                z_pop -= 1
            elif x >= 0:
                x -= 1
            else:
                y -= 3
                z_pop += 2
    else:
        y = 0

    if z_pop == 0:
        print("Food depleted at timestep {}".format(i))



    x_tim.append(x)
    y_tim.append(y)


from matplotlib import pyplot as plt


plt.plot(time_step, x_tim,'b')
plt.plot(time_step, y_tim,'r')

plt.show()