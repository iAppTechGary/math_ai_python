# yourapp/middleware.py

from django.http import JsonResponse
from django.conf import settings

class StaticAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):


        auth_header = request.headers.get("security_token")

        if not auth_header:
            return JsonResponse({"error": "Missing Authorization header."}, status=401)

        try:
            prefix, token = auth_header.strip().split(" ")
            if prefix.lower() != "token":
                raise ValueError("Invalid auth prefix")
        except ValueError:
            return JsonResponse({"error": "Invalid Authorization header format."}, status=401)

        if token != settings.STATIC_AUTH_TOKEN:
            return JsonResponse({"error": "Invalid token."}, status=401)

        return self.get_response(request)
