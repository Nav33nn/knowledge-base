help:
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run"
	@echo "        Runs the bot on the command line."
	@echo "    all"
	@echo "        Runs all targets together"
	@echo "    clean"
	@echo "        cleans the models."

run:
	make run-actions&
	make run-core

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

run-core:
	python -m rasa_core.run --nlu models/foodiebot/nlu/default/current --core models/foodiebot/dialogue --endpoints endpoints.yml

train-online:
	python -m rasa_core.train  --finetune  -d restaurant_domain.yml -s data/stories.md  --nlu models/foodiebot/nlu/default/current -o models/foodiebot/dialogue --endpoints endpoints.yml


train-nlu:
	python bot.py train-nlu

train-core:
	python bot.py train-dialogue

all: train-nlu train-core run

clean: 
	rm -rf models/
