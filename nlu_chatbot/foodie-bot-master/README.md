# foodie-bot
## Installation Steps

# Run the environment setup
./env_setup.sh

# Train NLU
python bot.py train-nlu

# Train Dialogue
python bot.py train-dialogue

# start the action listener on terminal one
python -m rasa_core_sdk.endpoint --actions actions

# start bot on new terminal 
python -m rasa_core.run --nlu models/foodiebot/nlu/default/current --core models/foodiebot/dialogue --endpoints endpoints.yml

#optional step: if you want to train little more
python -m rasa_core.train  --online  -d restaurant_domain.yml -s data/stories.md  --nlu models/foodiebot/nlu/default/current -o models/foodiebot/dialogue --endpoints endpoints.yml

