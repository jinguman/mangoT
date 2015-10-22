__author__ = 'jman'

import threading
import logging
import pymongo
from pymongo.errors import AutoReconnect
from pymongo.errors import DuplicateKeyError
import json


# default logger
logger = logger = logging.getLogger('mangoT.InsertTrace')


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
           self.put_station_collection_unlimited()

        pass

    def put_station_collection_unlimited(self):

        print_cnt = 0

        while(True):

            # get from queue
            get_data = self._queue.get()

            network = get_data['network']
            station = get_data['station']
            location = get_data['location']
            channel = get_data['channel']

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
            self._col = self._db[collection_name]

            key = {}
            key['_id'] = data['st']

            try:
                self._col.update(key, {'$set':{channel:data}}, upsert=True,multi=False)

                if print_cnt > 1000:
                    logger.info("<< Insert Queue.. %s_%s_%s | %s | %d", get_data['network'], get_data['station'], get_data['channel'], get_data['st'], self._queue.qsize())
                    print_cnt = 0
                print_cnt += 1


            except AutoReconnect as exception:
                logger.warn(exception.args)
                pass

            except DuplicateKeyError as exception:
                self._col.update(key, {'$set':{channel:data}}, upsert=False,multi=False)
                logger.info("<<<< INERT Queue.. %s_%s_%s | %s | %d", get_data['network'], get_data['station'], get_data['channel'], get_data['st'], self._queue.qsize())
            pass


        pass

