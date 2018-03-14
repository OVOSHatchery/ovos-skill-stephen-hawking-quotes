from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class StephenHawkingSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('StephenHawking'))
    def handle_stephen_hawking(self, message):
        self.speak_dialog('stephen.hawking')


def create_skill():
    return StephenHawkingSkill()

