from django.contrib import admin
from bobshow.models import Bob, Place, Comment, Photo


admin.site.register(Place)
admin.site.register(Comment)
admin.site.register(Bob)
admin.site.register(Photo)
