import sys

WindowManager = None

if sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
    # http://stackoverflow.com/a/373310/562769
    raise ImportError('this platform is not supported')

# elif sys.platform in ['Windows', 'win32', 'cygwin']:
#     from windowmanager._win32 import WindowManager
#         http://stackoverflow.com/a/608814/562769
#         import win32gui
#         window = win32gui.GetForegroundWindow()
#         active_window_name = win32gui.GetWindowText(window)

else:
    from windowmanager._xorg import WindowManager

if not WindowManager:
    raise ImportError('this platform is not supported')

if __name__ == "__main__":
    class DummyObserver:
        def notify(self, program_name):
            print(program_name)

    ob = DummyObserver()
    w = WindowManager()
    w.subscribe(ob)
    w.start()
