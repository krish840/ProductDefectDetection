import os
import random
from PySide2 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient

class ImageGallery(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Gallery")

        # Connect to database
        self.client = MongoClient()
        self.db = self.client['switchon']

        # Create UI
        self.layout = QtWidgets.QVBoxLayout()
        self.button_layout = QtWidgets.QHBoxLayout()
        self.all_button = QtWidgets.QPushButton("All")
        self.good_button = QtWidgets.QPushButton("Good")
        self.bad_button = QtWidgets.QPushButton("Bad")
        self.button_layout.addWidget(self.all_button)
        self.button_layout.addWidget(self.good_button)
        self.button_layout.addWidget(self.bad_button)
        self.layout.addLayout(self.button_layout)
        self.image_layout = QtWidgets.QGridLayout()
        self.layout.addLayout(self.image_layout)
        self.setLayout(self.layout)

        # Connect signals and slots
        self.all_button.clicked.connect(lambda: self.display_images("all"))
        self.good_button.clicked.connect(lambda: self.display_images("good"))
        self.bad_button.clicked.connect(lambda: self.display_images("bad"))

        # Display all images
        self.display_images("all")

    def display_images(self, status):
        # Clear existing images
        for i in reversed(range(self.image_layout.count())):
            self.image_layout.itemAt(i).widget().setParent(None)

        # Load images based on status
        if status == "all":
            image_list = self.db.image_data.find()
        else:
            image_list = self.db.image_data.find({"status": status})

        # Display images
        for idx, image_data in enumerate(image_list):
            image_file = os.path.join(os.path.dirname(__file__), "..", "data", "images", f"{image_data['unit_id']}.jpg")
            pixmap = QtGui.QPixmap(image_file)
            label = QtWidgets.QLabel()
            label.setPixmap(pixmap)
            if image_data['status'] == "good":
                label.setStyleSheet("border: 4px solid green;")
            else:
                label.setStyleSheet("border: 4px solid red;")
            self.image_layout.addWidget(label, idx//10, idx%10)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    image_gallery = ImageGallery()
    image_gallery.show()
    app.exec_()