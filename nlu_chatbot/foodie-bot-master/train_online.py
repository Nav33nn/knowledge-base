from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)


def run_restaurant_online(input_channel, interpreter,
                          domain_file="restaurant_domain.yml",
                          training_data_file='data/stories.md'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=interpreter)

    agent.train_online(training_data_file,
                       input_channel=input_channel,
                       max_history=2,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/foodiebot/nlu/default/current')
    print(nlu_interpreter.parse(u"Send an email on reghuram.rv@abc.com"))
