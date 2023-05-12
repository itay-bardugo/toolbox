import typer

from apps.tb_projects.entrypoints.create_project_from_template_entrypoint import CreateProjectFromTemplateEntrypoint
from apps.tb_projects.states.template_states.extractor_template_state import ExtractorTemplateState

app = typer.Typer()


@app.command(name='extractor')
def create_extractor(extractor: str, location: str):
    """
    starts an extractor project
    """
    ep = CreateProjectFromTemplateEntrypoint(
        project='extractor',
        location=location,
        extractor=extractor,
        template_state=ExtractorTemplateState
    )
    ep.enter()
