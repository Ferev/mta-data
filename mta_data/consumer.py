import tributary as ts
from .nodes import HTTPProtobufDecode, FileSink
from .endpoints import endpoints as ENDPOINTS_MAP
import os


class Consumer:
    DATA_PATH = os.path.join(os.path.abspath(os.getcwd()), 'data')
    def __init__(self, endpoint_id, repeat=-1, interval=30):
        self.api_key = os.environ.get('MTA_DATA_API_KEY')
        self.url = ENDPOINTS_MAP[endpoint_id][1]
        self.filename = os.path.join(Consumer.DATA_PATH, 
                                     self._format_endpoint_name(ENDPOINTS_MAP[endpoint_id][0]))
        self.repeat = repeat
        self.interval = interval

    def consume(self):
        graph = self.construct_graph()
        ts.run(graph)

    def _format_endpoint_name(self, name):
        name = name.replace(',', ' ').replace('/', ' ').replace('-', ' ').replace(' ', '_')
        name += '.json'
        return name

    def construct_graph(self):
        headers = {"x-api-key": self.api_key}
        node = HTTPProtobufDecode(url=self.url, headers=headers, repeat=self.repeat, interval=self.interval)
        out = FileSink(node=node, filename=self.filename)
        return out
        