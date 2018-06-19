
import testtools

from cloudframe.cmd import worker
from cloudframe.common.rpc import MyRPC
# from cloudframe.protos import function_pb2
# from cloudframe.protos import function_pb2_grpc
# from cloudframe.protos import heartbeat_pb2
# from cloudframe.protos import heartbeat_pb2_grpc
# from cloudframe.service.function import FunctionServicer
# from cloudframe.service.heartbeat import HbServicer


class RpcTestCase(testtools.TestCase):

    def setUp(self):
        super(RpcTestCase, self).setUp()
        host = {}
        host['host_ip'] = '[::]'
        host['host_port'] = worker.HOST_PORT
        self.rpc = MyRPC(host)

    def tearDown(self):
        super(RpcTestCase, self).tearDown()

    '''
    @classmethod
    def _start_server(cls):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        heartbeat_pb2_grpc.add_GreeterServicer_to_server(HbServicer(), server)
        function_pb2_grpc.add_GreeterServicer_to_server(FunctionServicer(), server)
        host = '[::]:' + str(worker.HOST_PORT)
        server.add_insecure_port(host)
        server.start()
        time.sleep(10)
    '''
