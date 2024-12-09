class BreadcrumbsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Initialisez avec un breadcrumb de base
        request.breadcrumbs = [{"name": "Home", "url": "/"}]
        response = self.get_response(request)
        return response
