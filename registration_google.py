from selenium import webdriver
import undetected_chromedriver as uc
import time


# options.add_argument("--headless")
if __name__ == '__main__':
    driver = uc.Chrome()

    url = 'https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    driver.get(url)
    email = driver.find_element_by_id('identifierId')
    email.send_keys('LOGIN')

    nextBtn = driver.find_element_by_id('identifierNext')
    nextBtn.click()

    time.sleep(2)
    passwd = driver.find_element_by_name('password')
    passwd.send_keys('PASS')


    nextBtn = driver.find_element_by_id('passwordNext')
    nextBtn.click()

    # print("Login completed!")
