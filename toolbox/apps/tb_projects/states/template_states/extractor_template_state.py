from apps.tb_projects.configs.constants import EXTRACTORS_DIR_NAME, EXTRACTORS_IMPLEMENTATION_SUFFIX
from apps.tb_projects.states.template_states.template_state import TemplateState


class ExtractorTemplateState(TemplateState):
    def handle(self):
        template = self.make_template()
        tpl_dir = template.get_template_dir()
        all_extractors = tpl_dir.joinpath(EXTRACTORS_DIR_NAME)
        selected_extractor = all_extractors.joinpath(f'{self.extractor}{EXTRACTORS_IMPLEMENTATION_SUFFIX}')
        template.exclude_template_path(str(all_extractors))
        template.include_template_path(str(selected_extractor))
        template.get_template_files()
        return template
