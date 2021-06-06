from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://redmine.zippyops.com:3000/')

signin = driver.find_element_by_xpath('//*[@id="account"]/ul/li[1]/a')
signin.click()

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('E00028')

userpasswd = driver.find_element_by_xpath('//*[@id="password"]')
userpasswd.send_keys('Zippyops@123')

login = driver.find_element_by_xpath('//*[@id="login-submit"]')
login.click()

clockin = driver.find_element_by_xpath('//*[@id="clockin"]')
clockin.click()