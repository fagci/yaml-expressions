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
