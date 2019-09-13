import logger


class Distributor:
    def __init__(self, analyser, keyboard):
        self.analyser = analyser
        self.keyboard = keyboard

    def interim(self, transcript, corrected_time):
        logger.debug("[{}] INTERIM: {}".format(corrected_time, transcript))


    def final(self, transcript):
        logger.info("FINAL: {}".format(transcript))
        analyzed_keys = self.analyser.analyse(transcript)
        self.keyboard.simulate(analyzed_keys)
