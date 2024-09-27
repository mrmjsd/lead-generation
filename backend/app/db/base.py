from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: any
    __name__: str

    # Automatically generate table names based on the class name if not explicitly defined
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()