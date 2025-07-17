import pytest
from openpyxl import load_workbook
from utils.helpers import get_timestamp, format_status

def pytest_sessionstart(session):
    session.results = []

def pytest_runtest_logreport(report):
    if report.when == "call":
        result = {
            "test": report.nodeid,
            "status": report.outcome == "passed"
        }
        report.session.results.append(result)

def pytest_sessionfinish(session, exitstatus):
    wb = load_workbook("reports/test_results.xlsx")
    ws = wb.active
    for result in session.results:
        ws.append([
            result["test"],
            format_status(result["status"]),
            get_timestamp()
        ])
    wb.save("reports/test_results.xlsx")
    print("✅ PyTest results logged to Excel.")
