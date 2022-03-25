"""
Discord script for polybar module.
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from os import popen

app = gtk.Window()
app.set_title('DiscordPolybarModule')
app.resize(130, 100)
app.move(1680/2 - 130/2, 50)
box = gtk.VBox(spacing=4)

show = gtk.Button(label='Show')
close = gtk.Button(label='Close')

bd = gtk.HBox(spacing=4)

inject = gtk.Button(label='>')
remove = gtk.Button(label='<')

show.connect('clicked', lambda *_: popen('discord &') + app.destroy())
close.connect('clicked', lambda *_: popen('killall Discord && killall Discord') + app.destroy())

inject.connect('clicked', lambda *_: popen('betterdiscordctl install && echo || betterdiscordctl reinstall'))
remove.connect('clicked', lambda *_: popen('betterdiscordctl uninstall'))

box.add(gtk.Label('Discord'))
box.add(show)
box.add(close)
box.add(gtk.Label('BetterDiscord'))
bd.add(inject)
bd.add(remove)
box.add(bd)

app.connect('delete-event', gtk.main_quit)
app.connect('destroy', gtk.main_quit)

app.add(box)
app.show_all()
gtk.main()
