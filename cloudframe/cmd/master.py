
import logging
import os
import time

os.environ.setdefault('LOG_LEVEL', 'DEBUG')
os.environ.setdefault('LIFE_CYCLE', 30)
loglevel_map = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARN': logging.WARN,
    'ERROR': logging.ERROR,
}
logging.basicConfig(
    level=loglevel_map[os.environ['LOG_LEVEL']],
    format='%(asctime)s.%(msecs)03d %(filename)s[line:%(lineno)d]'
           ' %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='/var/log/cloudframe/faas-master.log',
    filemode='a')


def main():
    LOG = logging.getLogger(__name__)
    LOG.error("Starting...")
    interval = int(os.environ['LIFE_CYCLE'])
    time.sleep(interval)
    LOG.error("end.")
    os.system('pkill -f faas-worker')
    exit(0)


if __name__ == "__main__":
    main()
