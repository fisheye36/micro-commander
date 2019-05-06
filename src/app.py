from conf import settings


class Application:
    def start(self):
        settings.load_configuration()
        settings.save_configuration()
        print(settings['language'])


if __name__ == "__main__":
    a = Application()
    a.start()
