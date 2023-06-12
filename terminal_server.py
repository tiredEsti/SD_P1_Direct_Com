import grpc
from concurrent import futures
import time
from datetime import datetime


import plotly.graph_objects as go

# import the generated classes
import meteoServer_pb2
import meteoServer_pb2_grpc
from terminal_service import terminal_service


# create a class to define the server functions
class TerminalServiceServicer(meteoServer_pb2_grpc.TerminalServiceServicer):

    def AddTerminalData(self, data, context):
        terminal_service.add_terminal_data(data)
        response = meteoServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

meteoServer_pb2_grpc.add_TerminalServiceServicer_to_server(TerminalServiceServicer(),server)

# listen on port 50056
print('Starting server. Listening for terminal data to plot...')
server.add_insecure_port('0.0.0.0:50056')
server.start()

fig = go.FigureWidget()
fig.add_scatter()
#fig.add_scatter(start_x, start_y, mode='lines+markers', name='Wellness', color='pink')
#fig.add_scatter(start_x, start_y, mode='lines+markers', name='Pollution', color='cyan')
fig.layout.title = 'Wellness and pollution data'
fig.layout.xaxis.title = 'Time'
fig.layout.yaxis.title = 'Coefficient'
ctr = 0

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        with fig.batch_update():
            fig.data[0].x = terminal_service.get_x()
            fig.data[0].y = terminal_service.get_y()
        fig.data[0].x = terminal_service.
        ctr += 1
except KeyboardInterrupt:
    server.stop(0)
