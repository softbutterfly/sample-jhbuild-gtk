import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

css = b"""
#hello_world_window {
    background-color: red;
}

#hello_world_button {
    background-color: blue;
}
"""

style_provider = Gtk.CssProvider()
style_provider.load_from_data(css)


class HelloWorldWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Linux at PUCP")

        self.set_name('hello_world_window')
        self.set_border_width(10)


        self.button = Gtk.Button(label="Go to linux playa!!")
        self.button.set_name('hello_world_button')
        self.button.connect("clicked", self.on_button_clicked)

        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello Linux at PUCP!! :D")


def main():
    win = HelloWorldWindow()

    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
