from flask_sqlalchemy import SQLAlchemy
from app import app


db = SQLAlchemy(app)


class TargetURL(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    targeturl = db.Column(db.String(120), index=True, unique=True)
    shortenedurls = db.relationship('shortenedURL',backref='target', lazy='dynamic')

    def __repr__(self):
        return 'Target URL: {}'.format(self.targeturl)


class ShortenedURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortenedurl = db.Column(db.String(140))
    target_id = db.Column(db.Integer, db.ForeignKey('targetURL.id'))

    def __repr__(self):
        return '<shortened URL: {}>'.format(self.shortenedurl)


def addtodb(mytargeturl, myshortenedurl):
    if (TargetURL.query.filter_by(targeturl=mytargeturl).first()) is None:
        x = TargetURL(targeturl=mytargeturl)
        db.session.add(x)
        db.session.commit()
    y = ShortenedURL(shortenedurl=myshortenedurl, target_id=TargetURL.query.filter_by(targeturl=mytargeturl).first().id)
    db.session.add(y)
    db.session.commit()


def return_url(myshortenedurl):
    query = ShortenedURL.query.filter_by(shortenedurl=myshortenedurl).first()
    target_url = query.target.targeturl
    short_url = query.shortenedurl
    return target_url, short_url
