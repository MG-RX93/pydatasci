from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Method to login and return session object
def login(username, password):
    # URL for the Salesforce login page
    login_url = 'https://salesforce-elf.herokuapp.com/'

    # Create a WebDriver instance (adjust the browser driver as needed)
    driver = webdriver.Chrome()  # You can use other browser drivers as well (e.g., Firefox, Edge)


    # Navigate to Salesforce login page
    driver.get(login_url)

    # Click on the "Production Login" button
    wait = WebDriverWait(driver, 1)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Production Login')]")))
    print(button)
    button.click()

    # # Wait for redirection and capture the final URL
    # wait.until(EC.url_changes(login_url))
    # final_url = driver.current_url

    # # Now you have the final URL after redirection, you can extract information or perform actions as needed
    # print("Final URL after redirection:", final_url)

    # Perform additional actions as needed (e.g., filling login form, submitting credentials)

    # Return session object or perform further actions
    return driver

# Main function
def main():
    # Define credentials
    username = ''
    password = ''

    # Login to Salesforce
    session = login(username, password)
    

if __name__ == "__main__":
    main()
