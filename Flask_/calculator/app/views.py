__author__ = 'anna'
# view functions

from flask import render_template, flash, redirect, url_for, request, session
from app import app
from .forms import InputForm, InputStringForm
import json
from .calculation import calculation, calculation_from_string_data

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit(): #this method will call validate() only if the form is submitted. This is a shortcut for form.is_submitted() and form.validate()
        flash('The calculation performed: %s %s %s' % (form.first_number.data, form.operation.data, form.second_number.data))
        # 1 way: pass result through url_for() as explicit parameter json encoded
        result = calculation(form.first_number.data, form.second_number.data, form.operation.data)
        result = json.dumps(result)
        # 2 way - store the messages into session (cookie) variable before redirecting
        # session['first_number'] = form.first_number.data
        # session['second_number'] = form.second_number.data
        # session['operation'] = form.operation.data
        # flash('From session: %s' % session['result'])
        return redirect(url_for('.result', result=result))
    return render_template('input.html', title='Hello!', form=form)

@app.route('/string-input', methods=['GET', 'POST'])
def input_string():
    form = InputStringForm()
    if form.validate_on_submit():
        flash('The calculation performed: %s' % form.string_data.data)
        session['string_data'] = form.string_data.data
        return redirect(url_for('.result'))
    return render_template('string-input.html', form=form)



@app.route('/result')
def result():
    try:
        result = request.args['result'] #counterpart for url_for() - dispatch args
    # 2 way: get the variable from session before rendering the template
    # first_number = session['first_number']
    # second_number = session['second_number']
    # operation = session['operation']
    # result = calculation(first_number, second_number, operation)
        return render_template('result.html', result=json.loads(result)) # decode json
    except:
        string_data = session['string_data']
        result = calculation_from_string_data(string_data)
        return render_template('result.html', result=result)





