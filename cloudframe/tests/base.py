
import testtools

from cloudframe.cmd import worker
from cloudframe.common.rpc import MyRPC


class RpcTestCase(testtools.TestCase):

    def setUp(self):
        super(RpcTestCase, self).setUp()
        host = {}
        host['host_ip'] = '[::]'
        host['host_port'] = worker.HOST_PORT
        self.rpc = MyRPC(host)

    def tearDown(self):
        super(RpcTestCase, self).tearDown()
