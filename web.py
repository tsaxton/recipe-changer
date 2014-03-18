import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
import recipe as recipeClass

app=Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def promptUser():
    return render_template('promptUser.html')

@app.route('/originalRecipe', methods=['GET','POST'])
def getOriginalRecipe():
    try:
        recipe = recipeClass.recipe(request.form['url'])
    except:
        return render_template('promptUser.html', error='There was a problem with the recipe you entered. Either the recipe was not from allrecipes.com, or there was a malformed expression within the recipe.')
    return render_template('displayRecipe.html', url=request.form['url'], recipe=recipe)


if __name__ == '__main__':
	    app.run()

