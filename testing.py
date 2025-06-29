from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

driver = webdriver.Chrome()
driver.maximize_window()

try:

    driver.get("http://localhost/Final_Exam/ocSs/admin.php")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "admin_username")))
    driver.find_element(By.NAME, "admin_username").send_keys("admin")
    time.sleep(1)
    driver.find_element(By.NAME, "admin_pass").send_keys("admin")
    time.sleep(1)
    driver.find_element(By.NAME, "admin_login").click()
    time.sleep(2)


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'☰')]"))).click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-target='#facultyModal']"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "facultyModal")))

    driver.find_element(By.NAME, "emp_number").send_keys("16-10")
    time.sleep(2)
    driver.find_element(By.NAME, "fname").send_keys("Rommel Manuquil")
    time.sleep(2)

    date_field = driver.find_element(By.NAME, "date_hired")
    date_field.click()
    time.sleep(1)
    date_field.send_keys("08-08-2012")
    time.sleep(2)

    driver.find_element(By.NAME, "status").click()
    driver.find_element(By.XPATH, "//option[text()='Temporary']").click()
    time.sleep(2)

    driver.find_element(By.NAME, "background_field").send_keys("IT Elective")
    time.sleep(2)
    driver.find_element(By.NAME, "address").send_keys("brgy. Kalilayan Ibaba Unisan , Quezon")
    time.sleep(2)
    driver.find_element(By.NAME, "contact_no").send_keys("09671231997")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("rommelmanuquil@gmail.com")
    time.sleep(2)
    driver.find_element(By.NAME, "pass").send_keys("Rommel123")
    time.sleep(2)
    driver.find_element(By.NAME, "register_faculty").click()
    time.sleep(2)

  
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'☰')]"))).click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-target='#subjectModal']"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "subjectModal")))

    driver.find_element(By.NAME, "subject_code").send_keys("IT101")
    time.sleep(1)
    driver.find_element(By.NAME, "subject_description").send_keys("Introduction to Computing")
    time.sleep(1)

    Select(driver.find_element(By.NAME, "unit")).select_by_visible_text("3")
    time.sleep(1)
    Select(driver.find_element(By.NAME, "lecture")).select_by_visible_text("2")
    time.sleep(1)
    Select(driver.find_element(By.NAME, "laboratory")).select_by_visible_text("2")
    time.sleep(1)

    driver.find_element(By.NAME, "add").click()
    time.sleep(2)


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'☰')]"))).click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-target='#roomModal']"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "roomModal")))


    driver.find_element(By.NAME, "room").send_keys("Room 04")
    time.sleep(1)
    driver.find_element(By.NAME, "add_room").click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'☰')]"))).click()
    time.sleep(1)


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Create Schedule"))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "subject_description")))


    Select(driver.find_element(By.NAME, "subject_description")).select_by_visible_text("Introduction to Computing")
    time.sleep(1)
    Select(driver.find_element(By.NAME, "day_description")).select_by_visible_text("T TH")
    time.sleep(1)
    Select(driver.find_element(By.NAME, "room_description")).select_by_visible_text("Room 04")
    time.sleep(1)
    Select(driver.find_element(By.NAME, "fname")).select_by_visible_text("Rommel Manuquil")
    time.sleep(1)

    driver.find_element(By.NAME, "add_schedule").click()
    time.sleep(2)

except Exception as e:
    traceback.print_exc()

finally:
    driver.quit()
