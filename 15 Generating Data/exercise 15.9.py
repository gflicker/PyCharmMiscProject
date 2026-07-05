#List comprehensions
#Rolling three D6s

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some roles, and store results in a list
result = die_1.roll() + die_2.roll() + die_3.roll()
results = [result for value in range(1000)]

#Analyze the results
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [result.count(value) for value in range(2,max_result)]

#Visualize the results
x_values = list(range(3,max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling three D6s 1000 times',
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd8_d8.html')
