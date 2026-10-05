import gi 

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk 

class App(Gtk.Window):
    def __init__(self):
        super().__init__(title="W_switcher")

        box = Gtk.Box()

        prev_btn = Gtk.Button(label="<")
        prev_btn.connect("clicked", lambda x: print("prev yo"))
        box.pack_start(prev_btn, True, True, 0)

        self.add(box)


win = App()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
