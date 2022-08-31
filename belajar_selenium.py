import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogin(unittest.TestCase): #TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome

    def test_success_login(self):
        #Steps
        browser = self.browser 
        browser.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
        time.sleep(1) #delay 5 detik
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("klarenss@gmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("yohisoyoh")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(1)

        #Validation
        response_message = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        response_data = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertIn('Welcome',response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_failed_login_by_invalid_password(self):
        #Steps
        browser = self.browser 
        browser.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
        time.sleep(2) #delay 5 detik
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("klarenss@gmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("yohisoyoh122")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(1)

        #Validation
        response_message = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        response_data = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertIn("Welcome User's not found ")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
        
    def tearDown(self):
        self.browser.close  

if __name__ == "__main__":
    unittest.main()
