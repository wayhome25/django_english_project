# mysite/urls.py
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from study import views as study_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup', study_views.signup, name='signup'),
    url(r'^', include('study.urls')),
]

if settings.DEBUG: # setting.py의 DEBUG = True인 경우
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
