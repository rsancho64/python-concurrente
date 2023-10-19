import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
    # format='PID: %(process)s ~ %(processName)s: %(message)s'
)


class PSimple(multiprocessing.Process):
    def __init__(self, daemon, name):
        multiprocessing.Process.__init__(self, daemon=daemon, name=name)

    def run(self):
        time.sleep(3)
        logging.info('este mensaje de despedida lo da un hijo')


if __name__ == '__main__':

    logging.info('COMIENZO...')

    Ps = PSimple(False, 'p-easy')
    Ps.start()

    logging.info('...FIN')
