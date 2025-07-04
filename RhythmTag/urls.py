from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # http://127.0.0.1:8000/admin/ 관리자 페이지 이동
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # http://127.0.0.1:8000/
    path('', include('accounts.urls')),
    # http://127.0.0.1:8000/blog/
    path('blog/', include('blog.urls')),
]

# CKEditor에서 사진을 올리기 위한 코드
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)