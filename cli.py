from typer import Typer

from app.main import populate_database, prepare_database

app = Typer()


@app.command(name="init-db")
def init_db():
    prepare_database()


@app.command(name="populate-db")
def populate_db():
    populate_database()


if __name__ == "__main__":
    app()
