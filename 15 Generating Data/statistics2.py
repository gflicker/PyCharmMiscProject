import matplotlib.pyplot as plt

#Plotting a mathematics statistics question paper 2
input_values = range(0,70,10)
patients = [0, 5, 15, 40, 70, 90, 100]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values,patients, linewidth=3)

#Set chart title and label axes
ax.set_title('Statistics Exam Question P2', fontsize=24)
ax.set_xlabel('Age (in years)', fontsize=14)
ax.set_ylabel('Number of Patients', fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

#Setting the y-axis scale
plt.yticks(range(0, 110, 10))

plt.show()