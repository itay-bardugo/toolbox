from typing import Type, Any

from apps.tb_projects.pipelines.create_from_teomplate_pipeline import CreateFromTemplatePipeline
from core.entrypoints.base_entrypoint import Entrypoint


class CreateProjectFromTemplateEntrypoint(Entrypoint):
    pipeline: CreateFromTemplatePipeline

    def get_pipeline_klass(self) -> Type[Any]:
        return CreateFromTemplatePipeline

    def enter(self):
        self.pipeline.setup_template()
        self.pipeline.validate_project()
        self.pipeline.copy_files()
