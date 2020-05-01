from app import app
from models import db, User, Feedback

db.drop_all()
db.create_all()

calvin = User(username = "calvinla", email = "calvinla@gmail.com", first_name = "Calvin", last_name = "La", password="password1")
feedback = Feedback(title = "test", content = "hello this is a test", username="calvinla")

db.session.add(calvin)
db.session.add(feedback)
db.session.commit()