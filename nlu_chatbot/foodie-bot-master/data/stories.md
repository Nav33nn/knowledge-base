## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export
## Generated Story -1371393708137348274
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - utter_ask_price_range
* price_check{"range": "between"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_id
* send_email{"email": "reghuram.rv@gmail.com"}
    - slot{"email": "reghuram.rv@gmail.com"}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye

## Generated Story -188370696778953598
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_check{"range": "-"}
    - slot{"range": "-"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email_id
* send_email{"email": "reghuram.rv@gmail.com"}
    - slot{"email": "reghuram.rv@gmail.com"}
    - action_send_email
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye

## Generated Story 8104540199928037149
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_price_range
* price_check
    - utter_ask_price_range
    - utter_ask_price_range
* price_check{"price": "300"}
    - slot{"price": "300"}
    - utter_ask_price_range
* price_check{"range": "-"}
    - slot{"range": "-"}
    - action_search_restaurants
    - slot{"location": "chennai"}
* send_email
    - utter_ask_email_id
* send_email{"email": "reghuram.rv@gmail.com"}
    - slot{"email": "reghuram.rv@gmail.com"}
    - utter_ask_howcanhelp

## Generated Story -3483316133665423216
* restaurant_search{"cuisine": "mexican", "location": "mumbai", "range": "between"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_id
* send_email{"email": "reghuram.rv@gmail.com"}
    - slot{"email": "reghuram.rv@gmail.com"}
    - action_send_email
    - utter_ask_howcanhelp
* deny
    - utter_goodbye

## Generated Story -5274105035582188331
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* price_check{"range": "between"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* send_email{"email": "reghuram.rv@gmail.com"}
    - slot{"email": "reghuram.rv@gmail.com"}
    - action_send_email
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye


