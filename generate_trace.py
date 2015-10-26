__author__ = 'jman'
import time
from datetime import datetime, timedelta
import json
import random
import threading
import logging


# default logger
logger = logging.getLogger('mangoS.SeedlinkClient')


class GenerateTrace(threading.Thread):

    def __init__(self, queue):


        self._buffer = []
        self._queue = queue
        #self._time = datetime.now()
        self._time = datetime(2015,1,1,0,0,0)
        self._endtime = datetime(2015,1,1,23,59,59)

        self.plus_time = 2 # second
        self.queue_threshold_count = 10000000000000000000

        threading.Thread.__init__(self)
        self.CHANNELS = ['BHZ', 'BHE', 'BHN', 'EHZ', 'EHE', 'EHN', 'HHZ', 'HHE', 'HHN','SHN','SHE','SHZ','UHN','UHE','UHZ'] # 15

        pass

    def run(self):

        while True:

            if self._queue.qsize() > self.queue_threshold_count:
                time.sleep(0.5)
                logger.info("Wait Queue emptying.. %s | %s | %d", "", "", self._queue.qsize())
                continue

            plusSecond = timedelta(seconds=3)

            for _lst in self._buffer:

                network = _lst[0]
                station = _lst[1]
                nsamp = _lst[2]


                for channel in self.CHANNELS:
                    data = {}
                    data['st'] = self._time
                    data['n'] = nsamp * self.plus_time
                    data['c'] = 1
                    data['s'] = nsamp
                    data['d'] = self.get_random_list(data['n'])
                    data['et'] = self._time + plusSecond

                    data['network'] = network
                    data['station'] = station
                    data['location'] = ''

                    data['channel'] = channel
                    #print data
                    self._queue.put(data)

                #logger.info(">> Put Queue.. %s_%s | %s | %d", data['network'], data['station'], data['st'], self._queue.qsize())

            self._time = self._time + plusSecond
            self._curtime = self._time

            if ( self._time > self._endtime ):
                break

        pass

    def set_buffer(self, network, station, nsamp):
        self._buffer.append([network, station, nsamp])

    def get_random_list(self, count):

        temp_list = []
        for i in range(count):
            temp_list.append(random.randint(-99999,99999))

        return temp_list
