import requests


class CourseService:
    def __init__(self):
        self.url = 'https://courses.edx.org/api/courses/v1/courses/'

    def get_courses(self, page=1, page_size=5, fields=None):
        params = {'page': page, 'page_size': page_size}

        response = requests.get(self.url, params=params)
        response.raise_for_status()

        data = response.json()

        if fields:
            data['results'] = [
                {field: course.get(field) for field in fields.split(',')} for course in data['results']
            ]
        return data
