from graphene import ObjectType, String, NonNull, Schema


class SomeQuery(ObjectType):
    name = NonNull(String, name=String(default_value="somebody"))
    password_hash = String(password=String())

    def resolve_name(root, info, name):
        return f"Hello {name.capitalize()}"

    def resolve_password_hash(root, info, password):
        return str(hash(password))


some_schema = Schema(query=SomeQuery)
result = some_schema.execute("{ passwordHash(password: \"1234\") name(name: \"me\") }")

print(result)