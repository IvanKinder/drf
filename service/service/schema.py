import graphene
from graphene_django import DjangoObjectType
from library.models import Book, Author
from todo.models import ToDo, Project
from django.contrib.auth.models import User


class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        uuid = graphene.UUID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, birthday_year, uuid):
        author = Author.objects.get(uuid=uuid)
        author.birthday_year = birthday_year
        author.save()
        return AuthorMutation(author=author)


class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    author_by_uuid = graphene.Field(AuthorType, uuid=graphene.UUID(required=True))
    books_by_author_name = graphene.List(BookType, name=graphene.String(required=False))
    all_todo = graphene.List(TodoType)
    all_projects = graphene.List(ProjectType)

    def resolve_all_todo(root, info):
        return ToDo.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_authors(root, info):
        return Author.objects.all()

    def resolve_author_by_uuid(root, info, uuid):
        try:
            return Author.objects.get(uuid=uuid)
        except Author.DoesNotExist:
            return None

    def resolve_books_by_author_name(root, info, name=None):
        if name:
            try:
                author_uuid = Author.objects.get(last_name=name)
                return Book.objects.filter(author=author_uuid)
            except Book.DoesNotExist:
                return None
        else:
            return Book.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
