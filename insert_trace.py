__author__ = 'jman'

import threading
import logging
import pymongo
from pymongo.errors import AutoReconnect
from pymongo.errors import DuplicateKeyError



# default logger
logger = logger = logging.getLogger('mangoT.InsertTrace')
INS_PACKET_LOG_PRINT_COUNT_THRESHOLD = 10

class InsertTrace(threading.Thread):

    def __init__(self, mongo_name, db_name, queue):

        threading.Thread.__init__(self)

        self._mongo_name = mongo_name
        self._db_name = db_name
        self._queue = queue

        try:
            self._con = pymongo.MongoClient(mongo_name)
        except pymongo.errors.ConnectionFailure:
            logger.error("No Host found", exc_info=True)
            return

        self._db = self._con['trace']
        pass

    def run(self):

        self._print_cnt = 0

        while(True):
           self.insert_document_per_second_and_station_collection_unlimited()

        pass

    def insert_document_per_second_and_station_collection_unlimited(self):

        print_cnt = 0

        while(True):

            # get from queue
            get_data = self._queue.get()

            network = get_data['network']
            station = get_data['station']
            location = get_data['location']
            channel = get_data['channel']
            start_time = get_data['st']


            # make collection name
            collection_name = network + "_" + station

            # make data
            data = {}
            data['st'] = str(get_data["st"])
            data['et'] = str(get_data["et"])
            data['n'] = get_data["n"]
            data['c'] = get_data["c"]
            data['s'] = get_data["s"]
            data['d'] = get_data['d']

            # insert mongoDB
            coll = self._db[collection_name]

            #make key
            str_yyyy_mm_dd_hh_mm_ss = '{0:04d}'.format(start_time.year) + "-" + '{0:02d}'.format(start_time.month) + "-" + '{0:02d}'.format(start_time.day) + "T" + '{0:02d}'.format(start_time.hour) + ':' + '{0:02d}'.format(start_time.minute) + ':' + '{0:02d}'.format(start_time.second)
            key = {}
            key['_id'] = str_yyyy_mm_dd_hh_mm_ss

            try:
                coll.update(key, {'$set':{channel:data}}, upsert=True,multi=False)

                if print_cnt > INS_PACKET_LOG_PRINT_COUNT_THRESHOLD:
                    logger.info("<< Insert Queue.. %s_%s_%s | %s | %d", get_data['network'], get_data['station'], get_data['channel'], get_data['st'], self._queue.qsize())
                    print_cnt = 0
                print_cnt += 1


            except AutoReconnect as exception:
                logger.warn(exception.args)
                pass

            except DuplicateKeyError as exception:
                coll.update(key, {'$set':{channel:data}}, upsert=False,multi=False)
                logger.info("<<<< INERT Queue.. %s_%s_%s | %s | %d", get_data['network'], get_data['station'], get_data['channel'], get_data['st'], self._queue.qsize())
            pass


        pass

