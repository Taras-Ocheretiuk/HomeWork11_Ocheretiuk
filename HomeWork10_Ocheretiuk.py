from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"

driver.get(url)

q1_element = driver.find_element(By.NAME, "q1")
q1_element.send_keys("n")

q2_element = driver.find_element(By.NAME, "q2")
q2_element.send_keys("10")

q3_element = driver.find_element(By.NAME, "q3")
q3_element.send_keys("8")

q9_element = driver.find_element(By.XPATH, '//input[@name="q9" and @value="b" and @type="radio"]')
q9_element.click()

q10_element = driver.find_element(By.XPATH, '//input[@name="q10" and @value="b"]')
q10_element.click()

q11_element = driver.find_element(By.XPATH, '//input[@name="q11" and @value="b"]')
q11_element.click()

q12_element = driver.find_element(By.XPATH, '//input[@name="q12" and @value="b"]')
q12_element.click()

q13_element = driver.find_element(By.XPATH, '//input[@name="q13" and @value="b"]')
q13_element.click()

q14_element = driver.find_element(By.XPATH, '//input[@name="q14" and @value="b"]')
q14_element.click()

q15_element = driver.find_element(By.XPATH, '//input[@name="q15" and @value="b"]')
q15_element.click()

q16_element = driver.find_element(By.XPATH, '//input[@name="q16" and @value="b"]')
q16_element.click()

q17_element = driver.find_element(By.XPATH, '//input[@name="q17" and @value="b"]')
q17_element.click()

q18_element = driver.find_element(By.XPATH, '//input[@name="q18" and @value="b"]')
q18_element.click()

q19_element = driver.find_element(By.XPATH, '//input[@name="q19" and @value="b"]')
q19_element.click()

q20_element = driver.find_element(By.XPATH, '//input[@name="q20" and @value="b"]')
q20_element.click()

q21_element = driver.find_element(By.XPATH, '//input[@name="q21" and @value="b"]')
q21_element.click()

q22_element = driver.find_element(By.XPATH, '//input[@name="q22" and @value="b"]')
q22_element.click()

q23_element = driver.find_element(By.XPATH, '//input[@name="q23" and @value="b"]')
q23_element.click()

q24_element = driver.find_element(By.XPATH, '//input[@name="q24" and @value="b"]')
q24_element.click()

q25_element = driver.find_element(By.XPATH, '//input[@name="q25" and @value="b"]')
q25_element.click()

q26_element = driver.find_element(By.XPATH, '//input[@name="q26" and @value="b"]')
q26_element.click()

q27_element = driver.find_element(By.XPATH, '//input[@name="q27" and @value="b"]')
q27_element.click()

q28_element = driver.find_element(By.XPATH, '//input[@name="q28" and @value="b"]')
q28_element.click()

q29_element = driver.find_element(By.XPATH, '//input[@name="q29" and @value="b"]')
q29_element.click()

q30_element = driver.find_element(By.XPATH, '//input[@name="q30" and @value="b"]')
q30_element.click()

q31_element = driver.find_element(By.XPATH, '//input[@name="q31" and @value="b"]')
q31_element.click()

q32_element = driver.find_element(By.XPATH, '//input[@name="q32" and @value="b"]')
q32_element.click()

q33_element = driver.find_element(By.XPATH, '//input[@name="q33" and @value="b"]')
q33_element.click()

time.sleep(1)

url = "https://test.mensa.no/Home/Test/en-US"

driver.get(url)

age_1850 = driver.find_element('xpath', '//button[contains(@class, "ageselect_1850")]')
age_1850.click()
time.sleep(2)

start_button = driver.find_element(By.ID, 'startTest')
start_button.click()
time.sleep(2)

q1_a_button = driver.find_element('xpath', '//div[@id="question_0"]//div[@data-answerid="0"]')
q1_a_button.click()
time.sleep(2)

q2_b_button = driver.find_element('xpath', '//div[@id="question_1"]//div[@data-answerid="1"]')
q2_b_button.click()
time.sleep(2)

q3_c_button = driver.find_element('xpath', '//div[@id="question_2"]//div[@data-answerid="2"]')
q3_c_button.click()
time.sleep(2)

q4_d_button = driver.find_element('xpath', '//div[@id="question_3"]//div[@data-answerid="3"]')
q4_d_button.click()
time.sleep(2)

q5_e_button = driver.find_element('xpath', '//div[@id="question_4"]//div[@data-answerid="4"]')
q5_e_button.click()
time.sleep(2)

q6_f_button = driver.find_element('xpath', '//div[@id="question_5"]//div[@data-answerid="5"]')
q6_f_button.click()
time.sleep(2)

q7_b_button = driver.find_element('xpath', '//div[@id="question_6"]//div[@data-answerid="1"]')
q7_b_button.click()
time.sleep(2)

q8_b_button = driver.find_element('xpath', '//div[@id="question_7"]//div[@data-answerid="1"]')
q8_b_button.click()
time.sleep(2)

q9_b_button = driver.find_element('xpath', '//div[@id="question_8"]//div[@data-answerid="1"]')
q9_b_button.click()
time.sleep(2)

q10_b_button = driver.find_element('xpath', '//div[@id="question_9"]//div[@data-answerid="1"]')
q10_b_button.click()
time.sleep(2)

q11_b_button = driver.find_element('xpath', '//div[@id="question_10"]//div[@data-answerid="1"]')
q11_b_button.click()
time.sleep(2)

q12_b_button = driver.find_element('xpath', '//div[@id="question_11"]//div[@data-answerid="1"]')
q12_b_button.click()
time.sleep(2)

q13_b_button = driver.find_element('xpath', '//div[@id="question_12"]//div[@data-answerid="1"]')
q13_b_button.click()
time.sleep(2)

q14_b_button = driver.find_element('xpath', '//div[@id="question_13"]//div[@data-answerid="1"]')
q14_b_button.click()
time.sleep(2)

q15_b_button = driver.find_element('xpath', '//div[@id="question_14"]//div[@data-answerid="1"]')
q15_b_button.click()
time.sleep(2)

q16_b_button = driver.find_element('xpath', '//div[@id="question_15"]//div[@data-answerid="1"]')
q16_b_button.click()
time.sleep(2)

q17_b_button = driver.find_element('xpath', '//div[@id="question_16"]//div[@data-answerid="1"]')
q17_b_button.click()
time.sleep(2)

q18_b_button = driver.find_element('xpath', '//div[@id="question_17"]//div[@data-answerid="1"]')
q18_b_button.click()
time.sleep(2)

q19_b_button = driver.find_element('xpath', '//div[@id="question_18"]//div[@data-answerid="1"]')
q19_b_button.click()
time.sleep(2)

q20_b_button = driver.find_element('xpath', '//div[@id="question_19"]//div[@data-answerid="1"]')
q20_b_button.click()
time.sleep(2)

q21_b_button = driver.find_element('xpath', '//div[@id="question_20"]//div[@data-answerid="1"]')
q21_b_button.click()
time.sleep(2)

q22_b_button = driver.find_element('xpath', '//div[@id="question_21"]//div[@data-answerid="1"]')
q22_b_button.click()
time.sleep(2)

q23_b_button = driver.find_element('xpath', '//div[@id="question_22"]//div[@data-answerid="1"]')
q23_b_button.click()
time.sleep(2)

q24_b_button = driver.find_element('xpath', '//div[@id="question_23"]//div[@data-answerid="1"]')
q24_b_button.click()
time.sleep(2)

q25_b_button = driver.find_element('xpath', '//div[@id="question_24"]//div[@data-answerid="1"]')
q25_b_button.click()
time.sleep(2)

q26_b_button = driver.find_element('xpath', '//div[@id="question_25"]//div[@data-answerid="1"]')
q26_b_button.click()
time.sleep(2)

q27_b_button = driver.find_element('xpath', '//div[@id="question_26"]//div[@data-answerid="1"]')
q27_b_button.click()
time.sleep(2)

q28_b_button = driver.find_element('xpath', '//div[@id="question_27"]//div[@data-answerid="1"]')
q28_b_button.click()
time.sleep(2)

q29_b_button = driver.find_element('xpath', '//div[@id="question_28"]//div[@data-answerid="1"]')
q29_b_button.click()
time.sleep(2)

q30_b_button = driver.find_element('xpath', '//div[@id="question_29"]//div[@data-answerid="1"]')
q30_b_button.click()
time.sleep(2)

q31_b_button = driver.find_element('xpath', '//div[@id="question_30"]//div[@data-answerid="1"]')
q31_b_button.click()
time.sleep(2)

q32_b_button = driver.find_element('xpath', '//div[@id="question_31"]//div[@data-answerid="1"]')
q32_b_button.click()
time.sleep(2)

q33_b_button = driver.find_element('xpath', '//div[@id="question_32"]//div[@data-answerid="1"]')
q33_b_button.click()
time.sleep(2)

q34_b_button = driver.find_element('xpath', '//div[@id="question_33"]//div[@data-answerid="1"]')
q34_b_button.click()
time.sleep(2)

q35_b_button = driver.find_element('xpath', '//div[@id="question_34"]//div[@data-answerid="1"]')
q35_b_button.click()
time.sleep(2)

