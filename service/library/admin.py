from django.contrib import admin

from library.models import Author, Biography, Book, Article
from todo.models import Project, ToDo

admin.site.register(Author)
admin.site.register(Biography)
admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Project)
admin.site.register(ToDo)
