from typing import Iterable
from jinja2.environment import Environment, Template
from jinja2.loaders import FileSystemLoader
import yaml
from yaml.loader import FullLoader


class Yex:
    _t = None  # template if initiated by passing string with it
    _env = None  # environment if initiated with templates path

    def __init__(self, t: str):
        """Init with template folder, template file or template string."""
        is_template_string_passed = '{' in t
        is_template_file_passed = t.endswith(('.yml', '.yaml',))

        if is_template_string_passed:
            self._t = Template(t)
        elif is_template_file_passed:
            with open(t) as file:
                self._t = Template(file.read())
        else:
            self._env = Environment(loader=FileSystemLoader(t))

    def render(self, *args, **context):
        """Render yaml with context"""
        return self._load(self.render_content(*args, **context))

    def render_content(self, *args, **context):
        if self._t:
            """Render pure yaml text template with context"""
            return self._render(self._t, *args, **context)

        if self._env:
            template = self._env.get_template(args[0])
            return self._render(template, *args, **context)

        return ''

    def generate(self, data: Iterable):
        for d in data:
            r = self.render(d)
            yield r

    @staticmethod
    def _render(template: Template, *args, **kwargs):
        return template.render(*args, **kwargs)

    @staticmethod
    def _load(text: str):
        return yaml.load(text, Loader=FullLoader)

    def __lt__(self, b):
        return self.render(b)

    def __call__(self, *args, **kwargs):
        return self.render(*args, **kwargs)
