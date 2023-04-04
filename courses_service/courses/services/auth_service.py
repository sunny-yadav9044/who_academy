import requests


class AuthService:
    def __init__(self, token):
        self.base_url = 'http://localhost:8001'
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
