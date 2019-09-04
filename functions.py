import string
from flask import jsonify
from random import choices
from models import *

def add_link(url):
	db._adapter.reconnect()
	short_url=generate_short_link()
	record = db.links.insert(original_url=url, short_url=short_url)
	if record:
		db.commit()
		return jsonify({'record':record, 'url': short_url, 'original_url':url})
	return 'error'

def generate_short_link():
	characters = string.digits + string.ascii_letters
	short_url = ''.join(choices(characters, k=9))

	link = db(db.links.short_url==short_url).select().first()

	if link:
		return generate_short_link()
	return short_url
