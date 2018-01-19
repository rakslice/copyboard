import json
import os

import wx

from copyboard_gui_autogen import MainView


def wx_button_label_escape(text):
    #XX TODO
    return text


def _animate_tween(start_val, end_val, time, duration):
    if isinstance(start_val, wx.Colour):
        assert isinstance(end_val, wx.Colour)
        # return _animate_tween()
        start_tuple = start_val.Get(includeAlpha=True)
        end_tuple = end_val.Get(includeAlpha=True)
        return wx.Colour(*(_animate_tween(x, y, time, duration) for (x, y) in zip(start_tuple, end_tuple)))
    elif isinstance(start_val, float):
        assert isinstance(end_val, float)
        ratio = float(time) / float(duration)
        return start_val * (1.0 - ratio) + end_val * ratio
    elif isinstance(start_val, int):
        assert isinstance(end_val, int)
        left = duration - time
        return (start_val * left + end_val * time) / duration
    else:
        raise ValueError("Don't know how to tween %r" % type(start_val))


class Animator(object):
    def __init__(self, obj, property_name, start_val, end_val, step_time, duration):
        assert step_time > 0
        assert duration > 0
        self.obj = obj
        self.property_name = property_name
        self.start_val = start_val
        self.end_val = end_val
        self.step_time = step_time
        self.duration = duration
        self.time = 0

    def step(self):
        cur_value = _animate_tween(self.start_val, self.end_val, self.time, self.duration)
        setattr(self.obj, self.property_name, cur_value)
        self.time += self.step_time
        if self.time < self.duration:
            wx.CallLater(self.step_time, self.step)


def animate(obj, property_name, from_val=None, to=None, over_ms=None, return_after_ms=None, frame_time=10):
    assert to is not None
    assert over_ms is not None

    if from_val is None:
        from_val = getattr(obj, property_name)

    if return_after_ms is not None:
        wx.CallLater(return_after_ms, lambda: animate(obj, property_name, from_val=to, to=from_val, over_ms=over_ms))

    ani = Animator(obj, property_name, from_val, to, frame_time, over_ms)
    ani.step()


class MainViewImpl(MainView):
    def __init__(self, *args, **kwargs):
        super(MainViewImpl, self).__init__(*args, **kwargs)
        self.copy_strings_list = None
        self.last_loaded_obj = None
        self.id_index_map = None
        """:type: list of unicode"""
        self.last_clipboard_obj = None
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        self.save_geometry_settings(self.last_loaded_obj)
        self.Destroy()

    def init_with_settings(self, last_loaded_obj):
        self.last_loaded_obj = last_loaded_obj

        self.load_geometry_settings(last_loaded_obj)

        self.copy_strings_list = last_loaded_obj["strings"]
        self._create_buttons()

    def load_geometry_settings(self, settings):
        position = settings.get("position")
        if position:
            self.SetPosition(wx.Point(*position))
        size = settings.get("size")
        if size:
            self.SetSize(wx.Size(*size))

    def save_geometry_settings(self, settings):
        pos = self.Position
        assert isinstance(pos, wx.Point)
        size = self.Size
        assert isinstance(size, wx.Size)
        settings["position"] = pos.Get()
        settings["size"] = size.Get()

    def _create_buttons(self):
        self.id_index_map = {}
        for i, copy_string in enumerate(self.copy_strings_list):
            button_id = self.NewControlId()
            self.id_index_map[button_id] = i
            cur_copy_button = wx.Button(self.panel_copybuttons, button_id, copy_string)
            # item, proportion, flag, boarder
            self.sizer_copybuttons.Add(cur_copy_button, 0, wx.EXPAND, 0)
            self.Bind(wx.EVT_BUTTON, self._copy_button_click, cur_copy_button)
        # self.sizer_copybuttons.Fit(self)
        # self.Layout()

    def _clear_buttons(self):
        buttons = list(self.sizer_copybuttons.GetChildren())
        for button in buttons:
            assert isinstance(button, wx.Button)
            del self.id_index_map[button.GetId()]
            self.Unbind(wx.EVT_BUTTON, handler=self._copy_button_click, source=button)
            self.sizer_copybuttons.Remove(button)

    def _copy_button_click(self, event):
        """:type event: wx.CommandEvent"""

        index = self.id_index_map[event.GetId()]
        text = self.copy_strings_list[index]

        obj = event.EventObject
        assert isinstance(obj, wx.Button)

        self.copy_text(text)
        animate(obj=obj, property_name="BackgroundColour", to=wx.Colour(95, 186, 125, 255), over_ms=100, return_after_ms=700, frame_time=20)

    def copy_text(self, text):
        self.last_clipboard_obj = wx.TextDataObject()
        self.last_clipboard_obj.SetText(text)
        with wx.Clipboard.Get() as clipboard:
            clipboard.SetData(self.last_clipboard_obj)

    def button_edit_click(self, event):
        pass


class AppLogic(object):
    def __init__(self):
        script_path = os.path.dirname(os.path.abspath(__file__))
        self.json_filename = os.path.join(script_path, "copystrings.json")
        self.last_loaded_obj = None
        self.load_file()

    def load_file(self):
        # noinspection PyBroadException
        try:
            with open(self.json_filename, "rb") as handle:
                self.last_loaded_obj = json.load(handle)
            copy_strings_list = self.last_loaded_obj["strings"]
            assert isinstance(copy_strings_list, list)
            assert all(isinstance(x, unicode) for x in copy_strings_list)
        except:
            self.last_loaded_obj = {"strings": []}

    def start_gui(self):
        app = wx.App()
        frame = MainViewImpl(None)
        frame.init_with_settings(self.last_loaded_obj)
        frame.Show()
        app.MainLoop()

    def save(self):
        temp_filename = self.json_filename + ".new"
        with open(temp_filename, "wb") as handle:
            json.dump(self.last_loaded_obj, handle)
        os.remove(self.json_filename)
        os.rename(temp_filename, self.json_filename)


def main():
    name = "copyboard-%s" % wx.GetUserId()
    instance = wx.SingleInstanceChecker(name)
    if instance.IsAnotherRunning():
        return
    app_logic = AppLogic()
    app_logic.start_gui()
    app_logic.save()


if __name__ == "__main__":
    main()

    # texts to copy load from an optional json.

    # Main view:
    # a list of copy buttons for each copy text with the text on the button
    # when you click on a copy button
    # - it copies the text to the clipboard
    # - it goes green
    # - a fraction of a second later it goes back to normal
    # there is an edit button; this flips to edit view
    #
    # Edit View:
    # - there is an edit box in the place of each button which allows editing the text
    # - edit button changes to save
    # - there is also a cancel button and an add button
