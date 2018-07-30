from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/', include('article.urls')),
    url(r'^list/', include('article.urls'))
]
