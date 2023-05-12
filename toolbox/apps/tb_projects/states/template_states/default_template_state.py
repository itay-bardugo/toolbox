from apps.tb_projects.states.template_states.template_state import TemplateState


class DefaultTemplateState(TemplateState):

    def handle(self):
        return self.make_template()
