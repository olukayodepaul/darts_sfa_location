from graphene import ObjectType, List, Field
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy.orm import Session
from data_model.sqlalchemy_model import Continent as ContinentModel
from data_model.graphql_type import ContinentType 
import graphene

# class Continent(SQLAlchemyObjectType):
#     class Meta:
#         model = ContinentModel
#         interfaces = (graphene.relay.Node,)

class Query(ObjectType):
    all_continents = List(ContinentType)

    def resolve_all_continents(root, info):
        db_session: Session = info.context["request"].state.db_session
        continents = db_session.query(ContinentModel).all()
        return continents

schema = graphene.Schema(query=Query)