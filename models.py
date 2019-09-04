from pydal import DAL, Field
from datetime import datetime

db = DAL('sqlite://storage.sqlite', folder='databases')

db.define_table('links',
				Field('original_url'),
				Field('short_url'),
				Field('visits', 'integer', default=0),
				Field('created_on', default=datetime.now)
)

db.define_table('referrers',
				Field('link', db.links),
				Field('referrer'),
				Field('visited_on', default=datetime.now),
				Field('user_data')
)
