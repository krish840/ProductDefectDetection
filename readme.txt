Documentation for Product Defect Detection System

Introduction
The Product Defect Detection System is a desktop application developed in Python 3 using the PySide2 library and MongoDB NoSQL database. It is designed to catch defects in products as they pass by on an assembly line by matching images of the products taken by a camera with images of known good parts. This system has two main functionalities, which are:

Analytics: Displays a bar graph of product quality over time.
Image Gallery: Displays product images with a red or green line indicating whether they are good or bad.
Folder Structure
The folder structure for this project is as follows:

project/
data/
database/
database.py
images/
good/
bad/
image_scraper.py
image_classifier.py
image_data_loader.py
analytics/
image_gallery.py
main.py
Dependencies
The following dependencies need to be installed to run this project:

PySide2
pymongo
How to Run the Application
To run the Product Defect Detection System, navigate to the project directory and run the following command:

css
Copy code
python main.py
This will start the application and display the main window, which has two tabs: Analytics and Image Gallery. Clicking on the Analytics tab will display a bar graph of product quality over time. Clicking on the Image Gallery tab will display product images with a red or green line indicating whether they are good or bad.

Functionality
The Product Defect Detection System has the following functionality:

Analytics:
Displays a bar graph of product quality over time.
The y-axis displays percentages from 0-100 in intervals of 5.
The x-axis displays time from 9:30-12:00 in intervals of 30 minutes.
Image Gallery:
Displays 100 product images.
Each image has a red or green line indicating whether it is good or bad.
Images can be filtered to display all, good, or bad products.
Scroll functionality is implemented to allow users to view all images.
Data
The Product Defect Detection System generates a dataset with the following format:

SKU Id, Unit Id, Status

SKU ID is a unique id for one kind of unit. It should be changed in case you are adding support for multiple kinds of products in your GUI.
Unit ID is an incrementing ID
Status is the output of the inspection, which will either be “Good” or “Bad”.
At least 100 image entries are created.
10% of the units are “Bad” and the remaining are “Good”.
The distribution of “Bad” units is random and uniform, which means that the good and the bad are interspersed in a uniform manner.
Product images are stored in a folder, and the image names are the Unit Id. The images are stored in two subfolders: good and bad.

Conclusion
The Product Defect Detection System is a simple desktop application that can help catch defects in products as they pass by on an assembly line. It has two main functionalities: Analytics and Image Gallery. The application is designed to be easy to use, and all product images are classified as good or bad.