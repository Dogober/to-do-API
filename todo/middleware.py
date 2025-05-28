import logging

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger = logging.getLogger('django.request')
        logger.debug(f'Incoming request: {request.method} {request.get_full_path()}')

        response = self.get_response(request)

        logger.debug(f'Outgoing response: {response.status_code}')

        return response
