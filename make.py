#!python3
import os, sys, collections
import jinja2

sections = collections.OrderedDict()

base_context = {
    'PROJECT':  'Lounge<Chat>',
    'HTTP':     'http:' if len(sys.argv) < 2 or not sys.argv[1].startswith('prod') else '',
    'SECTIONS': sections,
}

loader = jinja2.FileSystemLoader('src')
env    = jinja2.Environment(loader = loader, autoescape = True)

def add_section(name):
    sections[name] = { 'name': name, 'title': name.title() }

def render_part(name, is_section = True):
    html_name = name + '.html'
    template  = env.get_template(html_name)
    context   = dict(base_context)

    if is_section:
        context['current_section'] = sections[name]

    result = template.render(**context)

    with open(html_name, 'w', encoding = 'utf-8') as fp:
        fp.write(result)

def render():
    render_part('index', is_section = False)
    for section in sections:
        render_part(section)

add_section('project')
add_section('contributing')
render()
