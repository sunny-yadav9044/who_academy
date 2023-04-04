import requests


class AuthService:
    def __init__(self, token):
        # we are using reverse proxy that using container name for communication
        # self.base_url = 'http://localhost:8001'
        self.base_url = 'http://encore_assignment-nginx-1'
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.token}'
        })

    def validate_token(self):
        url = f'{self.base_url}/auth/token/validate/'
        response = self.session.post(url)
        # response.raise_for_status()
        return response.json()
