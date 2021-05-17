import grpc

from api import divider_pb2
from api import divider_pb2_grpc


def run(x: int, y: int, channel: grpc.Channel = None):

    if not channel:
        channel = grpc.insecure_channel('localhost:8191')

    with channel as c:
        client = divider_pb2_grpc.DividerStub(channel=c)
        resp: divider_pb2.DivideResponse = client.Divide(divider_pb2.DivideRequest(x=x, y=y))

    print(f'Response: {resp}')
