import graphene
from graphene_django import DjangoObjectType
from todo_app.models import ToDo
from users.models import User


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):

    all_todos = graphene.List(ToDoType)
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    todos_by_user_name = graphene.List(ToDoType, name=graphene.String(required=False))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def resolve_todos_by_user_name(self, info, name=None):
        todos = ToDo.objects.all()
        if name:
            todos = todos.filter(author__name=name)
        return todos


schema = graphene.Schema(query=Query)
