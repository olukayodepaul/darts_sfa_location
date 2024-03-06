import graphene

# import graphene

# # Define your types
# # class Country(graphene.ObjectType):
# #     id = graphene.Int()
# #     name = graphene.String()

# # class Continent(graphene.ObjectType):
# #     id = graphene.Int()
# #     name = graphene.String()
# #     countries = graphene.List(Country)
# #     created_at = graphene.String()

# # class Query(graphene.ObjectType):
# #     continents = graphene.List(Continent)
# #     continent = graphene.Field(Continent, id=graphene.Int(required=True))

# #     def resolve_continents(self, info):
# #         # Your logic to fetch continents from the database
# #         continents_data = [
# #             {"id": 1, "name": "Africa", "created_at": "2024-02-26T13:17:15.511383", "countries": [{"id": 1, "name": "Nigeria"}, {"id": 2, "name": "Ghana"}]},
# #             {"id": 2, "name": "Europe", "created_at": "2024-02-26T13:17:50.053310", "countries": [{"id": 3, "name": "France"}, {"id": 4, "name": "Germany"}]},
# #             {"id": 3, "name": "Asia", "created_at": "2024-02-26T13:17:56.473773", "countries": [{"id": 5, "name": "China"}, {"id": 6, "name": "India"}]}
# #         ]
        
# #         continents = []
# #         for continent_data in continents_data:
# #             continent = Continent(
# #                 id=continent_data["id"],
# #                 name=continent_data["name"],
# #                 created_at=continent_data["created_at"],
# #                 countries=[Country(id=country["id"], name=country["name"]) for country in continent_data["countries"]]
# #             )
# #             continents.append(continent)
# #         return continents

# #     def resolve_continent(self, info, id):
# #         # Your logic to fetch a continent by its ID from the database
# #         # Implement your logic to retrieve the continent with the provided ID
# #         # For now, I'll return a mock continent with the provided ID
# #         continent_data = {
# #             "id": id,
# #             "name": "Mock Continent",
# #             "created_at": "2024-02-26T13:17:15.511383",
# #             "countries": [{"id": 1, "name": "Mock Country 1"}, {"id": 2, "name": "Mock Country 2"}]
# #         }
# #         return Continent(
# #             id=continent_data["id"],
# #             name=continent_data["name"],
# #             created_at=continent_data["created_at"],
# #             countries=[Country(id=country["id"], name=country["name"]) for country in continent_data["countries"]]
# #         )

# # Create a schema
# # schema = graphene.Schema(query=Query)

# class Person(graphene.ObjectType):
#     id = graphene.ID(required=True)
#     name = graphene.String(required=True)
#     age = graphene.Int()
#     email = graphene.String()

# class Query(graphene.ObjectType):

#     def resolve_my_people(self, info, name=None, age=None, email=None):
#         # List of all people (assuming this comes from a data source)
#         people_data = [
#             {
#                 "id": "123456789",
#                 "name": "John Doe",
#                 "age": 30,
#                 "email": "john.doe@example.com"
#             },
#             {
#                 "id": "987654321",
#                 "name": "Jane Smith",
#                 "age": 25,
#                 "email": "jane.smith@example.com"
#             }
#             # Add more people data as needed
#         ]

#         # Filter people based on provided criteria
#         filtered_people = []
#         for person_data in people_data:
#             if (name is None or person_data['name'] == name) and \
#                (age is None or person_data['age'] == age) and \
#                (email is None or person_data['email'] == email):
#                 # Create a Person object from the person_data dictionary
#                 person = Person(**person_data)
#                 filtered_people.append(person)

#         return filtered_people

class Person(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    age = graphene.Int()
    email = graphene.String()    
    
class calculate(graphene.ObjectType):
    
    data = graphene.Field(Person, id = graphene.ID())
    
    def resolve_data(self, info, id=None):
        
        result = {}
        
        person_data = { 
                "id": 1,
                "name": "Jane Smith",
                "age": 25,
                "email": "jane.smith@example.com" 
                }
        
        if id is None:
            result = person_data 
        else:
            person_data['id'] = id
            result = person_data 
        
        return Person(**result)
    
schema = graphene.Schema(query=calculate)