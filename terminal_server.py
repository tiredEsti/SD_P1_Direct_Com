import grpc
from concurrent import futures
import time
import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

# create a figure and axis object
fig = plt.figure(figsize = (7, 5))
ax = fig.add_subplot(2,1,1)
ax.set_title('Wellness and pollution data')
ax.set_xlabel('Time')
ax.set_ylabel('Coefficient')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

# initialize the x and y data arrays
wtime = []
ptime = []
wcoef = []
pcoef = []

# create a line plot of the wellness and pollution data
wellness_line, = ax.plot(wtime, wcoef, color='purple', label='Wellness')
pollution_line, = ax.plot(ptime, wcoef, color='cyan', label='Pollution')
ax.legend()

# set the x-axis limits to show the most recent data
#ax.set_xlim(0, 10)

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        # update the line plot with the new data
        wellness_line.set_data(terminal_service.wtime, terminal_service.wcoef)
        pollution_line.set_data(terminal_service.ptime, terminal_service.pcoef)

        # set the x-axis limits to show the most recent data
        # Rotating X-axis labels
        for tick in ax.get_xticklabels():
            tick.set_rotation(90)
        ax.relim()
        ax.autoscale_view()

        # pause the plot for a short duration before updating it with new data
        print("Plot Update")
        plt.pause(5)
except KeyboardInterrupt:
    server.stop(0)
