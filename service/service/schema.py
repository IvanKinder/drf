import graphene
from graphene_django import DjangoObjectType
from library.models import Book, Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    author_by_uuid = graphene.Field(AuthorType, uuid=graphene.UUID(required=True))
    books_by_author_name = graphene.List(BookType, name=graphene.String(required=False))

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


schema = graphene.Schema(query=Query)
