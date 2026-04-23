import pandas as pd
# create a function that takes filename, summary data, compliance percentage and chart path and generates a report in PDF format
from fpdf import FPDF
def generate_report(filename: str, summary_data: str, compliance_data:pd.DataFrame , compliance_percentage: float, chart_path: str):
    """
    Generate a PDF report with the given summary data, compliance percentage, and chart.

    Parameters:
    filename (str): The name of the PDF file to be created.
    summary_data (str): A summary of the data to be included in the report.
    compliance_percentage (float): The percentage of compliant applications.
    chart_path (str): The path to the chart image to be included in the report.
    """
    pdf = FPDF()
    pdf.add_page()
    
    # Set title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Compliance Report", ln=True, align='C')
    
    # Add summary data
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"Summary:\n{summary_data}\n\nCompliance Percentage: {compliance_percentage:.2f}%")
    
    # Add chart image
    if chart_path:
        pdf.image(chart_path, x=10, y=pdf.get_y(), w=180)
    
    # Save the PDF
    try:
        pdf.output(filename)
        print(f"Report generated successfully: {filename}")
    except Exception as e:
        print(f"Error generating report: {e}")