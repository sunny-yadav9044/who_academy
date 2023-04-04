from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from ..services import AuthService



class TokenAuthentication(BasePermission):
    def authenticate_token(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        try:
            token = auth_header.split(' ')[1]
            service = AuthService(token)
            token = service.validate_token()
            return token
        except (IndexError) as e:
            return None

    def has_permission(self, request, view):
        token = self.authenticate_token(request)
        if not token:
            raise AuthenticationFailed('Invalid Token')
        if 'error' in token:
            raise AuthenticationFailed(token['error'])
        request.auth = token
        return True
