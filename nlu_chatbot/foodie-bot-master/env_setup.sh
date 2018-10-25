#!/bin/bash
pip install -r requirements.txt
python -m spacy download en
pip install rasa-core==0.11.12
pip install rasa-core-sdk==0.11.5
pip install rasa-nlu==0.13.7
