
import json
import logging
from datetime import datetime, timedelta
import os
from six.moves import http_client

from cloudframe.common import utils
from cloudframe.protos import function_pb2
from cloudframe.protos import function_pb2_grpc

LOG = logging.getLogger(__name__)
FAAS_DYING = 1033


class FunctionServicer(function_pb2_grpc.GreeterServicer):

    def Call(self, request, context):
        try:
            LOG.debug('Function call begin, tenant %(tenant)s, resource %(res)s, version %(ver)s, operation %(opr)s.',
                      {'tenant': request.tenant, 'res': request.resource, 'ver': request.version, 'opr': request.opr})
            current = datetime.now()
            start = utils.get_start_time()
            interval = int(os.environ['LIFE_CYCLE']) - 10
            if (current - start) > timedelta(seconds=interval):
                LOG.warn('FaaS deadline is comming, can not accept any call.')
                response = FAAS_DYING, {'result': 'deadline is comming.'}
            else:
                res = utils.get_resource(request.resource, request.version)
                if request.opr == 'post':
                    response = res.post(request.tenant, request.req)
                elif request.opr == 'put':
                    response = res.put(request.tenant, request.res_id, request.req)
                elif request.opr == 'get':
                    response = res.get(request.tenant, request.res_id)
                elif request.opr == 'delete':
                    response = res.delete(request.tenant, request.res_id)
                else:
                    LOG.error('Call %(resource)s, %(ver)s failed, operation %(opr)s is illegal.',
                              {'resource': request.resource, 'ver': request.version, 'opr': request.opr})
                    response = http_client.INTERNAL_SERVER_ERROR, {'result': 'error'}
        except Exception as e:
            LOG.error('Call %(resource)s, %(ver)s failed, error_info: %(error)s',
                      {'resource': request.resource, 'ver': request.version, 'error': e})
            response = http_client.INTERNAL_SERVER_ERROR, {'result': 'error'}

        LOG.debug('Function call resource %(res)s, operation %(opr)s end, return_code %(code)s.',
                  {'res': request.resource, 'opr': request.opr, 'code': response[0]})
        return function_pb2.FunctionReply(return_code=response[0], ack=json.dumps(response[1]))
