import json
import logging
from urllib.request import Request, urlopen
from urllib.error import URLError

logger = logging.getLogger(__name__)

LOGSTASH_URL = "http://localhost:8080"


def send_event(
    event: str,
    performance_id: int,
    request_method: str,
    endpoint: str) -> None:
    payload = {
        "event": event,
        "performance_id": performance_id,
        "level": "INFO",
        "request_method": request_method,
        "endpoint": endpoint
    }

    data = json.dumps(payload).encode("utf-8")

    request = Request(
        url=LOGSTASH_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(request, timeout=0.5) as response:
            response.read()
    except (URLError, OSError, TimeoutError):
        logger.warning("Não foi possível enviar o evento ao Logstash")