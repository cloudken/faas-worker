
from six.moves import http_client

from cloudframe.protos import heartbeat_pb2
from cloudframe.protos import heartbeat_pb2_grpc


class HbServicer(heartbeat_pb2_grpc.GreeterServicer):

    def Call(self, request, context):
        return heartbeat_pb2.HbReply(return_code=http_client.OK, ack='ok')