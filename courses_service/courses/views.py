from rest_framework import generics
from rest_framework.response import Response
from .auth_helper.token_authentication import TokenAuthentication
from .services import CourseService


def get_pagination_url(request, url):
    if not url:
        return url
    url_list = url.split('?')
    url_list[0] = request.build_absolute_uri().split('?')[0]
    return '?'.join(url_list)


class CourseListView(generics.ListAPIView):
    permission_classes = [TokenAuthentication]

    def list(self, request):
        page = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('page_size', 5)
        fields = self.request.query_params.get('fields', 'default_field_list')
        service = CourseService()
        courses = service.get_courses(page=page, page_size=page_size, fields=fields)
        courses['pagination'].update({
            'next': get_pagination_url(request, courses['pagination']['next']),
            'previous': get_pagination_url(request, courses['pagination']['previous'])
        })
        return Response(courses)
