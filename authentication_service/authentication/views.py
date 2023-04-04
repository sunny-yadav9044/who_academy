from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from rest_framework import status

from .common.utils import generate_token, validate_token


def get_token_from_request(request):
    auth_header = get_authorization_header(request)
    if not auth_header:
        raise AuthenticationFailed('Authorization header is missing')
    auth_header = auth_header.decode('utf-8').split()
    if len(auth_header) != 2 or auth_header[0].lower() != 'bearer':
        raise AuthenticationFailed('Invalid authorization header format')
    token = auth_header[1]
    return token


class TokenGenerateView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        token = generate_token()
        if token:
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Failed to generate token.'},
                status=status.HTTP_400_BAD_REQUEST
            )


class TokenValidateView(APIView):
    def post(self, request):
        token = validate_token(get_token_from_request(request))
        if token:
            return Response({'status': 'Token is valid.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)
