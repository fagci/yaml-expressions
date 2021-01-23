# YAML Jinja2 expressions

Renders Jinja2 expressions inside YAML file.

## Install

```
pip install yaml-expressions
```

## Examples

### Load template from file

cfg/cfg.yml:

```yaml
cfg:
  test: "{{test}}"
```

```python
from yex import Yex

yex = Yex('./cfg/')

print(yex.render('cfg.yml', test='passed'))
```

Output: `{'cfg': {'test': 'passed'}}`

### Load template from string

```python
from yex import Yex

result = Yex('test: {{test}}')(test='passed')
# or
result = {'test':'passed'} > Yex('test: {{test}}')
# or
result = Yex('test: {{test}}').render(test='passed')

print(result)
```

Output: `{'test': 'passed'}`

## Another examples

### Describe SEO checklist, generate report

```python
tests_tpl = """
tests:
    title: {{ 20 < (title | length) < 70 }}
    description: {{ 20 < (description | length) < 160 }}"""

report_tpl = """
report: >
    Test results:
      Title: {{ 'ok' if tests.title else 'fail' }}
        ({{ title[:10] }}...)
      Description: {{ 'ok' if tests.description else 'fail' }}
        ({{ description[:10] }}...)
"""

data = {
    'title': 't' * 130,
    'description': 'd' * 120,
}

results = Yex.render_text(tests_tpl, data)
report = Yex.render_text(report_tpl, **results, **data)

print(report.get('report'))
```

Output:

```text
Test results:
  Title: fail
    (tttttttttt...)
  Description: ok
    (dddddddddd...)
```

### Render HTML pages from prepared config

```python
template = """
meta:
{% for k, v in meta.items() %}
  {{ k }}: >-
    {{ v }}
{% endfor %}
data:
{% for k, v in data.items() %}
  {{ k }}: >-
    {{ v }}
{% endfor %}
"""
data = [
    {
        'meta': {
            'title': 'Hello, world 1!',
        },
        'data': {
            'content': """<h1>Wellcome to our site!</h1>
        <p>Glad to see you!</p>
        """
        }
    },
    {
        'meta': {
            'title': 'Hello, world 2!',
        },
        'data': {
            'content': """<h1>Wellcome to our site!</h1>
        <p>Glad to see you!</p>
        """
        }
    },
]
content_page_template = """<title>{{meta.title}}</title>
<div>{{data.content}}</div>"""
content_page = Yex(content_page_template)
for cfg in Yex(template).generate(data):
    print(content_page.render_content(cfg))
```

Output:

```text
<title>Hello, world 1!</title>
    <div><h1>Wellcome to our site!</h1>
    <p>Glad to see you!</p>
    </div>
<title>Hello, world 2!</title>
    <div><h1>Wellcome to our site!</h1>
    <p>Glad to see you!</p>
    </div>
```
