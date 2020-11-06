import tributary as ts
import aiofiles
import json as JSON
from .protobuf import gtfs_realtime_pb2
import httpx
import asyncio
from google.protobuf.json_format import MessageToJson, MessageToDict


def FileSink(node, filename=''):
    async def _file(data):
        async with aiofiles.open(filename, mode='a') as fp:
            await fp.write(JSON.dumps(data))
            await fp.write('\n')
        return data
    ret = ts.Node(foo=_file, name='FileOutput', inputs=1)
    node >> ret
    return ret


class HTTPProtobufDecode(ts.Foo):
    def __init__(self, url, headers, repeat=1, interval=1):
        async def _decode(url=url, headers=headers):
            feed = gtfs_realtime_pb2.FeedMessage()
            count = 0 if repeat >= 0 else float('-inf')
            while count < repeat:
                async with httpx.AsyncClient() as client:
                    response = await client.get(url=url, headers=headers)
                    feed.ParseFromString(response.content)
                    msg = MessageToDict(feed)
                    yield msg
                if interval:
                    await asyncio.sleep(interval)
                if repeat >= 0:
                    count += 1
        super().__init__(foo=_decode)
        self._name = 'Protobuf'