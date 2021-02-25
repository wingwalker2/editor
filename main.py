from gi.repository import Gtk
import sys

# a Gtk ApplicationWindow


class MainWindow(Gtk.ApplicationWindow):
    # constructor: the title is "Welcome to GNOME" and the window belongs
    # to the application app

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)

        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.vbox)

        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_hexpand(True)
        self.scrolledwindow.set_vexpand(True)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text(
            "Test test!\n"
            )
        self.scrolledwindow.add(self.textview)

        self.create_toolbar()

        self.vbox.pack_start(self.scrolledwindow, True, True, 0)
        self.create_status()

    def create_toolbar(self):
        self.toolbar = Gtk.Toolbar()
        self.vbox.pack_start(self.toolbar, False, False, 0)

        button_bold = Gtk.ToolButton()
        button_bold.set_icon_name("format-text-bold-symbolic")
        self.toolbar.insert(button_bold, 0)

    def create_status(self):
        self.status_frame = Gtk.Frame()
        self.status_box = Gtk.Box()
        self.label = Gtk.Label(xalign=0)
        self.label.set_text("CLICK THE BUTTON")
        self.buttton = Gtk.Button(label="CICK ME")
        self.buttton.connect("clicked", self.on_click)

        self.status_box.pack_start(self.label, True, True, 0)
        self.status_box.pack_start(self.buttton, False, False, 0)

        self.status_frame.set_label("Status")
        self.status_frame.set_shadow_type(Gtk.GTK_SHADOW_IN)
        self.status_frame.add(self.status_box)
        
        self.vbox.pack_start(self.status_frame, False, False, 0)


    def on_click(self, widget):
        print("BUTTON HAS BEEN CLICKED")
        self.textbuffer.insert_at_cursor("BUTTON HAS BEEN CLICKED\n")


class MainApplication(Gtk.Application):
    # constructor of the Gtk Application

    def __init__(self):
        Gtk.Application.__init__(self)

    # create and activate a MyWindow, with self (the MyApplication) as
    # application the window belongs to.
    # Note that the function in C activate() becomes do_activate() in Python
    def do_activate(self):
        win = MainWindow(self)
        win.set_default_size(600, 200)
        # show the window and all its content
        # this line could go in the constructor of MyWindow as well
        win.show_all()

    # start up the application
    # Note that the function in C startup() becomes do_startup() in Python
    def do_startup(self):
        Gtk.Application.do_startup(self)

# create and run the application, exit with the value returned by
# running the program
app = MainApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
