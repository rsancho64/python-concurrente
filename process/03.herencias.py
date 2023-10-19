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
        logging.info('este mensaje lo dice un proceso hijo')


if __name__ == '__main__':

    Ps = PSimple(False, 'p-easy')
    Ps.start()
