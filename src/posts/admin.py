from django.contrib import admin
from django.contrib.auth import get_user_model

from posts.models import IsRead, Post


User = get_user_model()


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'is_read',
    )
    readonly_fields = ('pub_date',)

    def get_queryset(self, request):
        """Метод для получения объекта класса request."""
        new_queryset = super(PostAdmin, self).get_queryset(request)
        self.request = request
        return new_queryset

    @admin.display(description='Прочитан')
    def is_read(self, obj):
        """Метод для отображения статуса поста 'Прочитан/не прочитан' в админ-панели."""
        if obj.is_read.filter(user=self.request.user):
            return 'Да'
        return 'Нет'


class IsReadAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'post',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(IsRead, IsReadAdmin)
