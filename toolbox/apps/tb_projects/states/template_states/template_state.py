from abc import ABCMeta, abstractmethod

from apps.tb_projects.configs.constants import PROJECTS_DIR
from core.templates.make_template import MakeTemplate


class TemplateState(metaclass=ABCMeta):
    def __init__(self, project, extractor, **kwargs):
        self.project = project
        self.extractor = extractor


    @abstractmethod
    def handle(self):
        ...

    def make_template(self):
        template_creator = MakeTemplate(
            templates_dir=str(PROJECTS_DIR),
            target_template=self.project,
        )
        return template_creator.make()
