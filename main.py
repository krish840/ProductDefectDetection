from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, \
    QLabel, QPushButton, QComboBox, QScrollArea
from PySide2.QtCore import Qt
from analytics.image_gallery import ImageGallery
from data.database.database import Database
import pymongo


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create database connection
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["switchon"]

        # Set window title and size
        self.setWindowTitle("SwitchOn Desktop Application")
        self.setMinimumSize(800, 600)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create layout for central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create tab widget
        tab_widget = QTabWidget()
        layout.addWidget(tab_widget)

        # Create analytics tab
        analytics_tab = QWidget()
        analytics_layout = QVBoxLayout()
        analytics_tab.setLayout(analytics_layout)

        # Add widgets to analytics tab
        analytics_layout.addWidget(QLabel("Analytics"))
        analytics_layout.addWidget(QPushButton("Refresh"))
        
        # Add bar graph to analytics tab
        database = Database(self.db)
        analytics_data = database.get_analytics_data()
        bar_graph = BarGraph(analytics_data)
        analytics_layout.addWidget(bar_graph)

        # Add analytics tab to tab widget
        tab_widget.addTab(analytics_tab, "Analytics")

        # Create image gallery tab
        image_gallery_tab = QWidget()
        image_gallery_layout = QVBoxLayout()
        image_gallery_tab.setLayout(image_gallery_layout)

        # Create filter widgets for image gallery
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Filter:"))
        filter_combo_box = QComboBox()
        filter_combo_box.addItems(["All", "Good", "Bad"])
        filter_layout.addWidget(filter_combo_box)
        image_gallery_layout.addLayout(filter_layout)

        # Add scroll area to image gallery tab
        scroll_area = QScrollArea()
        image_gallery_layout.addWidget(scroll_area)

        # Add image gallery to scroll area
        image_gallery = ImageGallery(self.db)
        scroll_area.setWidget(image_gallery)

        # Connect filter combo box to image gallery
        filter_combo_box.currentTextChanged.connect(image_gallery.filter_images)

        # Add image gallery tab to tab widget
        tab_widget.addTab(image_gallery_tab, "Image Gallery")


if __name__ == "__main__":
    # Create Qt application
    app = QApplication([])

    # Create main window
    window = MainWindow()
    window.show()

    # Run event loop
    app.exec_()