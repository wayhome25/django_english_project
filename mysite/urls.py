# mysite/urls.py
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from study import views as study_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('study.urls')),
    url(r'^accounts/signup/$', study_views.CreateUserView.as_view(), name='signup'),
    url(r'^accounts/signup/done$', study_views.RegisteredView.as_view(), name='create_user_done'),
]

if settings.DEBUG: # setting.py의 DEBUG = True인 경우
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
