from requestium import Session
import os
import sys
import requests
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CFG_DIR = os.path.join(BASE_DIR, "cfg")

gg_firebase_login_url = 'https://accounts.google.com/signin/v2/identifier?passive=1209600&osid=1&continue=https:' \
                        '//console.firebase.google.com/&followup=https://console.firebase.google.com/&flowName=' \
                        'GlifWebSignIn&flowEntry=ServiceLogin'

firebase_consoel_hosting_url = "https://console.firebase.google.com/project/dukedukedukedukeyang/hosting"
firebase_hosting_overview_url = "https://console.firebase.google.com/project/duketest0001/overview"

s = Session(webdriver_path=os.path.join(CFG_DIR, "win", "chromedriver.exe") if sys.platform.startswith(
        'win') else os.path.join(CFG_DIR, "chromedriver"), browser='chrome', default_timeout=15)

s.driver.get(gg_firebase_login_url)

EMAIL = "test"
PWD = "test"
PROJECT_NAME = "dukeduke"
PROJECT_ID = "dukedukedukedukeyang"
USE_COOKIE = False
FILE_OUTPUT = os.path.join(BASE_DIR, "result")
HEADERS = {"Content-Type": "application/javascript;charset=utf-8",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/62.0.3202.89 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
           "Referer": "https://console.firebase.google.com/",
           "X-client-data": "CJS2yQEIpLbJAQjEtskBCKmdygEIqKPKAQjPp8oBGPmlygE="
           }

sites_list = ["test"]

s.driver.ensure_element_by_xpath("//input[@id='identifierId']",
                                 state="visible", timeout=20).send_keys(EMAIL)
s.driver.ensure_element_by_xpath("//div[@id='identifierNext']/content[1]/span[1]",
                                 state="clickable", timeout=20).ensure_click()
s.driver.ensure_element_by_xpath("//input[@name='password']",
                                 state="visible", timeout=20).send_keys(PWD)
s.driver.ensure_element_by_xpath("//div[@id='passwordNext']/content[1]/span[1]",
                                 state="clickable", timeout=20).ensure_click()
s.driver.ensure_element_by_xpath("//*[@id='firebase-projects']/div[4]/project-card/div/md-card",
                                 state="clickable", timeout=80).ensure_click()
s.driver.ensure_element_by_xpath("//*[@id='nav-Develop-tree-content']/fb-navbar-item[4]/a",
                                 state="clickable", timeout=20).ensure_click()
s.driver.ensure_element_by_xpath("//*[@id='main']/ng-transclude/div/div/div/div[2]/md-single-grid/"
                                 "sites-overview-card/div/div/div/div/button",
                                 state="clickable", timeout=20).ensure_click()
for item in sites_list:
    s.driver.ensure_element_by_xpath("//*[@id='hosting_add_site_dialog']/ng-component/fire-dialog/div[2]/"
                                     "form/div/div/div/input", state="visible", timeout=20).send_keys(item)
    seconds_confirm = raw_input()
    if seconds_confirm == "yes":
        s.driver.ensure_element_by_xpath("//*[@id='hosting_add_site_dialog']/ng-component/fire-dialog/div[3]/button[2]",
                                         state="clickable", timeout=30).ensure_click()



