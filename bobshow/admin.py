from django.contrib import admin
from bobshow.models import Bob, Place, Comment, Photo


admin.site.register(Place)
admin.site.register(Comment)
admin.site.register(Photo)


@admin.register(Bob)
class BobAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'content')
    search_fields = ('name', 'place__name')