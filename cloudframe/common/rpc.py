
import grpc
import json

from cloudframe.protos import function_pb2
from cloudframe.protos import function_pb2_grpc
from cloudframe.protos import heartbeat_pb2
from cloudframe.protos import heartbeat_pb2_grpc

class MyRPC(object):
    def __init__(self, worker_data):
        self.host = worker_data['host_ip'] + ':' + worker_data['host_port']

    def call_function(self, tenant, req, res_id):
        req_str = json.dumps(req)
        channel = grpc.insecure_channel(self.host)
        stub = function_pb2_grpc.GreeterStub(channel)
        response = stub.Call(function_pb2.FunctionRequest(tenant=tenant, req=req_str, res_id=res_id))
        return response.return_code, json.loads(response.ack)

    def call_heartbeat(self):
        channel = grpc.insecure_channel(self.host)
        stub = heartbeat_pb2_grpc.HeartbeatStub(channel)
        response = stub.Call(heartbeat_pb2.Data())
        return response