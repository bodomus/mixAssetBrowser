import sys
import hou
import hutil
import json
import requests
import urllib

from hutil.Qt import QtCore
from hutil.Qt import QtGui
from PySide2 import QtNetwork
from hutil.Qt import QtWidgets


class ImgDownloader(QtCore.QObject):
    def __init__(self, parent, req):
        self.req = req
        self.pixmap = QtGui.QPixmap()
        super(ImgDownloader, self).__init__(parent)

    def start_fetch(self, net_mgr):
        self.fetch_task = net_mgr.get(self.req)
        self.fetch_task.finish.connect(self.resolve_fetch)

    def resolve_fetch(self):
        the_reply = self.fetch_task.readAll()
        self.set_widget_image(the_reply)

    def set_widget_image(self, img_binary):
        self.pixmap.loadFromData(img_binary)
        self.parent().setPixmap(self.pixmap)
