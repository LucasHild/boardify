from flask import Response


class _EndpointAction(object):
    def __init__(self, response):
        self.action = None
        self.response = Response(status=200, headers={}, response=response)

    def __call__(self, *args):
        return self.response
