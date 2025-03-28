import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# Load data from the JSON file
with open('data/cv_data.json', 'r') as file:
    data = json.load(file)

# Set up Jinja2 environment to load the template from the current directory
env = Environment(loader=FileSystemLoader('.'))  # Current directory
template = env.get_template('templates/template.html')  # Specify the template name

# Render the HTML with data
rendered_html = template.render(data)

# Generate the PDF
HTML(string=rendered_html).write_pdf('output/cv.pdf')

print("PDF CV generated successfully!")