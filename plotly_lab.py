from plotly.offline import plot
import plotly.graph_objs as go


#Plotly tutorials https://plot.ly/python/basic-charts/

#Line Graphs
scatter_data = go.Scatter(x=[1, 2, 3], y=[3, 2, 6])
plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='test_graph.html')

x_vals = []
y_vals = []
for val in range(20):
	x_vals.append(val)
	y_vals.append(val*val)

scatter_data2 = go.Scatter(x=x_vals, y=y_vals)
plot([go.Scatter(x=x_vals, y=y_vals)], filename='squared_graph.html')

#------------------------------------------------

#Bar Graphs
data = [go.Bar(
            x=['siteA-2015', 'siteB-2015', 'siteC-2015','siteA-2016', 'siteB-2016', 'siteC-2016'],
            y=[20, 14, 23, 19, 7, 20]
    )]
plot(data, filename='basic-bar.html')

#Grouped Bar chart DIY for comparing the sites

#-------------------------------------------------

#Pie Charts

#-------------------------------------------------
#Dynamic chart
#Chart motor-speed data
#Use pandas here

#Dash to combine these!


# We can also download an image of the plot by setting the image parameter
# to the image format we want
#plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='my-graph.html',image='jpeg')


# plotly.offline.init_notebook_mode(connected=True)

# plotly.offline.iplot({
#     "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#     "layout": go.Layout(title="hello world")
# })