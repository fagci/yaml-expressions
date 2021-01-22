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

print(yex.render_file('cfg.yml', test='passed'))
```

Output: `{'cfg': {'test': 'passed'}}`

### Load template from string

```python
from yex import Yex

print(yex.render_text('test: {{test}}', test='passed'))
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
