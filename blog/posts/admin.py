from django.contrib import admin

from posts.models import IsRead, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
    )
    readonly_fields = ('pub_date',)


class IsReadAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'post',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(IsRead, IsReadAdmin)
