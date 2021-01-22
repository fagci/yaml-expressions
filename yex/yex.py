from jinja2.environment import Environment, Template
from jinja2.loaders import FileSystemLoader
import yaml
from yaml.loader import FullLoader


class Yex:
    def __init__(self, templates_path):
        """Init with yaml templates folder"""
        self._env = Environment(loader=FileSystemLoader(templates_path))

    def render_file(self, file, *args, **context):
        """Render yaml with context"""
        template = self._env.get_template(file)
        yaml_text = self._render(template, *args, **context)
        return self._load(yaml_text)

    @classmethod
    def render_text(cls, text, *args, **context):
        """Render pure yaml text template with context"""
        template = Template(text)
        yaml_text = cls._render(template, *args, **context)
        return cls._load(yaml_text)

    @staticmethod
    def _render(template: Template, *args, **kwargs):
        return template.render(*args, **kwargs)

    @staticmethod
    def _load(text: str):
        return yaml.load(text, Loader=FullLoader)
