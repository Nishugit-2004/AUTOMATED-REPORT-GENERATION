import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import pagesizes
from reportlab.lib.units import inch
from datetime import datetime

print("Script started...")

try:
    data = pd.read_csv("data.csv")
    print("Data loaded successfully.")
except Exception as e:
    print("Error loading CSV:", e)
    exit()

# Analysis
total_employees = len(data)
average_salary = data["Salary"].mean()
max_salary = data["Salary"].max()
min_salary = data["Salary"].min()

print("Analysis completed.")

# Create PDF
doc = SimpleDocTemplate("generated_report.pdf", pagesize=pagesizes.letter)
elements = []
styles = getSampleStyleSheet()

elements.append(Paragraph("<b>Automated Employee Analysis Report</b>", styles['Title']))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph(f"Generated on: {datetime.now()}", styles['Normal']))
elements.append(Spacer(1, 0.3 * inch))

summary_data = [
    ["Total Employees", total_employees],
    ["Average Salary", f"${average_salary:.2f}"],
    ["Highest Salary", f"${max_salary}"],
    ["Lowest Salary", f"${min_salary}"]
]

table = Table(summary_data)
table.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(table)

doc.build(elements)

print("✅ Report generated successfully: generated_report.pdf")
