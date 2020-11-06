from .consumer import Consumer
from .endpoints import endpoints, id_name_listing
import argparse

parser = argparse.ArgumentParser(description='MTA data consumer', 
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--endpoint_id', 
                    choices = endpoints.keys(), 
                    help= id_name_listing,
                    required=True)
parser.add_argument('--repeat', type=int, default=-1, help='Number of times to request data')
parser.add_argument('--interval', type=int, default=30, help='Interval (in seconds) between requests')

args = parser.parse_args()

Consumer(args.endpoint_id, 
         args.repeat, 
         args.interval).consume()
