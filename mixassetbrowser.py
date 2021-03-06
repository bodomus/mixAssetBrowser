# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import json
import requests
import os
import tempfile
from shutil import copyfile

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtNetwork
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtCore import QTextCodec

from .ImgDownloader import ImgDownloader
from . import preferences
from .flowlayout import FlowLayout

thumb_width = 70
thumb_height = 70
assets_url = 'https://api.polyhaven.com/assets?t=hdris&c=outdoor'
FORM_UI = 'form.ui'

# from hutil.Qt.QtCore import Qt
# https://cdn.polyhaven.com/asset_img/primary/park_parking.png?height=70
# https://api.polyhaven.com/assets?t=hdris&c=outdoor


class MixAssetBrowser(QtWidgets.QWidget):
    def __init__(self):
        super(MixAssetBrowser, self).__init__()

        self.uiLoader = QUiLoader()
        self.prepare_content()
        self.download_queue = QtNetwork.QNetworkAccessManager()

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.content)
        icon_view = QtWidgets.QListWidget()
        icon_view.setViewMode(QtWidgets.QListWidget.IconMode)

        # get Assets icons
        request = requests.get(preferences.getAssetsUrl())
        data = json.loads(request.content)
        # polyhaven stuff

        for url in data.keys():
            img_lbl = QtWidgets.QLabel(data[url]['name'])
            req = QtNetwork.QNetworkRequest(QtCore.QUrl(preferences.getAssetDetailUrl(url, thumb_width)))
            # print(data[url]['name'])
            down = ImgDownloader(img_lbl, req)
            down.start_fetch(self.download_queue)
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(thumb_width + 80, thumb_height + 20))
            icon_view.addItem(item)
            icon_view.setItemWidget(item, img_lbl)

        main_layout.addWidget(icon_view)

        self.setLayout(main_layout)
        f = FlowLayout()
        f1 = FlowLayout()

    def prepare_content(self):
        tempd = tempfile.gettempdir()
        if (not os.path.isdir(tempd)):
            os.mkdir(tempd)
        tempf = os.path.join(tempd, FORM_UI)
        copyfile(self.getUIPath(), tempf)

        try:
            file = QFile(tempf)
            file.open(QFile.ReadOnly)
            self.ui = self.uiLoader.load(file, self)
            self.content = self.ui.contentArea
        finally:
            file.close()

    def getUIPath(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r'qt\assetBrowser\form.ui')

        return os.path.join(os.path.dirname(os.path.abspath(__file__)), r'qt\assetBrowser\form.ui')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
