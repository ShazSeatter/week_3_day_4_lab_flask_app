from models.event import *
import datetime

event1 = Event(datetime.date(2023, 6, 25), "Wedding", 30, "Event Room A", "Wedding for John and Jane")
event2 = Event(datetime.date(2023, 3, 10), "Conference", 50, "Conference Hall", "Business Conference")
event3 = Event(datetime.date(2023, 3, 7), "Birthday", 10, "Event Room B", "Jack's 10th Birthday Party")


events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)


# def delete_selected_event(event_name):
#     event_to_delete = None
#     for event in events:
#         if event.name == event_name:
#             event_to_delete = event
#             break

#     events.remove(event_to_delete)