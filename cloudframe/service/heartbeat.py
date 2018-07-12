
from datetime import datetime, timedelta
import json
import logging
import os
from six.moves import http_client

from cloudframe.common import utils
from cloudframe.protos import heartbeat_pb2
from cloudframe.protos import heartbeat_pb2_grpc

LOG = logging.getLogger(__name__)
FAAS_DYING = 1033


class HbServicer(heartbeat_pb2_grpc.GreeterServicer):

    def Call(self, request, context):
        LOG.debug('Heartbeat call begin...')
        current = datetime.now()
        start = utils.get_start_time()
        interval = int(os.environ['LIFE_CYCLE']) - 10
        if (current - start) < timedelta(seconds=interval):
            response = {'result': 'ok'}
            code = http_client.OK
        else:
            LOG.warn('FaaS deadline is comming, can not accept any call.')
            response = {'result': 'deadline is comming.'}
            code = FAAS_DYING
        LOG.debug('Heartbeat call end, return_code %(code)s.', {'code': code})
        return heartbeat_pb2.HbReply(return_code=code, ack=json.dumps(response))
