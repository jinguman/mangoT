__author__ = 'jman'

import Queue
from generate_trace import GenerateTrace
from insert_trace import InsertTrace
import logging.config
import os
import yaml
from datetime import datetime, timedelta

def main():

    #variables
    mongo_name = "localhost"
    db_name = "trace"

    #log
    logger = logging.getLogger('mangoT')
    loggingConfigPath = 'logging.yaml'
    if os.path.exists(loggingConfigPath):
        with open(loggingConfigPath, 'rt') as f:
            loggingConfig = yaml.load(f.read())
            logging.config.dictConfig(loggingConfig)
    else:
        logger.basicConfig(level=logging.INFO)


    queue = Queue.Queue()
    gt = GenerateTrace(queue)


    #gt.set_buffer("test1",100)

    #station number
    num_station = 1
    nsamp = 1000

    network = "KA"
    for i in range(num_station):
        station = "AAA" + str(i)
        gt.set_buffer(network,station, nsamp)
    gt.start()


    it = InsertTrace(mongo_name, db_name, queue)
    it.start()

    it2 = InsertTrace(mongo_name, db_name, queue)
    it2.start()

    it3 = InsertTrace(mongo_name, db_name, queue)
    it3.start()

    it4 = InsertTrace(mongo_name, db_name, queue)
    it4.start()

    it5 = InsertTrace(mongo_name, db_name, queue)
    it5.start()


    gt.join()
    it.join()
    it2.join()
    it3.join()
    it4.join()
    it5.join()

    pass

if __name__ == "__main__":
    main()
