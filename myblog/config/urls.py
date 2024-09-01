from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import MainPageView
from django.conf.urls import handler404
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main_page'),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]


handler404 = 'blog.views.custom_page_not_found_view'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)