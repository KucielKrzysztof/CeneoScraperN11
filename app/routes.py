from app import app
from flask import render_template
import json
import requests
from bs4 import BeautifulSoup

@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/extract/<product_id>')
def  extract(product_id):
    pass

@app.route('/products')
def  products():
    pass

@app.route('/product/<product_id>')
def  product(product_id):
    pass
