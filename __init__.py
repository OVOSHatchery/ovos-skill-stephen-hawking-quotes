from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.tts.espeak_tts import ESpeak
from os.path import join, dirname


class StephenHawkingTributeSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
        try:
            self.espeak = ESpeak("en-uk", {"voice": "m1"})
        except:
            self.espeak = None

    def initialize(self):
        if self.espeak:
            self.espeak.init(self.bus)
        self.add_event('skill-stephen-hawking.jarbasskills.home', self.homepage)

    def homepage(self):
        utterance = """"
My goal is simple. It is a complete understanding of the universe, why it is as it is and why it exists at all."

-- Stephen Hawking, 1942 - 2018
"""
        self.gui.show_text(utterance)

    def hawking_speak(self, utterance):
        if self.espeak:
            self.espeak.execute(utterance)
        else:
            self.speak(utterance)

    @intent_handler(IntentBuilder("StephenHawkingQuote").require(
        'StephenHawking').require(
        'quote'))
    def handle_quote(self, message):
        utterance = self.dialog_renderer.render("quote", {})
        self.log.info("speak: " + utterance)
        self.hawking_speak(utterance)

        self.gui.clear()
        self.gui.show_image(join(dirname(__file__), "ui", "hawking.jpg"),
                            caption=utterance, fill='PreserveAspectFit')


    @intent_handler(IntentBuilder("StephenHawkingBirth").require(
        'StephenHawking').require(
        'birth'))
    def handle_birth(self, message):
        utterance = self.dialog_renderer.render("birth", {})
        self.speak_dialog(utterance)
        self.gui.clear()
        self.gui.show_image(join(dirname(__file__), "ui", "young_hawking.jpg"),
                            caption=utterance, fill='PreserveAspectFit')

    @intent_handler(IntentBuilder("StephenHawkingDeath").require(
        'StephenHawking').require(
        'death'))
    def handle_death(self, message):
        utterance = self.dialog_renderer.render("death", {})
        self.speak_dialog(utterance)
        self.gui.clear()
        self.gui.show_image(join(dirname(__file__), "ui", "hawking.jpg"),
                            caption=utterance, fill='PreserveAspectFit')

def create_skill():
    return StephenHawkingTributeSkill()
