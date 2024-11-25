import requests
import zipfile
import os


subset = 'https://surfdrive.surf.nl/files/index.php/s/P448UpWEnEkqKKJ/download'
fullset = "https://surfdrive.surf.nl/files/index.php/s/v52aKdVspw5yMJ3/download"

# Download the images from the cloud add print the progress
def download_images(full = False):
    print("Downloading images...")
    _download_image_zip(full)
    print("Download complete!")

    print("Unzipping images...")
    _unzip_images()
    print("Unzip complete!")

    print("Removing zip file...")
    os.remove('data/images.zip')

    print("Done!")

# Download the images from the cloud
def _download_image_zip(full = False):
    global subset, fullset
    url = fullset if full else subset
    r = requests.get(url, allow_redirects=True)
    open('data/images.zip', 'wb').write(r.content)

# Unzip the images using python
def _unzip_images():
    with zipfile.ZipFile('data/images.zip', 'r') as zip_ref:
        zip_ref.extractall('data/')

