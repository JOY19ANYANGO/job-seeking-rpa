# selenium_script.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from your_flask_app import create_app, db
from models import User

def login_to_website(username, password):
    # Initialize the WebDriver (in this example, using Chrome)
    driver = webdriver.Chrome()

    # Navigate to the login page
    driver.get("https://www.linkedin.com/login")

    # Find and fill in the username and password fields
    username_field = driver.find_element("id", "username")
    password_field = driver.find_element("id", "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Simulate pressing the Enter key to submit the form
    password_field.send_keys(Keys.RETURN)

    # Perform additional actions as needed (e.g., navigate to specific pages, interact with elements)

    # Close the browser
    driver.quit()

def process_users(start_id, batch_size):
    app = create_app()
    with app.app_context():
        while True:
            # Fetch a batch of users starting from start_id
            users = User.query.filter(User.id >= start_id, User.processed == False).limit(batch_size).all()

            if not users:
                break  # No more users to process

            for user in users:
                login_to_website(user.username, user.password)
                user.processed = True  # Mark the user as processed
                db.session.commit()

            start_id += batch_size

# Example usage for processing users in batches
process_users(start_id=1, batch_size=100)
