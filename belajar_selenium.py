import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogin(unittest.TestCase): #TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome

    def test_a_success_login(self):
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
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_b_failed_login_by_password_empty(self):
        #Steps
        browser = self.browser 
        browser.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
        time.sleep(2) #delay 5 detik
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("klarenss@gmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(1)

        #Validation
        response_message = browser.find_element(By.ID,"swal2-content").text
        response_data = browser.find_element(By.ID,"swal2-title").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_c_failed_login_by_password_max_characters(self):
        #Steps
        browser = self.browser 
        browser.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
        time.sleep(2) #delay 5 detik
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("klarenss@gmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[3]").click()
        time.sleep(1)

        #Validation
        response_message = browser.find_element(By.ID,"swal2-content").text
        response_data = browser.find_element(By.ID,"swal2-title").text

        self.assertIn("Email/Password melebihin maksimal karakter")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
        
    def tearDown(self):
        self.browser.close  

class TestRegister(unittest.TestCase): #TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome

    def test_a_success_Register(self):
        #Steps
        browser = self.browser 
        browser.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
        time.sleep(1) #delay 5 detik
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("Justin")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#email_register").send_keys("justin@gmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#password_register").send_keys("yohisoyoh")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click()
        time.sleep(1)

        #Validation
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    

def tearDown(self):
        self.browser.close 

if __name__ == "__main__":
    unittest.main()
