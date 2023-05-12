from functools import cache
from pathlib import Path

import pandas as pd


class Template:
    def __init__(self, folder):
        self.dir = Path(folder)
        self._excluded_path = []
        self._included_path = []

    def exclude_template_path(self, p):
        self._excluded_path.append(p)

    def include_template_path(self, p):
        self._included_path.append(p)

    def get_template_dir(self):
        return self.dir

    @cache
    def get_template_files(self):
        project_files = set([str(path) for path in self.dir.glob('**/*')])
        project_files.add(str(self.dir))
        include_files, excluded_files = set(), set()
        for path in self._included_path:
            to_update = [str(path)]
            to_update.extend([str(child) for child in Path(path).glob('**/*')])
            to_update.extend([str(Path(path).parents[0])])
            init_file = Path(path).parents[0].joinpath('__init__.py')
            if init_file.is_file():
                to_update.extend([str(init_file)])
            include_files.update(to_update)
        for path in self._excluded_path:
            to_update = [str(path)]
            to_update.extend([str(child) for child in Path(path).glob('**/*')])
            excluded_files.update(to_update)
        excluded_files = excluded_files - include_files
        project_files = project_files - excluded_files

        # return project_files
