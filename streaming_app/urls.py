from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('streaming_page', views.streaming_page, name='streaming_page'),
    path('streaming_index/<int:pk>', views.streaming_index, name='streaming_index'),
    url(r'^streaming/$', TemplateView.as_view(template_name="streaming/saved_resource.html"), name="saved_resource"),
    url(r'^streaming/$', TemplateView.as_view(template_name="streaming/saved_resource(1).html"), name="saved_resource(1)"),
    url(r'^streaming/$', TemplateView.as_view(template_name="streaming/bc-v3.min.html"), name="bc-v3"),
    url(r'^user/packages/$', TemplateView.as_view(template_name="streaming/aesthetic/index.html"), name="user_packages"),
    path('login_stream', views.login_user, name="login-stream"),
    path('logout_stream', views.logout_streaming, name="logout-stream"),
    path('register_stream/<str:pk>', views.register_streaming, name='register_stream'),
    path('streaming_plateform', views.streaming_plateform, name='streaming_plateform'),
    path('stream_main', views.stream_main, name="stream_main"),
    path('live_main', views.live_main, name="live_main"),
    path('live_stream/<str:id>', views.live_stream, name="live_stream"),
    path('user/profile', views.profil_stream, name='profil-stream')
]