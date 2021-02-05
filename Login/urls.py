
from django.contrib import admin
from django.urls import path ,include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve


admin.site.site_header = "Holme's Ice Cream"
admin.site.site_title = "Holme's Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Holme's Ice Cream Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    # path('',views.home),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),

    # path('login',include('login.urls')),
    # path('register',include('register.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)