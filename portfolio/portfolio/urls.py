from django.contrib import admin
from django.urls import path

# Import the include function.
from django.urls import include
# In order to access the difference images on the server.
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Already written by Django.  This will take you to the admin portal.
    path('admin/', admin.site.urls),
    # Written by me.  This basically says, for any other path extension, 
    # refer to the mainapp.urls file (which I wrote) to determine which view
    # to render.
    path("", include("mainapp.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# The above concatenation is what we imported static and settings for (to
# access the project images (ie. media).)
