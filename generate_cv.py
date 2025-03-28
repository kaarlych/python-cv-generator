import os
import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# Load data from the JSON file
with open('data/cv_data.json', 'r') as file:
    data = json.load(file)

# Set up Jinja2 environment to load the template from the 'templates' folder
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('template.html')

# Render the HTML with data (including the image path)
rendered_html = template.render(data)

# Generate the PDF and save it to the 'output' folder
HTML(string=rendered_html).write_pdf('output/cv.pdf')

print("PDF CV generated successfully!")