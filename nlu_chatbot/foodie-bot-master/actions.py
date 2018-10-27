from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import zomatopy
import json
import  pickle

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "6ce88a5ec1419e335afa1c7f92f4b739"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        city_id = d1["location_suggestions"][0]["city_id"]
        known_city_ids = pickle.load('data/known_cities_id.pkl','rb')
        if city_id in known_city_ids:            
            cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
                             'south indian': 85}
            results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
            d = json.loads(results)
            response = ""
            if d['results_found'] == 0:
                response = "no results"
            else:
                for restaurant in d['restaurants']:
                    response = response + "Found " + restaurant['restaurant']['name'] + " in " \
                               + restaurant['restaurant']['location']['address'] + "\n"

            dispatcher.utter_message("-----" + response)
        else:
            dispatcher.utter_message("I'm really sorry to say this, but we do not operate in {} yet. Sorry for the inconvinience caused".format(city_name))
        return [SlotSet('location', loc)]


class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        dispatcher.utter_message(tracker.get_slot("matches"))
        dispatcher.utter_message("is it ok for you? "
                                 "hint: I'm not going to "
                                 "find anything else :)")
        return [SlotSet('matches')]

class ActionSendEmail(Action):
    def name(self):
        return 'utter_send_email'

    def run(self, dispatcher, tracker, domain):
        email_id = tracker.get_slot('email')
        textfile = 'message_body.txt'

        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)

        #Next, log in to the server
        server.starttls()
        server.login("bot.foodie.01@gmail.com", "IIITB201802")

        #Send the mail
        mail_subject = 'Restaurant Details'
        config = {"user_key": "6ce88a5ec1419e335afa1c7f92f4b739"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        city_id = get_city_ID(loc)
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        city_id = d1["location_suggestions"][0]["city_id"]
        known_city_ids = pickle.load('data/known_cities_id.pkl','rb')
        if city_id in known_city_ids:            
            cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
                             'south indian': 85}
            results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
            d = json.loads(results)
            response = ""
            if d['results_found'] == 0:
                response = "no results"
            else:
                for restaurant in d['restaurants']:
                    response = response + "Found " + restaurant['restaurant']['name'] + " in " \
                               + restaurant['restaurant']['location']['address'] + "\n"
        else:
            body = 'The city you had selected do not belong to Tier 1 or Tier 2 cities. Apologies extended.'

        body = response
        msg = 'Subject: {}\n\n{}'.format(mail_subject, body)

        server.sendmail("bot.foodie.01@gmail.com", email_id, msg)