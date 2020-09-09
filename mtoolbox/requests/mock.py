import re

from requests import Response


def build_response(url, filename):
    response = Response()
    response.url = url
    # The file will (should?) be closed in `response.close()`.
    response.raw = open(filename, "rb")
    response.status_code = 200
    return response


def build_response_404(url):
    response = Response()
    response.url = url
    response.status_code = 404
    return response


class RequestsMock:
    def __init__(self):
        # TODO: option for unknown requests
        # => forward, none, raise, 404, ...
        self.rules = []

    def register(self, pattern, filename):
        if isinstance(pattern, str):
            pattern = re.compile(pattern)
            func = lambda m, u, **kwargs: pattern.match(u)
        self.rules.append((func, filename))

    def request(self, method, url, **kwargs):
        for func, filename in self.rules:
            if func(method, url, **kwargs):
                return build_response(url, filename)
        return build_response_404(url)
