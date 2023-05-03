import typer
import sys

from apps.tb_projects import tb_projects_entrypoint

app = typer.Typer()
app.add_typer(tb_projects_entrypoint.app, name='project')

if __name__ == '__main__':
    app()
