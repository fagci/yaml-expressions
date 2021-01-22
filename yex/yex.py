from typing import Iterable
from jinja2.environment import Environment, Template
from jinja2.loaders import FileSystemLoader
import yaml
from yaml.loader import FullLoader


class Yex:
    def __init__(self, t: str):
        """Init with yaml templates folder"""
        # is template string
        if '{' in t:
            self._t = Template(t)
        # is file
        else:
            self._env = Environment(loader=FileSystemLoader(t))

    def render(self, *args, **context):
        """Render yaml with context"""
        return self._load(self.render_text(*args, **context))

    def render_text(self, *args, **context):
        if self._t:
            """Render pure yaml text template with context"""
            return self._render(self._t, *args, **context)

        if self._env:
            template = self._env.get_template(args[0])
            return self._render(template, *args, **context)

        return ''

    def generate(self, data: Iterable):
        for d in data:
            yield self.render(**d)

    @staticmethod
    def _render(template: Template, *args, **kwargs):
        return template.render(*args, **kwargs)

    @staticmethod
    def _load(text: str):
        return yaml.load(text, Loader=FullLoader)

    def __lt__(self, b):
        return self.render(self._t, b)

    def __call__(self, *args, **kwargs):
        return self.render(*args, **kwargs)


if __name__ == "__main__":
    template = """
    meta:
    {% for k, v in meta.items() %}
      {{ k }}: >-
        {{ v }}
    {% endfor %}
    """
    data = [
        {
            'meta': {
                'title': 'Hello, world 1!',
                'content': """<h1>Wellcome to our site!</h1>
            <p>Glad to see you!</p>
            """
            }
        },
        {
            'meta': {
                'title': 'Hello, world 2!',
                'content': """<h1>Wellcome to our site!</h1>
            <p>Glad to see you!</p>
            """
            }
        },
    ]
    content_page_template = """<title>{{title}}</title>
    <div>{{content}}</div>"""
    content_page = Yex(content_page_template)
    for cfg in Yex(template).generate(data):
        print(content_page.render_text(cfg))
