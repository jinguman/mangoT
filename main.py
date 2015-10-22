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
    gt8 = GenerateTrace(queue)
    gt9 = GenerateTrace(queue)
    gt10 = GenerateTrace(queue)
    gt11 = GenerateTrace(queue)
    gt12 = GenerateTrace(queue)
    gt13 = GenerateTrace(queue)
    gt14 = GenerateTrace(queue)
    gt15 = GenerateTrace(queue)
    gt16 = GenerateTrace(queue)
    gt17 = GenerateTrace(queue)
    gt18 = GenerateTrace(queue)
    gt19 = GenerateTrace(queue)
    gt20 = GenerateTrace(queue)
    gt21 = GenerateTrace(queue)
    gt22 = GenerateTrace(queue)
    gt23 = GenerateTrace(queue)
    gt24 = GenerateTrace(queue)
    gt25 = GenerateTrace(queue)

    #gt.set_buffer("test1",100)

    #station number
    num_station = 20
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

    network = "KH"
    for i in range(num_station):
        station = "HHH" + str(i)
        gt8.set_buffer(network,station, nsamp)
    gt8.start()

    network = "KI"
    for i in range(num_station):
        station = "III" + str(i)
        gt9.set_buffer(network,station, nsamp)
    gt9.start()

    network = "KJ"
    for i in range(num_station):
        station = "JJJ" + str(i)
        gt10.set_buffer(network,station, nsamp)
    gt10.start()

    network = "KK"
    for i in range(num_station):
        station = "KKK" + str(i)
        gt11.set_buffer(network,station, nsamp)
    gt11.start()

    network = "KL"
    for i in range(num_station):
        station = "LLL" + str(i)
        gt12.set_buffer(network,station, nsamp)
    gt12.start()

    network = "KM"
    for i in range(num_station):
        station = "MMM" + str(i)
        gt13.set_buffer(network,station, nsamp)
    gt13.start()

    network = "KN"
    for i in range(num_station):
        station = "NNN" + str(i)
        gt14.set_buffer(network,station, nsamp)
    gt14.start()

    network = "KO"
    for i in range(num_station):
        station = "OOO" + str(i)
        gt15.set_buffer(network,station, nsamp)
    gt15.start()

    network = "KP"
    for i in range(num_station):
        station = "PPP" + str(i)
        gt16.set_buffer(network,station, nsamp)
    gt16.start()

    network = "KQ"
    for i in range(num_station):
        station = "QQQ" + str(i)
        gt17.set_buffer(network,station, nsamp)
    gt17.start()

    network = "KR"
    for i in range(num_station):
        station = "RRR" + str(i)
        gt18.set_buffer(network,station, nsamp)
    gt18.start()

    network = "KS"
    for i in range(num_station):
        station = "SSS" + str(i)
        gt19.set_buffer(network,station, nsamp)
    gt19.start()

    network = "KT"
    for i in range(num_station):
        station = "TTT" + str(i)
        gt20.set_buffer(network,station, nsamp)
    gt20.start()

    network = "KU"
    for i in range(num_station):
        station = "UUU" + str(i)
        gt21.set_buffer(network,station, nsamp)
    gt21.start()

    network = "KV"
    for i in range(num_station):
        station = "VVV" + str(i)
        gt22.set_buffer(network,station, nsamp)
    gt22.start()

    network = "KW"
    for i in range(num_station):
        station = "WWW" + str(i)
        gt23.set_buffer(network,station, nsamp)
    gt23.start()

    network = "KX"
    for i in range(num_station):
        station = "XXX" + str(i)
        gt24.set_buffer(network,station, nsamp)
    gt24.start()

    network = "KY"
    for i in range(num_station):
        station = "YYY" + str(i)
        gt25.set_buffer(network,station, nsamp)
    gt25.start()




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
