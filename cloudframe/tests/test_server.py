
import grpc
import json
import mock
import os
from six.moves import http_client
import signal
import testtools
import time

from cloudframe.protos import function_pb2
from cloudframe.protos import function_pb2_grpc
from cloudframe.protos import heartbeat_pb2
from cloudframe.protos import heartbeat_pb2_grpc
from cloudframe.server import server


def call_function(opr, tenant, version, res, res_id, req):
    channel = grpc.insecure_channel('[::]:50051')
    req_str = json.dumps(req)
    stub = function_pb2_grpc.GreeterStub(channel)
    response = stub.Call(function_pb2.FunctionRequest(
        opr=opr, tenant=tenant, version=version,
        resource=res, res_id=res_id, req=req_str))
    return response.return_code, json.loads(response.ack)


def call_heartbeat():
    channel = grpc.insecure_channel('[::]:50051')
    stub = heartbeat_pb2_grpc.GreeterStub(channel)
    response = stub.Call(heartbeat_pb2.HbRequest())
    return response.return_code, json.loads(response.ack)


class TestServerServers(testtools.TestCase):

    def setUp(self):
        super(TestServerServers, self).setUp()
        '''
        pid = os.fork()
        if pid == 0:
            server.serve()
            # time.sleep(5)
        else:
            self.stubpid = pid
        '''

    def tearDown(self):
        super(TestServerServers, self).tearDown()
        # os.kill(self.stubpid, signal.SIGKILL)

    def test_function_post(self):
        version = 'v1'
        tenant = 'tenant'
        res = 'res01'
        opr = 'post'
        req_id = '1234'
        req = {'name': 'server 1'}
        ack = {'result': 'OK'}
        rv = call_function(opr, tenant, version, res, req_id, req)
        self.assertEqual(http_client.OK, rv[0])
        self.assertEqual(ack, rv[1])
