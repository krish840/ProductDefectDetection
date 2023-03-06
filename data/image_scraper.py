import urllib.request
import os

url = "https://www.google.com/search?q=white+bootle+images&tbm=isch&ved=2ahUKEwijsdDwhMf9AhW2HbcAHQzPCuQQ2-cCegQIABAA&oq=white+bootle+images&gs_lcp=CgNpbWcQAzoECCMQJzoJCAAQgAQQChAYUIAGWL8NYKYUaABwAHgAgAFdiAHaBJIBATeYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=vLgFZKPjBba73LUPjJ6roA4&bih=617&biw=1366&rlz=1C1CHBF_enIN1042IN1042#imgrc=gxPLweVSxjdqtM"
image_dir = "./images"
num_images = 100

# Create the image directory if it doesn't exist
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Download and save each image
for i in range(num_images):
    filename = f"{i+1}.jpg"
    filepath = os.path.join(image_dir, filename)
    urllib.request.urlretrieve(url, filepath)
