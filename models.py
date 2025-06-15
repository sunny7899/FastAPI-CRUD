from sqlmodel import SQLModel, Field

class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    owner_id: str
    data: str
