from PySide2 import QtWidgets, QtGui
import config
import server  # DON`T REMOVE
from get_image import GetImageFromServer


def client():
    path_to_image = config.IMAGE_PATH
    GetImageFromServer(config.HOST, config.PORT, path_to_image)
    return path_to_image


def main():
    path = client()
    app = QtWidgets.QApplication([])
    label = QtWidgets.QLabel()
    label.setMinimumSize(100, 100)
    label.setPixmap(QtGui.QPixmap(path))
    label.show()
    app.exec_()


if __name__ == '__main__':
    main()
