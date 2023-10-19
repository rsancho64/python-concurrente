import os
import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='PID: %(process)s ~ %(processName)s: %(message)s')


def newP(mensaje):
    logging.info('soy nuevo')
    time.sleep(3)
    logging.info(mensaje)
    logging.info('termino.')


if __name__ == '__main__':

    logging.info('COMIENZO...')
    time.sleep(1)

    P = multiprocessing.Process(target=newP, name='ChildProcess',
                                kwargs={'mensaje': 'i feel good'})
    P.start()

    P.join()

    logging.info('...FIN')
