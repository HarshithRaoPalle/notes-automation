from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

from config.environment import config

from utils.logger import get_logger


logger = get_logger()


def get_driver():


    chrome_options = Options()

    chrome_options.add_argument("--start-maximized")

    chrome_options.add_argument("--disable-notifications")

    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=chrome_options
    )


    logger.info("Chrome browser launched")

    return driver