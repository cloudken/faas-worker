# -*- encoding: utf-8 -*-
#
# Copyright 2013 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
The Framework Service
"""

from concurrent import futures
# from gevent import monkey
import grpc
import logging
import os
import time

from cloudframe.common import utils
from cloudframe.protos import heartbeat_pb2_grpc
from cloudframe.protos import function_pb2_grpc
from cloudframe.service.function import FunctionServicer
from cloudframe.service.heartbeat import HbServicer

# from cloudframe.common import job


_ONE_DAY_IN_SECONDS = 60 * 60 * 24
LIFE_CYCLE = 60 * 60
MAX_WORKERS = 10
HOST_PORT = 50051

os.environ.setdefault('LOG_LEVEL', 'DEBUG')
os.environ.setdefault('LIFE_CYCLE', '30')
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
    filename='/var/log/cloudframe/faas-worker.log',
    filemode='a')


def main():
    # monkey.patch_all()
    LOG = logging.getLogger(__name__)
    LOG.debug("Starting...")
    utils.set_start_time()
    # job.start_worker(5)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    heartbeat_pb2_grpc.add_GreeterServicer_to_server(HbServicer(), server)
    function_pb2_grpc.add_GreeterServicer_to_server(FunctionServicer(), server)
    host = '[::]:' + str(HOST_PORT)
    server.add_insecure_port(host)
    server.start()
    try:
        while True:
            time.sleep(LIFE_CYCLE)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
