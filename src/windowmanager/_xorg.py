import Xlib
from Xlib.display import Display

from ._base import AbstractWindowManager
import logger


# TODO check and raiseError
def _check_conn_to_xserver():
    display = Xlib.display.Display()
    display.close()


_check_conn_to_xserver()
del _check_conn_to_xserver


class WindowManager(AbstractWindowManager):
    def __init__(self):
        super(WindowManager, self).__init__()
        self.disp = Display()
        self.root = self.disp.screen().root
        self._listen_for_window_property_changes()

        self.NET_ACTIVE_WINDOW = self.disp.intern_atom('_NET_ACTIVE_WINDOW')

        self._active_window = None
        self._update_active_window()

    def run(self):
        self.notify_all()
        while True:  # next_event() sleeps until we get an event
            self._handle_xevent(self.disp.next_event())

    def get_active_program_name(self):
        try:
            return self._active_window.get_wm_class()[1]
        except e:
            logger.exeption(e)
            return 'FAILED'

    def _handle_xevent(self, event):
        if event.type != Xlib.X.PropertyNotify:
            return

        if event.atom == self.NET_ACTIVE_WINDOW:
            if self._update_active_window():
                self.notify_all()

    def _update_active_window(self):
        active_win_id = self.root.get_full_property(self.NET_ACTIVE_WINDOW,
                                                    Xlib.X.AnyPropertyType).value[0]
        if self._has_focus_changed(active_win_id):
            new_win = self._window_obj(active_win_id)
            if new_win:
                if self._active_window:
                    self._active_window.change_attributes(event_mask=Xlib.X.NoEventMask)

                self._active_window = new_win
                self._active_window.change_attributes(event_mask=Xlib.X.PropertyChangeMask)
                return True
        return False

    def _listen_for_window_property_changes(self):
        self.root.change_attributes(event_mask=Xlib.X.PropertyChangeMask)

    def _window_obj(self, xid):
        window_obj = None
        if xid:
            try:
                window_obj = self.disp.create_resource_object('window', xid)
            except Xlib.error.XError:
                pass
        return window_obj

    def _has_focus_changed(self, active_win_xid):
        if self._active_window:
            return active_win_xid != self._active_window.id
        return True
