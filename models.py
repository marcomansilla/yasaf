from pydal import DAL, Field
from datetime import datetime

db = DAL('sqlite://storage.sqlite', folder='databases')

db.define_table('links',
				Field('original_url'),
				Field('short_url'),
				Field('visits', 'integer'),
				Field('created_on', default=datetime.now)
)
