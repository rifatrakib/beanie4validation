from typer import Typer

from app.main import prepare_database

app = Typer()


@app.command(name="init-db")
def init_db():
    prepare_database()


if __name__ == "__main__":
    app()
