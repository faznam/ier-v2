import os

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

PATH_BADGE_SERVICE = os.path.dirname(os.path.abspath(__file__))


def generate_badge_pdf():
    env = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(PATH_BADGE_SERVICE, "templates")),
        trim_blocks=False,
    )
    file_html = "template.html"

    template = env.get_template(file_html)

    template_vars = {
        "title": "National Sales Funnel Report",
        "national_pivot_table": "test",
    }
    # TODO add css
    html_out = template.render(template_vars)
    pdf_file = HTML(string=html_out).write_pdf()
    return pdf_file
