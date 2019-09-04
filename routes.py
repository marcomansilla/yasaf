from flask import request, Blueprint, render_template, redirect
from models import *
from functions import generate_short_link, add_link

short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
	db._adapter.reconnect()
	record = db(db.links.short_url==short_url).select().first()
	if record:
		db(db.links.id==record.id).update(visits=record.visits+1)
		db.referrers.insert(link=record.id, referrer=request.headers.get("Referer"), user_data=request.headers.get('User-Agent'))
		db.commit()
		return redirect(record.original_url)
	return 'Does not exist'

@short.route('/')
def index():
	return render_template('index.html')

@short.route('/new_link', methods=['POST'])
def new_link():
	print('working on url')
	original_url = request.form['original_url']
	result = add_link(original_url)
	return render_template('new_link.html', data=result.get_json())

@short.route('/stats')
def stats():
	return 'view'

@short.errorhandler(404)
def page_not_found(e):
	return '', 404
