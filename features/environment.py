from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import coverage
# import inspect
# import importlib

# def reload_modules():
#   import your_app1
#   import your_app2

#   for app in [your_app1, your_app2]:
#       members = inspect.getmembers(app)
#       modules = map(
#           lambda keyval: keyval[1],
#           filter(lambda keyval: inspect.ismodule(keyval[1]), members),
#       )
#       for module in modules:
#           try:
#               importlib.reload(module)
#           except:
#               continue


def before_all(context):
    # Chrome is used there (headless browser - meaning we can execute tests in a command-line environment, which is what we want for use with SemaphoreCI
    # For debugging purposes, you can use the Firefox driver instead.
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    context.browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver',chrome_options=chrome_options)

    # context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'
    # cov = coverage.Coverage()
    # cov.start()
    # context.cov = cov
    # # modules
    # reload_modules()


def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done
    context.browser.quit()
    # cov = context.cov
    # cov.stop()
    # cov.save()
    # cov.html_report(directory="./cov")


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass
