
from six.moves import http_client


def post(tenant, req):
    ack = {'status': 'OK'}
    return http_client.OK, ack


def put(tenant, res_id, req):
    ack = {'status': 'OK'}
    return http_client.OK, ack


def get(tenant, res_id):
    ack = {'status': 'OK'}
    return http_client.OK, ack


def delete(tenant, res_id):
    ack = {'status': 'OK'}
    return http_client.OK, ack
