# common/play_ringtone

import winsound

class RingtonePlayer:
    def __init__(self, ringtone_file):
        self.ringtone_file = ringtone_file

    def play_finish_ringtone(self):
        # Play a sound when the operation is finished
        winsound.PlaySound(self.ringtone_file, winsound.SND_FILENAME)


