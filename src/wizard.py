class Wizard:
    def __init__(self, schema: dict):
        self.__schema = schema

    @property
    def schema(self) -> dict:
        return self.__schema
