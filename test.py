import time
from datetime import datetime
import plotly.graph_objects as go


fig = go.FigureWidget()
fig.add_scatter()
#fig.add_scatter(start_x, start_y, mode='lines+markers', name='Wellness', color='pink')
#fig.add_scatter(start_x, start_y, mode='lines+markers', name='Pollution', color='cyan')
fig.layout.title = 'Wellness and pollution data'
fig.layout.xaxis.title = 'Time'
fig.layout.yaxis.title = 'Coefficient'
ctr = 0
data = 5
fig


try:
    while True:
        with fig.batch_update():
            fig.data[0].x = data
            fig.data[0].y = datetime.now()
        ctr += 1
        data += 2
except KeyboardInterrupt:
    exit(0)
