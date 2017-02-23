from django.contrib import admin
from bobshow.models import Bob, Place, Comment, Image, Date

admin.site.register(Place)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Date)


@admin.register(Bob)
class BobAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'score')
    search_fields = ('name', 'place__name', 'score')
