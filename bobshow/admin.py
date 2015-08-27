from django.contrib import admin
from bobshow.models import Bob, Place, Comment


admin.site.register(Place)
admin.site.register(Comment)
admin.site.register(Bob)
