import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
    # format='PID: %(process)s ~ %(processName)s: %(message)s'
    )

def newP():
    logging.info('soy nuevo')

    time.sleep(3)

    logging.info('termino bien.')  # no se ve


if __name__ == '__main__':

    logging.info('COMIENZO...')
    time.sleep(1)

    P = multiprocessing.Process(target=newP)

    P.start()

    # time.sleep(5)  # TOGGLE THIS COMMENT

    if P.is_alive():
        P.terminate()
        logging.info('hijo señalado y terminado')

    logging.info('...FIN')
