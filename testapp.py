from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import pytest

from forapp import app

def test_header_present():
    dash_app = dash.Dash(__name__)
    dash_app.layout = app.layout
    dash_app.title = app.title

    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8050/')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        header = driver.find_element(By.CSS_SELECTOR, "h1")
        assert header.text == "Soul Foods Sales Data Visualizer"
    finally:
        driver.quit()

def test_visualisation_present():
    dash_app = dash.Dash(__name__)
    dash_app.layout = app.layout
    dash_app.title = app.title

    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8050/')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "sales-line-chart")))
        graph = driver.find_element(By.ID, "sales-line-chart")
        assert graph is not None
    finally:
        driver.quit()

def test_region_picker_present():
    dash_app = dash.Dash(__name__)
    dash_app.layout = app.layout
    dash_app.title = app.title

    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8050/')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "region-selector")))
        region_picker = driver.find_element(By.ID, "region-selector")
        assert region_picker is not None
    finally:
        driver.quit()

if __name__ == '__main__':
    pytest.main(['testapp.py'])
