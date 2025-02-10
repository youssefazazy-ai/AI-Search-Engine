from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import SQLALCHEMY_DATABASE_URL  
from app.models import Base  

# ✅ PostgreSQL connection
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)  # `echo=True` for debugging (remove in production)

# ✅ Session setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ❌ Remove `Base.metadata.create_all(engine)` (Handled by Alembic)

# ✅ Dependency for DB session with better error handling
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()  # Rollback if there's an error
        raise e
    finally:
        db.close()
