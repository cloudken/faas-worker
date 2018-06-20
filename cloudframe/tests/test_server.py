
# import mock
import json
from six.moves import http_client

from cloudframe.tests import base


class TestServerServers(base.RpcTestCase):

    def setUp(self):
        super(TestServerServers, self).setUp()

    def test_function_post(self):
        version = 'v1'
        tenant = 'tenant'
        res = 'res01'
        opr = 'post'
        req_id = '1234'
        req = {'name': 'server 1'}
        ack = {'status': 'OK'}
        rv = self.rpc.call_function(opr, tenant, version, res, req_id, req)
        self.assertEqual(http_client.OK, rv[0])
        self.assertEqual(ack, json.loads(rv[1]))

    def test_function_no_res(self):
        version = 'v1'
        tenant = 'tenant'
        res = 'abc_not_exist'
        opr = 'post'
        req_id = '1234'
        req = {'name': 'server 1'}
        ack = {'result': 'error'}
        rv = self.rpc.call_function(opr, tenant, version, res, req_id, req)
        self.assertEqual(http_client.INTERNAL_SERVER_ERROR, rv[0])
        self.assertEqual(ack, json.loads(rv[1]))

    def test_function_opr_error(self):
        version = 'v1'
        tenant = 'tenant'
        res = 'res01'
        opr = 'wrong_opr'
        req_id = '1234'
        req = {'name': 'server 1'}
        ack = {'result': 'error'}
        rv = self.rpc.call_function(opr, tenant, version, res, req_id, req)
        self.assertEqual(http_client.INTERNAL_SERVER_ERROR, rv[0])
        self.assertEqual(ack, json.loads(rv[1]))

    def test_heartbeat(self):
        ack = {'result': 'ok'}
        rv = self.rpc.call_heartbeat()
        self.assertEqual(http_client.OK, rv[0])
        self.assertEqual(ack, json.loads(rv[1]))
