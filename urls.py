from django.conf.urls import url
from django.views.generic import ListView

from .views import view_post, new_post, temp_page, like_post, del_post
from .models import BlogPost


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=BlogPost.objects.all().order_by("-posted")[:10],
                                template_name="blog/post_list.html"), name='post_list'),
    url(r'^post/(?P<pk>\d+)$', view_post, name='view_post'),
    url('^new/$', new_post, name='new_post'),
    url('^temp$', temp_page, name='temp_page'),
    url('^post/like_post/$', like_post, name='like_post'),
    url('^post/del_post/$', del_post, name='del_post'),
]
