from django.urls import path 
from .views import test_api, test_json_api, test_html_page

urlpatterns = [
    # path( "route-name", views, name="name of the route" )
    # name is used for redirection purpose 
    path("test-api/", test_api, name="test_api"),
    path("test-json-api/", test_json_api, name="test_json_api"),
    path("test-html-page/", test_html_page, name="test_html_page"),
    
]


