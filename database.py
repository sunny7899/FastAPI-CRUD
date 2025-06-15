from sqlmodel import SQLModel, create_engine

# SQLite URL (uses a local file)
DATABASE_URL = "sqlite:///database.db"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)
