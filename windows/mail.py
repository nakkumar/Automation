mail variable passing
**********************

from selenium import webdriver

import time

sendmailid = 'arunkumar.nagarajan@zippyops.in'
sendmailpasswd = 'Arun@1997'
tomailid = 'admin@zippyops.in'
ccmailid = 'CC'
bccmailid = 'BCC'
subjectmsg = 'testing'
bodymsg = 'demo-testing'



driver = webdriver.Chrome()
driver.get('http://192.168.1.4/webmail/src/login.php')

sendmail = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/center/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input')
sendmail.send_keys(sendmailid)

sendmailpass = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/center/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input[1]')
sendmailpass.send_keys(sendmailpasswd)

time.sleep(1)

maillogin = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/center/table/tbody/tr[3]/td/center/input')
maillogin.click()

time.sleep(2)

#comp = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/a[1]')
#comp.click()

driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")

driver.get('http://192.168.1.4/webmail/src/compose.php?mailbox=INBOX&startMessage=1')

time.sleep(1)

tomail = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[2]/input')
tomail.send_keys(tomailid)

#ccmail = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input')
#ccmail.send_keys(ccmailid)

#bccmail = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input')
#bccmail.send_keys(bccmailid)

subject = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td[2]/input')
subject.send_keys(subjectmsg)

body = driver.find_element_by_xpath('//*[@id="body"]')
body.send_keys(bodymsg)

send = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[8]/td/input')
send.click()



###########################################################################################
from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get('http://192.168.1.4/webmail/src/login.php')

mailid = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/center/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input')
mailid.send_keys('arunkumar.nagarajan@zippyops.in')

mailidpasswd = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/center/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input[1]')
mailidpasswd.send_keys('Arun@1997')

time.sleep(1)

maillogin = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/center/table/tbody/tr[3]/td/center/input')
maillogin.click()

time.sleep(2)

#comp = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/a[1]')
#comp.click()

driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")

driver.get('http://192.168.1.4/webmail/src/compose.php?mailbox=INBOX&startMessage=1')

time.sleep(1)

tomail = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[2]/input')
tomail.send_keys('admin@zippyops.in')

#ccmail = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input')
#ccmail.send_keys('DEMO-CC')

#bccmail = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input')
#bccmail.send_keys('DEMO-BCC')

subject = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td[2]/input')
subject.send_keys('DEMO-SUBJECT')

body = driver.find_element_by_xpath('//*[@id="body"]')
body.send_keys('Testing')

send = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[8]/td/input')
send.click()

