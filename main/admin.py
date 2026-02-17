from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Article, Tag, Comment, Vote


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id', 'email', 'username', 'first_name', 'last_name',
        'is_staff', 'is_active', 'is_superuser', 'date_joined', 'last_login'
    )
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name')}),
        ('دسترسی‌ها', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('تاریخ‌ها', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'content', 'uvotec', 'dvotec',
        'is_open', 'published'
    )
    list_filter = ('is_open', 'published')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)
    raw_id_fields = ('author',)
    fieldsets = (
        (None, {'fields': ('title', 'author', 'content')}),
        ('وضعیت', {'fields': ('uvotec', 'dvotec', 'is_open', 'published')}),
        ('تگ‌ها', {'fields': ('tags',)}),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'author', 'content')
    list_filter = ('article',)
    search_fields = ('content',)
    raw_id_fields = ('author', 'article')
    fields = ('article', 'author', 'content')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'voter', 'type')
    list_filter = ('type',)
    raw_id_fields = ('voter', 'article')
    fields = ('article', 'voter', 'type')
