from app import app, forms
from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import db as dbmodel


url_name = 'http://127.0.0.1:5000'


@app.route('/', methods=['GET', 'POST'], endpoint='main')
def main():
    if request.method == 'POST':
        mytargeturl = request.form['inputURL']
        myshortenedurl = request.form['shortener']
        dbmodel.addtodb(mytargeturl, myshortenedurl)
        target_url, short_url = dbmodel.return_url(myshortenedurl)
        complete_short_url = url_name + '/' + str(short_url)
        print(complete_short_url)
        return render_template('1index.html',target_url=str(target_url), finalanswer = complete_short_url, url_name=url_name)
    else:
        form = forms.LoginForm()
        return render_template('form.html', form=form, url_name = url_name)


@app.route('/<path>', endpoint='router')
def router(path):
    target_url, _ = dbmodel.return_url(path)
    if target_url.startswith('http'):
        return redirect(target_url)
    else:
        return redirect('http://{}'.format(target_url))
