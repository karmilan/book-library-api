from sqlmodel import Session, create_engine

from app.core.config import Settings


# MySQL connection URL
mysql_url = f"mysql+pymysql://{Settings.DB_USER}:{Settings.DB_PASSWORD}@{Settings.DB_HOST}/{Settings.DB_NAME}"

engine = create_engine(mysql_url, echo=True)


# Dependency
def get_session():
    with Session(engine) as session:
        yield session
