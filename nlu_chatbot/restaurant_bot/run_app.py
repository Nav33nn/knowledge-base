from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.slack import SlackInput
from rasa_core.channels.console import CmdlineInput;


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-359418684578-360311923670-373479391381-faf4e29bddac4cd131221b8cf0ffa627', #app verification token
							#'xoxb-359418684578-372796513233-gHxeV6CHQFl8MPkZVrPHBsnQ', # bot verification token
							#'7uAoXNmNANaqCa9WpALV9EhR', # slack verification token
							True)
cmd_channel = CmdlineInput()

agent.handle_channels(channels=[input_channel, cmd_channel], http_port=5004, serve_forever=True)