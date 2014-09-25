#!python3
import os, sys, collections
import jinja2, pygments, pygments.lexers, pygments.formatters

def highlight(example):
    with open('examples/' + example, 'r', encoding = 'utf-8') as fp:
        code = fp.read()

    lexer       = pygments.lexers.get_lexer_for_filename(example)
    formatter   = pygments.formatters.HtmlFormatter()
    highlighted = pygments.highlight(code, lexer, formatter)

    return jinja2.Markup(highlighted)

def add_section(name):
    sections[name] = { 'name': name, 'title': name.title() }

def render_part(name, is_section = True):
    html_name = name + '.html'
    template  = env.get_template(html_name)
    context   = dict(base_context)

    if is_section:
        context['current_section'] = sections[name]

    result = template.render(**context)

    if not production:
        os.makedirs('tmp', exist_ok = True)
        html_name = 'tmp/' + html_name

    with open(html_name, 'w', encoding = 'utf-8') as fp:
        fp.write(result)

def render():
    render_part('index', is_section = False)
    for section in sections:
        render_part(section)

sections     = collections.OrderedDict()
production   = len(sys.argv) >= 2 and sys.argv[1].startswith('prod')
base_context = {
    'PROJECT':   'Lounge<C++>',
    'HTTP':      '' if production else 'http:',
    'BASE':      '' if production else '../',
    'SECTIONS':  sections,
    'highlight': highlight,
}

loader = jinja2.FileSystemLoader('src')
env    = jinja2.Environment(loader = loader, autoescape = True)

render()
