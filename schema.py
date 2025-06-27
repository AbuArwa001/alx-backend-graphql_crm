from graphene import ObjectType
from graphene import String, Int, Field, List
from graphene import Schema
from graphene import Mutation, InputObjectType


class Query(ObjectType):
    hello = String(greetings=String(default_value="Hello, GraphQL!"))

    def resolve_hello(self, info, greetings):
        return f"{greetings}!"

schema = Schema(query=Query)