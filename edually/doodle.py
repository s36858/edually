from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from time import sleep


def app():
    # name = input("Name: \n")
    # email = input("Email: \n")
    eventTitle = input("Event Title: \n")
    description = input("Description: \n")
    # location = input("Location: \n")
    # fromDate = input(
    #     "Date(Day 1):\n(Format: YY-MM-DD)\n(Example: 2017-01-01) \n")
    # fromDate = fromDate[0:4] + fromDate[5:7] + fromDate[8:10]
    # _time = input("Time Interval:\n(Example- 07:00-14:00) \n")
    # _time = _time[0:2] + _time[3:8] + _time[9:11]
    # _time2 = input("Time Interval(2): \n")
    # _time2 = _time2[0:2] + _time2[3:8] + _time2[9:11]
    # fromDate2 = input("Date(Day 2): \n")
    # fromDate2 = fromDate2[0:4] + fromDate2[5:7] + fromDate2[8:10]
    # _dtime = input("Time Interval: \n")
    # _dtime = _dtime[0:2] + _dtime[3:8] + _dtime[9:11]
    # _dtime2 = input("Time Interval(2, Optional): \n")
    # _dtime2 = _dtime2[0:2] + _dtime2[3:8] + _dtime2[9:11]
    # fromDate3 = input("Date(Day 3): \n")
    # fromDate3 = fromDate3[0:4] + fromDate3[5:7] + fromDate3[8:10]
    # _ddtime = input("Time Interval: \n")
    # _ddtime = _ddtime[0:2] + _ddtime[3:8] + _ddtime[9:11]
    # _ddtime2 = input("Time Interval(2, Optional): \n")
    # _ddtime2 = _ddtime2[0:2] + _ddtime2[3:8] + _ddtime2[9:11]

    doodUrl = "http://doodle.com/create?type=date&locale=en&title=" + \
        eventTitle

    # + "&name=" + name
    # + "&note=" + description + "&" + fromDate + "=" + \
    #     _time + "||" + _time2 + "&" + fromDate2 + "=" + _dtime + "||" + _dtime2 + \
    #     "&" + fromDate3 + "=" + _ddtime + "||" + _ddtime2 + "&location=" + location

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(doodUrl)
    try:
        descripton = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id("d-pollDescription")
        )
        driver.find_element_by_id("d-pollDescription").send_keys(description)

        next_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(
            '#d-wizardGeneralInformationNavigationView > div > div > div.d-actionButtons > button')
        )
        driver.execute_script("arguments[0].click();", next_button)

        initemail = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id("initiatorEmail"))
        driver.find_element_by_id("initiatorEmail").send_keys(email)
        next1 = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id("next1"))
        if driver.find_element_by_id("next1").is_enabled() and driver.find_element_by_id("next1").is_displayed():
            pass
        else:
            next1 = WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element_by_id("next1"))
        next1.click()
        next2a = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id("next2a"))
        if driver.find_element_by_id("next2a").is_enabled() and driver.find_element_by_id("next2a").is_displayed():
            pass
        else:
            next2a = WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element_by_id("next2a"))
        next2a.click()
        next2b = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id("next2b"))
        if driver.find_element_by_id("next2b").is_enabled() and driver.find_element_by_id("next2b").is_displayed():
            pass
        else:
            next2b = WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element_by_id("next2b"))
        next2b.click()
        next3s = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id("next3s"))
        if driver.find_element_by_id("next3s").is_enabled() and driver.find_element_by_id("next3s").is_displayed():
            pass
        else:
            next3s = WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element_by_id("next3s"))
        next3s.click()
        finish4a = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id("finish4a"))
        if driver.find_element_by_id("finish4a").is_enabled() and driver.find_element_by_id("finish4a").is_displayed():
            pass
        else:
            finish4a = WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element_by_id("finish4a"))
        finish4a.click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "participationLink")))
            if driver.find_element_by_id("participationLink").is_displayed() and driver.find_element_by_id("participationLink").is_enabled():
                print("Event has been scheduled.")
                print("Thank You for using Doodle Scheduler.")
            else:
                print("Error occurred. Please try again.")
        except TimeoutException:
            print("Timed out waiting for page to load")
        except NoSuchElementException:
            print("Unable to locate element.")
            print("Please try again.")

        print("Timed out waiting for page to load")
        print("Please try again!")
    except NoSuchElementException:
        print("Unable to locate element.")
        print("Please try again.")

    driver.quit()
    sleep(10)


print("test me ")
app()
