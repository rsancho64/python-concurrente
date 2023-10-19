import os
import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='PID: %(process)s ~ %(processName)s: %(message)s')


if __name__ == '__main__':
    current_process = multiprocessing.current_process()
    pid = current_process.pid
    name = current_process.name

    logging.info(f'P now: {current_process}')
    logging.info(f'  PID: {pid}')
    logging.info(f'P.nom: {name}')
