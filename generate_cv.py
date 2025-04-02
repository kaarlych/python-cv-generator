import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# Load data from the JSON file
with open('data/cv_data.json', 'r') as file:
    data = json.load(file)

# Set up Jinja2 environment to load the template from the 'templates' folder
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('template.html')


# Render the template with data from the JSON file
rendered_html = template.render(
    name=data['name'],
    title=data['title'],
    address=data['personal']['address'],
    phone_number=data['personal']['phone_number'],
    email=data['personal']['email'],
    date_of_birth=data['personal']['date_of_birth'],
    nationality=data['personal']['nationality'],
    driving_license=data['personal']['driving_license'],
    github=data['personal']['github'],
    about_me=data['about_me'],
    education=data['education'],
    experience=data['experience']
)

# Generate the PDF and save it to the 'output' folder
HTML(string=rendered_html).write_pdf('output/cv.pdf')

print("PDF CV generated successfully!")