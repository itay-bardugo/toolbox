from typing import Type

from apps.tb_projects.configs.constants import PROJECTS_DIR
from apps.tb_projects.states.template_states.default_template_state import DefaultTemplateState
from apps.tb_projects.states.template_states.template_state import TemplateState
from core.templates.make_template import MakeTemplate


class CreateFromTemplatePipeline:
    def __init__(self, project, location, template_state: Type[TemplateState] = DefaultTemplateState, **kwargs):
        self.project = project
        self.location = location
        self.template_state = template_state(project=project, **kwargs)
        self._template = None

    def setup_template(self):
        self._template = self.template_state.handle()
        return self._template

    def validate_project(self):
        ...

    def copy_files(self):
        ...
