import pandas as pd
import yaml
from bs4 import BeautifulSoup
from selenium import webdriver


def get_config(path='config/conf.yaml', location='local'):
    """
    Reads yaml config.
    :param path: path(key)
    :type path: str
    :param location: where your conf.yaml located
    :type location: str

    :return: yaml config.
    :rtype: dict
    """
    if location == 'local':
        with open(path, 'r') as yaml_file:
            return yaml.safe_load(yaml_file)
    else:
        raise RuntimeError


def get_selenium_driver():
    """
    Gets configured Selenium Chrome driver for further usage
    :return:
    """
    return webdriver.Chrome()


def get_dom(url, browser):
    """
    Get events urls
    :param browser: driver
    :param url: url
    :return: list of urls
    """
    # Visit the page
    browser.get(url)
    dom_html = browser.page_source
    return BeautifulSoup(dom_html, 'lxml')


def to_csv(data, file_name):
    """
    Loading data to csv format
    :param data: data
    :type data: list of dicts
    :param file_name: name of file
    :type file_name: str

    :return: None
    """
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
