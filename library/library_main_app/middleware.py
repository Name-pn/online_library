import logging


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('django')

    def __call__(self, request):
        response = self.get_response(request)

        self.logger.info(
            f'Method: {request.method}, '
            f'Path: {request.path}, '
            f'Status Code: {response.status_code}, '
        )

        return response
