import selenium.webdriver.support.ui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def search_on_mumzworld(search_text):
    # Set up the WebDriver
    driver = webdriver.Firefox()  # Replace with your preferred browser

    # Navigate to the website
    driver.get("https://www.mumzworld.com/en/")

    # Wait for the search field to be clickable
    search_field = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/header/div[1]/div[2]/div/div[1]/form/input"))
    )

    # Enter the search text
    search_field.send_keys(search_text)

    # Click on the search icon
    search_icon = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/header/div[1]/div[2]/div/div[1]/form/button[1]"))
    )
    search_icon.click()

    # Wait for the "Show all" button to be clickable
    show_all_button = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/header/div[1]/div[2]/div/div[2]/div[2]/div/a"))
    )

    # Click on the "Show all" button
    show_all_button.click()

    # Wait for 5 seconds for search results
    time.sleep(5)

    # Call the function to click on the first product icon
    click_on_first_product_icon(driver)


def click_on_first_product_icon(driver):
    # Wait for the first product icon to be clickable
    first_product_icon = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/article/div[2]/div[2]/section[1]/div/div/div[1]/a/div/picture/img"))
    )

    # Click on the first product icon
    first_product_icon.click()

    # Wait for 5 seconds for the product page to load
    time.sleep(5)

    # Call the function to click on the "Add to bag" button
    click_on_add_to_bag_button(driver)


def click_on_add_to_bag_button(driver):
    # Wait for the "Add to bag" button to be clickable
    add_to_bag_button = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/div[2]/form/section[7]/button"))
    )

    # Click on the "Add to bag" button
    add_to_bag_button.click()

    # Wait for 5 seconds for the bag to update
    time.sleep(5)

    # Call the function to click on the "View bag" button
    click_on_view_bag_button(driver)


def click_on_view_bag_button(driver):
    # Wait for the "View bag" button to be clickable
    view_bag_button = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div[4]/a"))
    )

    # Click on the "View bag" button
    view_bag_button.click()

    # Wait for 5 seconds for the bag page to load
    time.sleep(5)

    # Call the function to click on the "+" button 5 times
    click_on_plus_button(driver)


def click_on_plus_button(driver):
    # Wait for the "+" button to be clickable
    plus_button = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//*[@id='root']/main/div[2]/div/div[3]/div[1]/div[2]/div/ul/li/div/div[2]/div/form/div/button[2]"))
    )

    # Click on the "+" button 2 times
    for i in range(2):
        plus_button.click()
        time.sleep(1)  # wait for 1 second between clicks

    # Wait for 5 seconds for the quantity to update
    time.sleep(5)

    # Call the function to proceed to checkout
    proceed_to_checkout(driver)


def proceed_to_checkout(driver):
    # Wait for the "Proceed to checkout" button to be clickable
    proceed_to_checkout_button = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/main/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div/button"))
    )

    # Click on the "Proceed to checkout" button
    proceed_to_checkout_button.click()

    # Wait for 5 seconds for the checkout page to load
    time.sleep(5)

    # Call the function to click on the "Sign up" button
    click_on_sign_up_button(driver)


def click_on_sign_up_button(driver):
    # Wait for the "Sign up" button to be clickable
    sign_up_button = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/div[2]/div/div/div/div/button/span"))
    )

    # Click on the "Sign up" button
    sign_up_button.click()

    # Wait for 5 seconds for the sign up page to load
    time.sleep(5)

    # Call the function to fill out the sign up form
    fill_out_sign_up_form(driver)


def fill_out_sign_up_form(driver):
    # Wait for the first name field to be clickable
    first_name_field = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='create_account_page_firstname']"))
    )

    # Enter the first name
    first_name_field.send_keys("qa")
    time.sleep(3)  # wait for 3 seconds

    # Wait for the last name field to be clickable
    last_name_field = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='create_account_page_lastname']"))
    )

    # Enter the last name
    last_name_field.send_keys("tester")
    time.sleep(3)  # wait for 3 seconds

    # Wait for the email field to be clickable
    email_field = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='create_account_page_email']"))
    )

    # Enter the email
    email_field.send_keys("qa.tester@mailinator.com")
    time.sleep(3)  # wait for 3 seconds

    # Wait for the password field to be clickable
    password_field = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='create_account_page_password']"))
    )

    # Enter the password
    password_field.send_keys("Test@112233")
    time.sleep(3)  # wait for 3 seconds

    # Wait for the "Register" button to be clickable
    register_button = selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/div[2]/div/div/form/div[7]/button[1]"))
    )

    # Click on the "Register" button
    register_button.click()

    # Wait for 5 seconds for the registration to complete
    time.sleep(5)

    # Close the browser
    driver.quit()


# Call the function with the search text
search_on_mumzworld("Teknum - Bedside Crib - Grey")
