from sqlmodel import Session, create_engine


MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_HOST = "localhost"
MYSQL_DB = "book_library"

# MySQL connection URL
mysql_url = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

engine = create_engine(mysql_url, echo=True)


# Dependency
def get_session():
    with Session(engine) as session:
        yield session
