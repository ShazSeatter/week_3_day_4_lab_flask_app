from flask import render_template, request, redirect
from app import app
from models.event_list import events, add_new_event
from models.event import *
import datetime

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events/new')
def new_event():
    return render_template('new_event.html', title="New Event")

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['name']
    event_guest = request.form['guest']
    event_location = request.form['location']
    event_date = request.form['event-date']
    split_date = event_date.split('-')
    new_year = int(split_date[0])
    new_month = int(split_date[1])
    new_day = int(split_date[2])
    new_date = datetime.date(new_year, new_month, new_day)
    print(new_date)
    event_desc = request.form['description']
    new_event = Event(new_date, event_name, event_guest, event_location, event_desc)
    add_new_event(new_event)
    return redirect('/events')

# @app.route('/events/delete/<index>', methods=['POST'])
# def delete_event(index):
#     delete = events(index)
#     delete_selected_event(delete)
#     return render_template('index.html', event=delete)