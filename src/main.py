from gi.repository import Gtk
from gui.criptografia_gui import cripto_janela

CriptoKey = cripto_janela()
CriptoKey.connect("delete-event", Gtk.main_quit)
CriptoKey.set_resizable(False)

CriptoKey.show_all()
Gtk.main()