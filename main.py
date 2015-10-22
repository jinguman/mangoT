__author__ = 'jman'

import Queue
from generate_trace import GenerateTrace
from insert_trace import InsertTrace
import logging.config
import os
import yaml


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
    num_station = 100
    nsamp = 100

    network = "KG"
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

    it5 = InsertTrace(mongo_name, db_name, queue)
    it5.start()

    it6 = InsertTrace(mongo_name, db_name, queue)
    it6.start()

    it7 = InsertTrace(mongo_name, db_name, queue)
    it7.start()

    it8 = InsertTrace(mongo_name, db_name, queue)
    it8.start()

    it9 = InsertTrace(mongo_name, db_name, queue)
    it9.start()

    it10 = InsertTrace(mongo_name, db_name, queue)
    it10.start()

    pass

if __name__ == "__main__":
    main()
