import typer

from apps.tb_projects.entrypoints.create_from_template_entrypont import CreateFromTemplateEntrypoint

app = typer.Typer()


@app.command(name='extractor')
def create_extractor(location):
    """
    starts an extractor project
    :param location:
    :return:
    """
    ep = CreateFromTemplateEntrypoint(
        project='extractor',
        location=location
    )
    ep.enter()
