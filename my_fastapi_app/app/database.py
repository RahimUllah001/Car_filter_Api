from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://postgres:Ali_wazir1@localhost/car_db"  # Use the normal postgres driver

# Create the engine (synchronous version)
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory (use Session class for synchronous behavior)
SessionLocal = sessionmaker(
    bind=engine,  # The engine to bind the session to
    class_=Session,  # Use Session instead of AsyncSession
    autocommit=False,
    autoflush=False,
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # Use the synchronous session
    try:
        yield db
    finally:
        db.close()  # Make sure to close the session after use
# &min_price=111111&max_price=3000000
# &min_price=111111&max_price=3000000