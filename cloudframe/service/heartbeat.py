
from datetime import datetime, timedelta
import json
import os
from six.moves import http_client

from cloudframe.common import utils
from cloudframe.protos import heartbeat_pb2
from cloudframe.protos import heartbeat_pb2_grpc


class HbServicer(heartbeat_pb2_grpc.GreeterServicer):

    def Call(self, request, context):
        current = datetime.now()
        start = utils.get_start_time()
        interval = int(os.environ['LIFE_CYCLE']) - 10
        if (current - start) < timedelta(seconds=interval):
            response = {'result': 'ok'}
            code = http_client.OK
        else:
            response = {'result': 'deadline is comming.'}
            code = http_client.FORBIDDEN
        return heartbeat_pb2.HbReply(return_code=code, ack=json.dumps(response))
