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
        yaml_str = self._env.get_template(file).render(*args, **context)
        return self._load(yaml_str)

    @classmethod
    def render_text(cls, text, *args, **context):
        """Render pure yaml text template with context"""
        return cls._load(Template(text).render(*args, **context))

    @staticmethod
    def _load(text):
        return yaml.load(text, Loader=FullLoader)


# if __name__ == "__main__":
#     print(Yex('./cfg/').render_file('cfg.yml', test='passed'))
#     print(Yex.render_text('test: {{test}}', test='passed'))
