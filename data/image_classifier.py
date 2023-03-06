import requests
import os

# Set the URL to scrape images from
url = "https://www.google.com/search?q=white+bootle+images&tbm=isch&ved=2ahUKEwijsdDwhMf9AhW2HbcAHQzPCuQQ2-cCegQIABAA&oq=white+bootle+images&gs_lcp=CgNpbWcQAzoECCMQJzoJCAAQgAQQChAYUIAGWL8NYKYUaABwAHgAgAFdiAHaBJIBATeYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=vLgFZKPjBba73LUPjJ6roA4&bih=617&biw=1366&rlz=1C1CHBF_enIN1042IN1042#imgrc=gxPLweVSxjdqtM"

# Set the number of images to scrape
num_images = 100

# Set the number of bad images
num_bad_images = 10

# Set the folder paths for storing the images
image_folder = "images/"
good_folder = "images/good/"
bad_folder = "images/bad/"

# Create the folders if they don't exist
if not os.path.exists(image_folder):
    os.mkdir(image_folder)
if not os.path.exists