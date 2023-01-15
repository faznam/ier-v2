from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def generate_badge_pdf():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("myreport.html")
    template_vars = {
        "title": "National Sales Funnel Report",
        "national_pivot_table": "test",
    }
    # Render our file and create the PDF using our css style file
    html_out = template.render(template_vars)
    pdf_file = HTML(string=html_out).write_pdf(stylesheets=["style.css"])
    return pdf_file