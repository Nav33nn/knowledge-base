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
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
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
    - utter_ask_price_range
* price_check{"range": "between"}
    - slot{"range": "between"}
    - action_search_restaurants
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
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
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
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
    - utter_ask_price_range
* price_check{"range": "between"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - export


## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_check{"range": "between"}
    - slot{"range": "between"}
    - action_search_restaurants
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
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
    - utter_email_send_confirmation
* affirm
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
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_email_send_confirmation
* affirm
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
* price_check{"price": "300"}
    - slot{"price": "300"}
    - utter_ask_price_range
* price_check{"range": "-"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_email_send_confirmation
* affirm
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
    - utter_email_send_confirmation
* affirm
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
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "reghuram.rv@gmail.com"}
    - slot{"email": "reghuram.rv@gmail.com"}
    - action_send_email
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye


## Generated Story 633930060048726669
* restaurant_search{"location": "bangalore", "cuisine": "chinese", "range": "between"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - action_send_email
    - utter_goodbye

## Generated Story 4291709115114936574
* restaurant_search{"location": "bangalore", "range": "between", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_goodbye

## Generated Story -5201673030082883406
* restaurant_search{"cuisine": "chinese", "location": "bangalore", "range": "between"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - action_send_email
    - utter_goodbye

## Generated Story 3670796697931885406
* restaurant_search{"cuisine": "chinese", "range": "between", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_goodbye

## Generated Story 106966901103757368
* restaurant_search{"range": "between", "cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc007@gmail.com"}
    - slot{"email": "abc007@gmail.com"}
    - action_send_email
    - utter_goodbye

## Generated Story -7648841222212364292
* restaurant_search{"range": "between", "location": "bangalore", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"range": "between"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "d.s007@gmail.com"}
    - slot{"email": "d.s007@gmail.com"}
    - action_send_email
    - utter_goodbye


## Generated Story -3496581748033414984
* restaurant_search{"location": "bangalore", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - utter_ask_price_range
* restaurant_search{"price": "300"}
    - slot{"price": "300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_goodbye

## Generated Story -4893720700486910855
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - utter_ask_price_range
* price_check{"range": "more"}
    - slot{"range": "more"}
    - slot{"price": "700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_goodbye

## Generated Story 5336218531095077697
* restaurant_search{"location": "bangalore", "range": "between"}
    - slot{"location": "bangalore"}
    - slot{"range": "between"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_goodbye

## Generated Story -4114385369068410516
* restaurant_search{"range": "between", "location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"range": "between"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* deny
    - utter_goodbye

## Generated Story -4788423261798420954
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* price_check{"range": "more", "price": "700"}
    - slot{"price": "700"}
    - slot{"range": "more"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "dipesh.singhal@gmail.com"}
    - slot{"email": "dipesh.singhal@gmail.com"}
    - action_send_email
    - utter_goodbye


## Generated Story -8544261640449368810
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* price_check{"range": "more"}
    - slot{"range": "more"}
    - slot{"price": "700"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "nav33nn92@gmail.com"}
    - slot{"email": "nav33nn92@gmail.com"}
    - action_send_email
    - slot{"location": "chennai"}
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye

## Generated Story 7998468385428889827
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* price_check{"range": "less than"}
    - slot{"range": "less"}
    - slot{"price": "300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_email_send_confirmation
* deny
    - utter_goodbye

## Generated Story 1816799016789453470
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price_range
* price_check{"range": "more", "price": "700"}
    - slot{"price": "700"}
    - slot{"range": "more"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "bcd@gmail.com"}
    - slot{"email": "bcd@gmail.com"}
    - action_send_email
    - slot{"location": "delhi"}
    - utter_goodbye

## Generated Story 599768256890217234
* restaurant_search{"range": "less", "price": "300"}
    - slot{"price": "300"}
    - slot{"range": "less"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_email_send_confirmation
* deny
    - utter_goodbye

## Generated Story -92993947683901549
* restaurant_search{"range": "more", "price": "700"}
    - slot{"price": "700"}
    - slot{"range": "more"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "dip040708@gmail.com"}
    - slot{"email": "dip040708@gmail.com"}
    - action_send_email
    - slot{"location": "kolkata"}
    - utter_goodbye

## Generated Story 4358061991144644977
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* price_check{"range": "Less", "price": "300"}
    - slot{"price": "300"}
    - slot{"range": "Less"}
    - action_search_restaurants
    - slot{"location": "indore"}
    - utter_email_send_confirmation
* deny
    - utter_goodbye

## Generated Story -8522128277739239398
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* price_check{"range": "more", "price": "700"}
    - slot{"price": "700"}
    - slot{"range": "more"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_email_send_confirmation
* affirm
    - utter_ask_email_id
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - slot{"location": "chennai"}
    - utter_goodbye

## Generated Story 4053657311894282044
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "dehradoon"}
    - slot{"location": "dehradoon"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_check{"range": "less than", "price": "300"}
    - slot{"price": "300"}
    - slot{"range": "less"}
    - action_search_restaurants
    - slot{"location": "dehradoon"}
    - utter_email_send_confirmation
* deny
    - utter_goodbye

## Generated Story -5409371390447508982
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "shimla"}
    - slot{"location": "shimla"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_check{"range": "less than", "price": "300"}
    - slot{"price": "300"}
    - slot{"range": "less"}
    - action_search_restaurants
    - slot{"location": "shimla"}
    - utter_goodbye

