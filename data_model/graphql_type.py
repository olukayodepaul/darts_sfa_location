import graphene

class ContinentType(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String()
    created_at = graphene.DateTime()

