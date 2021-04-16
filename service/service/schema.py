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

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_authors(root, info):
        return Author.objects.all()

    def resolve_author_by_uuid(root, info, uuid):
        try:
            return Author.objects.get(uuid=uuid)
        except Author.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
