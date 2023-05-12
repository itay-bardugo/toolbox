from pathlib import Path
from unittest import TestCase

from core.exceptions.template_exceptions import TemplateNotFound, TemplatesDirNotFound
from core.templates.make_template import MakeTemplate


class TestMakeTemplates(TestCase):
    def test_template_folder_mismatch(self):
        templates_folder = Path(__file__).parent.joinpath(*['fixtures', 'make_template_fixtures', 'bad_path'])
        creator = MakeTemplate(
            templates_dir=str(templates_folder),
            target_template='foo'
        )
        with self.assertRaises(TemplatesDirNotFound) as e:
            creator.make()

    def test_template_mismatch(self):
        templates_folder = Path(__file__).parent.joinpath(*['fixtures', 'make_template_fixtures', 'template_lists'])
        creator = MakeTemplate(
            templates_dir=str(templates_folder),
            target_template='foo'
        )
        with self.assertRaises(TemplateNotFound) as e:
            creator.make()


if __name__ == '__main__':
    TestMakeTemplates.run()
