from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__))))

def render_prompt(template_name: str, context: dict):
    template = env.get_template(template_name)
    return template.render(**context)
