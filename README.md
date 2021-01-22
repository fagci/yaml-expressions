# YAML Jinja2 expressions

Renders Jinja2 expressions inside YAML file.

## Examples:

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

Output: {'cfg': {'test': 'passed'}}

