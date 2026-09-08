from prometheus_client import Counter, Histogram

http_requests_total = Counter(
    "http_requests_total",
    "Total de Requisições HTTP",
    ["method", "endpoint", "status_code"]
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "Duração das Requisições HTTP em Segundos",
    ["method", "endpoint"]
)