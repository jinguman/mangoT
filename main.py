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
    gt2 = GenerateTrace(queue)
    gt3 = GenerateTrace(queue)
    gt4 = GenerateTrace(queue)
    gt5 = GenerateTrace(queue)
    gt6 = GenerateTrace(queue)
    gt7 = GenerateTrace(queue)

    #gt.set_buffer("test1",100)

    #station number
    num_station = 50
    nsamp = 100

    network = "KA"
    for i in range(num_station):
        station = "AAA" + str(i)
        gt.set_buffer(network,station, nsamp)
    gt.start()

    network = "KB"
    for i in range(num_station):
        station = "BBB" + str(i)
        gt2.set_buffer(network,station, nsamp)
    gt2.start()

    network = "KC"
    for i in range(num_station):
        station = "CCC" + str(i)
        gt3.set_buffer(network,station, nsamp)
    gt3.start()

    network = "KD"
    for i in range(num_station):
        station = "DDD" + str(i)
        gt4.set_buffer(network,station, nsamp)
    gt4.start()

    network = "KE"
    for i in range(num_station):
        station = "EEE" + str(i)
        gt5.set_buffer(network,station, nsamp)
    gt5.start()

    network = "KF"
    for i in range(num_station):
        station = "FFF" + str(i)
        gt6.set_buffer(network,station, nsamp)
    gt6.start()

    network = "KG"
    for i in range(num_station):
        station = "GGG" + str(i)
        gt7.set_buffer(network,station, nsamp)
    gt7.start()


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
