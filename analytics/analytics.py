Copy code
import sys
import random
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QApplication


class AnalyticsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Analytics")

        tab_widget = QTabWidget()
        tab_widget.addTab(self.get_bar_graph(), "Bar Graph")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def get_bar_graph(self):
        # Generate random percentage values for y-axis and time values for x-axis
        y_data = [random.randint(0, 50) * 2 for i in range(12)]
        x_data = ['9:30', '10:00', '10:30', '11:00', '11:30', '12:00']

        # Create a bar plot
        plt.bar(x_data, y_data)

        # Set the plot title and axis labels
        plt.title('Defect Detection Rate')
        plt.xlabel('Time')
        plt.ylabel('Percentage')

        # Convert the plot to a PySide2 compatible format
        canvas = plt.gcf().canvas
        canvas.draw()

        # Create a QWidget to display the plot in the PySide2 application
        bar_graph = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(canvas.native)
        bar_graph.setLayout(layout)

        return bar_graph


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnalyticsWindow()
    window.show()
    sys.exit(app.exec_())