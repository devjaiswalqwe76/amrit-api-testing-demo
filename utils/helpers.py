from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_status(passed):
    return "PASS" if passed else "FAIL"
