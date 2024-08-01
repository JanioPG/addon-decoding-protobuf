import logging
import appanalytics_pb2
from mitmproxy import contentviews
from mitmproxy import flow
from mitmproxy import http
from mitmproxy.addonmanager import Loader
from dataclasses import dataclass, field


@dataclass
class MitmproxyUtils:
    ENDPOINT_ANDROID: str
    ENDPOINT_IOS: str
    VIEW_NAME: str
    VIEW_DESCRIPTION: str
    TAG: str
    _error_message: str = field(init=False, repr=False)
    _info_request_GA4: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._error_message = f"{self.TAG} => protobuf decoding error:"
        self._info_request_GA4 = f"{self.TAG} => a request has been made to GA4. url:"


proxy_utils = MitmproxyUtils(
    ENDPOINT_ANDROID='app-measurement.com/a',
    ENDPOINT_IOS='app-analytics-services-att.com/a',
    VIEW_NAME="protobuf to GA4",
    VIEW_DESCRIPTION="protobuf decoded to GA4",
    TAG="APP_TRACKING"
)


class ViewProtobuf(contentviews.View):
    name = proxy_utils.VIEW_NAME

    def __call__(
        self,
        data: bytes,
        *,
        content_type: str | None = None,
        flow: flow.Flow | None = None,
        http_message: http.Message | None = None,
        **unknown_metadata,
    ) -> contentviews.TViewResult:
        url = flow.request.url
        try:
            if (proxy_utils.ENDPOINT_ANDROID in url) or (proxy_utils.ENDPOINT_IOS in url):
                batch = appanalytics_pb2.Batch()
                batch.ParseFromString(data)
                return proxy_utils.VIEW_DESCRIPTION, contentviews.format_text(repr(batch))
            
        except Exception as e:
            logging.info(f"{proxy_utils._error_message} {e}")
            

    def render_priority(
        self,
        data: bytes,
        *,
        content_type: str | None = None,
        flow: flow.Flow | None = None,
        http_message: http.Message | None = None,
        **unknown_metadata,
    ) -> float:
        url = flow.request.url
        if (proxy_utils.ENDPOINT_ANDROID in url) or (proxy_utils.ENDPOINT_IOS in url):
            return 1
        else:
            return 0


view = ViewProtobuf()


def load(loader: Loader):
    contentviews.add(view)


def done():
    contentviews.remove(view)


def request(flow):
    url = str(flow.request.url)
    if (proxy_utils.ENDPOINT_ANDROID in url) or (proxy_utils.ENDPOINT_IOS in url):
        logging.info(f"{proxy_utils._info_request_GA4} {url}")
