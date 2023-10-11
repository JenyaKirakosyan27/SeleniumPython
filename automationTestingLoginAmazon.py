from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.amazon.com")

#loginButton = driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']")
loginButton = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
loginButton.click()

emailField = driver.find_element(By.NAME, "email")
emailField.clear()
emailField.send_keys("jenyakirakosyan27@gmail.com")

continueButton = driver.find_element(By.CSS_SELECTOR, "span#continue")
continueButton.click()

passwordFild = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
passwordFild.clear()
passwordFild.send_keys("//eva[@tsaturyan]")

signInButton = driver.find_element(By.ID, "signInSubmit")
signInButton.click()


driver.quit()

