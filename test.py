import time
from datetime import datetime
import plotly.graph_objects as go


ctr = 0
idk = 5
idata = []
idtm = []
fig = go.FigureWidget()
fig.add_scatter(y=idata, x=idtm)
#fig.add_scatter(start_x, start_y, mode='lines+markers', name='Wellness', color='pink')
#fig.add_scatter(start_x, start_y, mode='lines+markers', name='Pollution', color='cyan')
fig.layout.title = 'Wellness and pollution data'
fig.layout.xaxis.title = 'Time'
fig.layout.yaxis.title = 'Coefficient'
fig.show()
go.FigureWidget().close()

try:
    while True:
        idtm.append(datetime.now())
        idata.append(idk)
        with fig.batch_update():
            fig.data[0].x = idata
            fig.data[0].y = idtm
        ctr += 1
        idk += 2
except KeyboardInterrupt:
    go.FigureWidget().close()
    exit(0)
