
import json
import logging
from six.moves import http_client

from cloudframe.common.utils import get_resource
from cloudframe.protos import function_pb2
from cloudframe.protos import function_pb2_grpc

LOG = logging.getLogger(__name__)


class FunctionServicer(function_pb2_grpc.GreeterServicer):

    def Call(self, request, context):
        try:
            res = get_resource(request.resource, request.version)
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

        return function_pb2.FunctionReply(return_code=response[0], ack=json.dumps(response[1]))
