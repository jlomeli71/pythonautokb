#!/usr/bin/env python
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/")

j2_vars = {
    "ntp1": "130.126.24.24",
    "ntp2": "152.2.21.1",
    "timezone": "PST",
    "timezone_offset": "-8",
    "timezone_dst": "PDT",
}

template_file = "exer5.j2"
template = env.get_template(template_file)
config = template.render(**j2_vars)
print(config)
