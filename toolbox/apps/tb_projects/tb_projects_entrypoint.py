import typer

from apps.tb_projects.cli_commands import create_command

app = typer.Typer()
app.add_typer(create_command.app, name='create')
