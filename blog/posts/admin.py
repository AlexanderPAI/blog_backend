from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
    )
    readonly_fields = ('pub_date',)


admin.site.register(Post, PostAdmin)
