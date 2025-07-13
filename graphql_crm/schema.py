import graphene
from crm.schema import Mutation as CrmMutation

class Mutation(CrmMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(mutation=Mutation)
