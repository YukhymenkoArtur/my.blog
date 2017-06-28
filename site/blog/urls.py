# from django.conf.urls import url

# from .views import index, detail, create

# urlpatterns = [
#     url(r'^$', index, name='index'),
#     url(r'^detail/(?P<item_id>\d+)/$', detail, name='detail'),
#     url(r'^create/', create, name='create')
# ]


from django.conf.urls import url
from .views import index, detail, create, post_edit, deleted

urlpatterns = [
	url(r"^$", index, name="index"),
	url(r"^detail/(?P<item_id>\d+)/$", detail, name="detail"),
	url(r"^create/", create, name="create"),
	url(r"^post/(?P<item_id>[0-9]+)/edit/$", post_edit, name="post_edit"),
	url(r"^deleted/(?P<pk>[0-9]+)/$", deleted, name="deleted"),
]