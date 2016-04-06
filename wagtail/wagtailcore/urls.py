from django.conf.urls import url
from wagtail.wagtailcore import views
from wagtail.wagtailcore.utils import WAGTAIL_APPEND_SLASH


# If WAGTAIL_APPEND_SLASH is False, allow Wagtail to serve pages on URLs
# with and without trailing slahes
if WAGTAIL_APPEND_SLASH:
    serve_pattern = r'^((?:[\w\-]+/)*)$'
else:
    serve_pattern = r'^(.*)$'


urlpatterns = [
    url(r'^_util/authenticate_with_password/(\d+)/(\d+)/$', views.authenticate_with_password,
        name='wagtailcore_authenticate_with_password'),

    # Front-end page views are handled through Wagtail's core.views.serve mechanism.
    # Here we match a (possibly empty) list of path segments, each followed by
    # a '/'. If a trailing slash is not present, we leave CommonMiddleware to
    # handle it as usual (i.e. redirect it to the trailing slash version if
    # settings.APPEND_SLASH is True)
    url(serve_pattern, views.serve, name='wagtail_serve')
]
