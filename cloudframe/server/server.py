"""A gRPC server servicing both Heartbeat and Function RPCs."""

from concurrent import futures
# import time

import grpc

from cloudframe.protos import heartbeat_pb2_grpc
from cloudframe.protos import function_pb2_grpc
from cloudframe.server.function import FunctionServicer
from cloudframe.server.heartbeat import HbServicer

MAX_WORKERS = 10


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    # heartbeat_pb2_grpc.add_GreeterServicer_to_server(HbServicer(), server)
    function_pb2_grpc.add_GreeterServicer_to_server(FunctionServicer(), server)
    server.add_insecure_port('[::]:50051')
    # server.add_insecure_port('0.0.0.0:50051')
    server.start()
