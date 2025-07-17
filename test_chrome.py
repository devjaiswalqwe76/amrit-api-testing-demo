from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Auto-download and use ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate and test
driver.get("https://www.google.com")
assert "Google" in driver.title

# Clean up
driver.quit()
