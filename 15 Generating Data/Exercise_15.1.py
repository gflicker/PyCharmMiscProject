#Plotting the first 5000 cubic numbers
import matplotlib.pyplot as plt

input_values = range(5000)
cubes = [x**3 for x in input_values]

#The graph and type of plotting
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(input_values,cubes, c='red', s=8)

#Scale on each axis
ax.tick_params(axis='both', which='major', labelsize=15)

#Setting title and labels
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Numbers to be cubed", fontsize=16)
ax.set_ylabel("Cubes", fontsize=16)

#Calling the function to plot the points
plt.show()