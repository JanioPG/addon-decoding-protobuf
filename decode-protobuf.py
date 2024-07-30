import logging
import appanalytics_pb2
from mitmproxy.contentviews.protobuf import ViewProtobuf

def request(flow):
    url = str(flow.request.url)
    data = flow.request.content

    try:
        if ('app-measurement.com/a' in url) or ('app-analytics-services-att.com/a' in url):
            TAG = "GA4DEBUG"
            batch = appanalytics_pb2.Batch()
            batch.ParseFromString(data)

            logging.info(f"{TAG} => url: {url}")
            logging.info(f"{TAG} => data: \n{repr(batch)}")

    except Exception as e:
        logging.info(f"{TAG} => decoding error: {e}")
