import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_cv_from_json(json_file, output_file, image_path, background_image):
    # Load data from the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract sections
    personal_details = data.get("personal_details", {})
    work_experience = data.get("work_experience", [])
    education = data.get("education", [])

    # Create a canvas
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Draw an image as the background
    try:
        c.drawImage(background_image, 0, 0, width=width, height=height)  # Adjust size to cover the page
    except Exception as e:
        print(f"Could not load background image: {e}")

    # Define column positions
    left_column_x = 50
    right_column_x = width / 2 + 30
    top_y = height - 50

    # Add picture to the left column
    try:
        c.drawImage(image_path, left_column_x, top_y - 210, width=100, height=170)  # Adjust size and position
    except Exception as e:
        print(f"Could not load image: {e}")

    # Place name above the picture
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left_column_x, top_y - 20, personal_details.get("name", "Your Name"))  # Positioned above the image

    # Left column - Personal Details
    c.setFont("Helvetica", 12)
    c.drawString(left_column_x, top_y - 240, f"Address: {personal_details.get('address', 'N/A')}")
    c.drawString(left_column_x, top_y - 260, f"Phone: {personal_details.get('phone', 'N/A')}")
    c.drawString(left_column_x, top_y - 280, f"Email: {personal_details.get('email', 'N/A')}")
    c.drawString(left_column_x, top_y - 300, f"Date of Birth: {personal_details.get('date_of_birth', 'N/A')}")
    c.drawString(left_column_x, top_y - 320, f"Nationality: {personal_details.get('nationality', 'N/A')}")
    c.drawString(left_column_x, top_y - 340, f"Driving License: {personal_details.get('driving_license', 'N/A')}")

    # Right column - Work Experience
    c.setFont("Helvetica-Bold", 14)
    c.drawString(right_column_x, top_y - 40, "Work Experience")
    c.setFont("Helvetica", 12)
    for i, exp in enumerate(work_experience):
        c.drawString(right_column_x, top_y - 60 - (i * 20), f"- {exp}")

    # Right column - Education
    c.setFont("Helvetica-Bold", 14)
    c.drawString(right_column_x, top_y - 120 - (len(work_experience) * 20), "Education")
    c.setFont("Helvetica", 12)
    for i, edu in enumerate(education):
        c.drawString(right_column_x, top_y - 140 - (len(work_experience) * 20) - (i * 20), f"- {edu}")

    # Save the PDF
    c.save()


# File paths
json_file = "data/cv_data.json"
image_path = "assets/cv_image.jpg"  # Replace with the actual image file path
background_image = "assets/minimalistic_background.jpg"
output_file = "output/Karol_Janowski_Refactored_CV.pdf"

# Generate the CV
generate_cv_from_json(json_file, output_file, image_path, background_image)
print("CV has been generated successfully!")
