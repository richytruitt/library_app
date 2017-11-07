import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_index_html():
    fname = "labelmaking/labels/output.html"
    urls = ['Richy', 'Cortney', 'Chris','Richy', 'Cortney', 'Chris']
    context = {
        'urls': urls
    }
    #
    with open(fname, 'w') as f:
        html = render_template('labels.html.jinja2', context)
        f.write(html)
 
 
def main():
    create_index_html()
 
if __name__ == "__main__":
    main()