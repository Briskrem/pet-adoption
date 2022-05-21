from app import db
from models import Pet

db.drop_all()
db.create_all()

img_link = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Male_and_female_chicken_sitting_together.jpg/640px-Male_and_female_chicken_sitting_together.jpg'
note = 'she is a very sweet chicken'

img_link2 = 'https://modernfarmer.com/wp-content/uploads/2021/09/shutterstock_1838180608-scaled.jpg'
note2 = 'he is a bad wolf'

u = Pet(name="Kehe", species = 'chicken', photo_url = img_link, age=1, notes = note, available=True )
v = Pet(name='Fireman', species='wolf', photo_url = img_link2, age=4, notes = note2, available = False )
db.session.add(u)
db.session.add(v)
db.session.commit()
