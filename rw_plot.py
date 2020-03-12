import matplotlib.pyplot as plt

from random_walk import RandomWalk

#make a walk
rw = RandomWalk()
rw.fill_walk()

#make a line plot of the walk
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth = 3)

#plot stylings
ax.set_title("Molecular Motion Simulation")
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()