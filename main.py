from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import time

chrome_driver_path = '/Users/nikhilmittal/Documents/Selenium/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

uname = '*************'
pwd = '***********'
user_phn_no = '************'

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3104636706&keywords=marketing'

driver.get(URL)

n = 0

try:
    wait = WebDriverWait(driver, 30)
    wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'cta-modal__primary-btn')))

    try:
        sign_in = driver.find_element(by=By.CLASS_NAME, value='cta-modal__primary-btn')
        sign_in.click()

    except NoSuchElementException:
        print('Element Not Found, wrong entry')

except TimeoutError:
    print('Timed Out')

try:
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID, 'username')))
    uname_inp = driver.find_element(by=By.ID, value='username')
    uname_inp.send_keys(uname)
    pass_inp = driver.find_element(by=By.ID, value='password')
    pass_inp.send_keys(pwd)
    main_sign_in = driver.find_element(by=By.CLASS_NAME, value='btn__primary--large')
    main_sign_in.click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, '.jobs-search__left-rail .job-card-list__title')))
    jobs = driver.find_elements(by=By.CSS_SELECTOR, value='.jobs-search__left-rail .job-card-list__title')
    for job in jobs:
        print(job.text)
        job.click()
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.jobs-search__right-rail .jobs-apply-button--top-card .artdeco-button__text')))
        job_right = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-search__right-rail .jobs-apply-button--top-card .artdeco-button__text')
        print('before easy apply loop')
        if job_right.text == 'Easy Apply':
            print('inside easy apply loop')
            try:
                job_right.click()
            except StaleElementReferenceException:
                print('stale element, laoding again')
                job_right = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-search__right-rail .jobs-apply-button--top-card .artdeco-button__text')
                job_right.click()
            print('easy apply clicked')
            wait = WebDriverWait(driver, 10)
            wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'artdeco-modal__dismiss')))
            dismiss_btn = driver.find_element(by=By.CLASS_NAME, value='artdeco-modal__dismiss')
            dismiss_btn.click()
            print('dismiss button clicked')
            wait = WebDriverWait(driver, 10)
            wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'artdeco-button--secondary')))
            discard_btn = driver.find_element(by=By.CLASS_NAME, value='artdeco-button--secondary')
            discard_btn.click()
            print('discard button clicked')
            time.sleep(5)

        else:
            print("can't easy apply")

except NoSuchElementException:
    print('No element found')


driver.quit()

