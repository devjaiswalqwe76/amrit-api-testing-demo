from openpyxl import Workbook
from utils.helpers import get_timestamp, format_status

# Create a new workbook and worksheet
wb = Workbook()
ws = wb.active
ws.title = "Test Results"

# Add headers
ws.append(["Test Name", "Status", "Timestamp"])

# Sample results
results = [
    {"test": "test_addition", "status": True},
    {"test": "test_max_value", "status": True},
    {"test": "test_total", "status": False}
]

# Append each result
for result in results:
    ws.append([
        result["test"],
        format_status(result["status"]),
        get_timestamp()
    ])

# Save the new Excel file
wb.save("reports/test_results.xlsx")
print("✅ Excel report created successfully.")
