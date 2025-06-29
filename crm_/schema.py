from graphene import ObjectType
from graphene import String
from graphene import Schema

class Query(ObjectType):
    hello = String(greetings=String(default_value="Hello, GraphQL"))

    def resolve_hello(self, info, greetings):
        return f"{greetings}!"

# schema = Schema(query=Query)
schema = Schema(query=Query)