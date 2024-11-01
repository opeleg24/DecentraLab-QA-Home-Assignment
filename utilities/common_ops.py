import json
import time
import xml.etree.ElementTree as ET

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import test_cases.conftest as conf


def get_data(node_name):
    root = ET.parse('./configuration/data.xml').getroot()
    return root.find('.//' + node_name).text


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def wait(for_element, elem):
    if for_element == 'element_displayed':
        WebDriverWait(conf.driver, 10).until(EC.visibility_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_to_be_clickable':
        WebDriverWait(conf.driver, 10).until(EC.element_to_be_clickable((elem[0], elem[1])))


def get_time_stamp():
    return time.time()


class For:
    ELEMENT_DISPLAYED = 'element_displayed'
    ELEMENT_IS_CLICKABLE = 'element_to_be_clickable'
