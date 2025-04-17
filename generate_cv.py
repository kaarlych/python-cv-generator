import json
import argparse
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


# Base directory (directory of main.py)
base_dir = Path(__file__).parent.resolve()

# Load data from the JSON file
with open(base_dir / 'data' / 'cv_data.json', 'r') as file:
    data = json.load(file)

# Set up Jinja2 environment to load the template from the 'templates' folder
env = Environment(loader=FileSystemLoader(base_dir / 'templates'))

# Add a custom function to the Jinja2 environment
def file_url(relative_path):
    return (base_dir / relative_path).as_uri()

env.globals['file_url'] = file_url

template = env.get_template('template.html')

# Get the file:// path for the CSS
css_path = (base_dir / 'assets' / 'style.css').as_uri()

# Render the template with data from the JSON file
rendered_html = template.render(
    css_path=css_path,
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
    experience=data['experience'],
    courses=data['courses'],
    skills=data['skills'],
    projects=data['projects']
)


# Generate timestamped filename as default
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
default_filename = f"cv_{timestamp}.pdf"

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--output', default=default_filename, help='Output PDF filename')
args = parser.parse_args()


# Ensure output directory exists
(output_dir := base_dir / 'output').mkdir(exist_ok=True)

# Generate PDF
HTML(string=rendered_html).write_pdf(output_dir / args.output)

print(f"PDF CV generated successfully! Saved to output/{args.output}")

