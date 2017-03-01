from django.conf.urls import url
from django.contrib import admin
from posts import views as views_post
from sidepages import views as views_side
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views_post.home, name="home"),
    url(r'^about/', views_side.about, name="about"),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views_post.post_detail, name="post_detail")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
