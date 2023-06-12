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
fig, ax = plt.subplots()
ax.set_title('Wellness and pollution data')
ax.set_xlabel('Time')
ax.set_ylabel('Coefficient')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
ax.xaxis.set_major_locator(mdates.DayLocator())


# initialize the x and y data arrays
well_time = []
poll_time = []
wellness_data = []
pollution_data = []

# create a line plot of the wellness and pollution data
wellness_line, = ax.plot(well_time, wellness_data, color='purple', label='Wellness')
pollution_line, = ax.plot(poll_time, pollution_data, color='cyan', label='Pollution')
ax.legend()

# set the x-axis limits to show the most recent data
ax.set_xlim(0, 10)

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        # get the latest wellness and pollution data
        well_timestamp = terminal_service.get_data('wtime')
        well_timestamp = dt.datetime.strptime(well_timestamp, '%Y-%m-%d %H:%M:%S')
        poll_timestamp = terminal_service.get_data('ptime')
        poll_timestamp = dt.datetime.strptime(poll_timestamp, '%Y-%m-%d %H:%M:%S')

        wellness_coefficient = terminal_service.get_data('well')
        pollution_coefficient = terminal_service.get_data('poll')


        # append the new data to the x and y data arrays
        well_time.append(well_timestamp)
        poll_time.append(poll_timestamp)
        wellness_data.append(wellness_coefficient)
        pollution_data.append(pollution_coefficient)

        # update the line plot with the new data
        wellness_line.set_data(well_time, wellness_data)
        pollution_line.set_data(poll_time, pollution_data)

        # set the x-axis limits to show the most recent data
        #ax.set_xlim(max(0, len(x_data) - 10), len(x_data))

        # pause the plot for a short duration before updating it with new data
        plt.pause(5)
except KeyboardInterrupt:
    server.stop(0)
