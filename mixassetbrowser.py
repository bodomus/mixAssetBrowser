# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import hou
import hutil
import json
import requests
import urllib

from hutil.Qt import QtCore
from hutil.Qt import QtGui
from hutil.Qt import QtWidgets
from PySide2 import QtNetwork

# from hutil.Qt.QtCore import Qt
# https://cdn.polyhaven.com/asset_img/primary/park_parking.png?height=70


class MixAssetBrowser(QtWidgets.QWidget):
    def __init__(self):
        super(MixAssetBrowser, self).__init__()
        print('Hello all')
        self.download_queue = QtNetwork.QNetworkAccessManager()

        main_layout = QtWidgets.QVBoxLayout()
        lbl = QtWidgets.QLabel('label')
        image = QtGui.QImage()
        image.loadFromData(requests.get('https://cdn.polyhaven.com/asset_img/primary/park_parking.png?height=70').content)
        pixmap = QtGui.QPixmap(image)
        lbl.setPixmap(pixmap)


        # main_layout.addWidget(QtWidgets.QPushButton('Hello'))
        main_layout.addWidget(lbl)

        main_layout.setContentsMargins(0, 0, 0, 0)
        # polyhaven stuff
        urls = ['https://cdn.polyhaven.com/asset_img/primary/forest_leaves_03.png?height=70',
                'https://cdn.polyhaven.com/asset_img/primary/dry_mud_field_001.png?height=70',
                'https://cdn.polyhaven.com/asset_img/primary/brown_mud_03.png?height=70']
        url = 'https://api.polyhaven.com/assets?t=hdris&c=outdoor'
        request = requests.get(url)
        data = json.loads(request.content)
        print(data['urban_street_01'])
        self.setLayout(main_layout)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
