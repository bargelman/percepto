import json
import os
import random
import time

import pytest

from selenium import webdriver
from utilities.readProperties import ReadConfig
from webLocators.web_locators import LoginPageLocators

browserType = ReadConfig.getApplicationBrowserType()
baseURL = ReadConfig.getApplicationBaseURL()

baseDir = os.path.dirname(os.path.abspath(__file__))
baseDirParent = os.path.dirname(baseDir)
loginJsonPath = ReadConfig.getApplicationloginJsonPath()

json_file_path = os.path.join(baseDirParent, "configurations", "loginData.json")


@pytest.fixture(scope="class")
def get_random_user():
    def _get_random_user(login_data_json_file_path):
        with open(login_data_json_file_path, "r") as file:
            data = json.load(file)

        users = data["Login_Data"]
        selected_user_key = random.choice(list(users.keys()))
        selected_user = users[selected_user_key]

        return selected_user

    return _get_random_user


@pytest.fixture(scope="class")
def setup(request, get_random_user):
    if browserType == 'chrome':
        driver = webdriver.Chrome()
    elif browserType == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser not supported. Please choose 'chrome' or 'firefox' browserType in config.ini file.")

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(baseURL)
    random_user = get_random_user(json_file_path)

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    username_field = driver.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT)
    password_field = driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT)

    username_field.send_keys(random_user["userName"])
    password_field.send_keys(random_user["password"])

    driver.find_element(*LoginPageLocators.SUBMIT_LOGIN_BUTTON).click()
    time.sleep(5)

    request.cls.driver = driver
    request.cls.random_user = random_user
    yield
    driver.close()
