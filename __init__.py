from os.path import join, dirname
from tempfile import gettempdir

from ovos_workshop.decorators import intent_handler
from ovos_workshop.intents import IntentBuilder
from ovos_workshop.skills import OVOSSkill


class StephenHawkingTributeSkill(OVOSSkill):

    def initialize(self):
        try:
            from ovos_tts_plugin_espeakng import EspeakNGTTS
            self.espeak = EspeakNGTTS()
            self.espeak.init(self.bus)
        except:
            self.espeak = None

    def hawking_speak(self, utterance):
        if self.espeak:
            tts, _ = self.espeak.get_tts(utterance, f"{gettempdir()}/hawk_{utterance[:6]}.wav")
            self.play_audio(tts)
        else:
            self.speak(utterance, wait=True)

    @intent_handler(IntentBuilder("StephenHawkingQuote").
                    require('StephenHawking').require('quote'))
    def handle_quote(self, message):
        utterance = self.dialog_renderer.render("quote", {})
        self.log.info("speak: " + utterance)
        self.gui.show_image(join(dirname(__file__), "ui", "hawking.jpg"),
                            caption=utterance,
                            fill='PreserveAspectFit')
        self.hawking_speak(utterance)
        self.gui.release()

    @intent_handler(IntentBuilder("StephenHawkingBirth").
                    require('StephenHawking').require('birth'))
    def handle_birth(self, message):
        utterance = self.dialog_renderer.render("birth", {})
        self.gui.show_image(join(dirname(__file__), "ui", "young_hawking.jpg"),
                            caption=utterance,
                            fill='PreserveAspectFit')
        self.speak(utterance, wait=True)
        self.gui.release()

    @intent_handler(IntentBuilder("StephenHawkingDeath").
                    require('StephenHawking').require('death'))
    def handle_death(self, message):
        utterance = self.dialog_renderer.render("death", {})
        self.gui.show_image(join(dirname(__file__), "ui", "hawking.jpg"),
                            caption=utterance,
                            fill='PreserveAspectFit')
        self.speak(utterance, wait=True)
        self.gui.release()
