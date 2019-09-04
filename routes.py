from flask import request, Blueprint, render_template
from models import *
from functions import generate_short_link, add_link

short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
	return 'short_link'

@short.route('/')
def index():
	return render_template('index.html')

@short.route('/new_link', methods=['POST'])
def new_link():
	print('working on url')
	original_url = request.form['original_url']
	result = add_link(original_url)
	return result

@short.route('/stats')
def stats():
	return 'view'

@short.errorhandler(404)
def page_not_found(e):
	return '', 404
