from datetime import datetime
from video import db


class Videos(db.Model):
    video_name = db.Column(db.String(20), nullable=False, primary_key=True)
    video_do = db.Column(db.Integer)
    video_likes = db.Column(db.Integer)

    def __repr__(self):
        return f"Videos('{self.video_name}', '{self.video_do}', '{self.video_likes}')"

