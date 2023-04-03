from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed



class TokenAuthentication(BasePermission):
    def authenticate_token(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        try:
            token = auth_header.split(' ')[1]
            # token_obj = Token.objects.get(key=token)
            return token
        except (IndexError, Token.DoesNotExist):
            return None

    def has_permission(self, request, view):
        auth_header = request.headers.get('Authorization')
        # token = self.authenticate_token(request)
        if auth_header is None:
            raise AuthenticationFailed('Invalid Token')

        # request.user = user
        # request.auth = token
        return bool(auth_header)
