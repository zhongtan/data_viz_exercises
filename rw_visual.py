import matplotlib.pyplot as plt

from random_walk import RandomWalk

keep_running = 'y'

# Keep making new walks, as long as the program is active.
while keep_running == 'y':
  # Make a random walk, and plot the points.
  rw = RandomWalk(5000)
  rw.fill_walk()

  # Set the size of the plotting window.
  plt.figure(dpi=128, figsize=(10, 6))

  point_numbers = list(range(rw.num_points))  
  plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
  
  # Emphasize the first and last points.
  plt.scatter(0, 0, c='green', edgecolors='none', s=10)
  plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=10)

  # Remove the axes.
  plt.axes().get_xaxis().set_visible(False)
  plt.axes().get_yaxis().set_visible(False)

  plt.show()

  keep_running = raw_input("Make another walk? (y/n): ")
  
  while keep_running != 'y' and keep_running != 'n':
    keep_running = raw_input("Make another walk? (y/n): ")
