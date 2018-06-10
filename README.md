# Selenium automates browsers for KODI.

 Example
#
# ...
#
# import xbmcaddon
# from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.driver_utils import get_driver_path
# from selenium.webdriver.common.driver_utils import run_selenium_doker
#
# ...
#
# Addon = xbmcaddon.Addon('plugin.video.adult.freeomovie')
# Docker = Addon.getSetting('use_docker')
# WebTimeOut = Addon.getSetting('web_timeout')
# Debug = Addon.getSetting('use_debug')
# VisibleBrowser = Addon.getSetting('visible_browser')
#
# ...
#
# def openURLWebDriverContent(url):
#    if Docker == 'true':
#        run_selenium_doker()
#        driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
#    else:
#        driverPath = get_driver_path('chromedriver')
#        dbg_log('openURLWebDriverContent','Driver path: ' + driverPath)
#        options = webdriver.ChromeOptions()
#        if VisibleBrowser == 'false':
#            options.add_argument('headless')
#        driver = webdriver.Chrome(driverPath, chrome_options=options)
#    driver.get(url)
#    timeout = int(WebTimeOut)
#    result = ''
#    try:
#        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'postcont'))
#        WebDriverWait(driver, timeout).until(element_present)
#        result = driver.page_source
#        dbg_log('openURLWebDriver','Page source: ' + 'OK')
#    except Exception, e:
#       dbg_log('openURLWebDriverContent', 'ERROR: (' + repr(e) + ')')
#       pass
#    driver.close()
#    if Docker != 'true':
#        driver.service.stop()
#    return result
#
