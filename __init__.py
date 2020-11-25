from mycroft import MycroftSkill, intent_file_handler


class LaunchScript(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('script.launch.intent')
    def handle_script_launch(self, message):
        self.speak_dialog('script.launch')


def create_skill():
    return LaunchScript()

