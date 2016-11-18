class AppendSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path_info[-1] != '/':
            request.path_info += '/'
        response = self.get_response(request)
        return response
