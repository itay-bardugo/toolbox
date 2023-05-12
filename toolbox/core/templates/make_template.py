import os
from pathlib import Path

from core.configs.core_constants import PROJECT_PATH_SUFFIX
from core.exceptions.template_exceptions import TemplateNotFound, TemplatesDirNotFound
from core.templates.template_entities.template import Template


class MakeTemplate:
    def __init__(self, templates_dir: str, target_template: str):
        self.templates_dir = templates_dir
        self.target_template = target_template

    def make(self):
        if not os.path.isdir(self.templates_dir):
            raise TemplatesDirNotFound(f'{self.templates_dir} is not a folder')
        project = Path(self.templates_dir).joinpath(f'{self.target_template}{PROJECT_PATH_SUFFIX}')
        if not os.path.isdir(project):
            raise TemplateNotFound(f'project {project} not exists')

        return Template(
            folder=project
        )
