from selenium import webdriver
from time import sleep

import proxy
import tor

VIEWS = 10000
VIEWS_PER_IP = 50

def viewMax():
	pproxy = proxy.Proxy('127.0.0.1:8118')
	chrome_options = webdriver.ChromeOptions()
	
	tor.clean()
	chrome_options.add_argument(f'--proxy-server={pproxy.ip_port}')

	driver = webdriver.Chrome(r'chromedriver.exe', chrome_options=chrome_options)

	for _ in range(0, VIEWS_PER_IP):
		driver.get('http://www.ip-adress.eu/')
		sleep(5)

	driver.quit()

for _ in range(0, VIEWS):
	viewMax()
