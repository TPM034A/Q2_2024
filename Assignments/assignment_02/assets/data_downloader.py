import requests
import zipfile
import os

''
data = 'https://surfdrive.surf.nl/files/index.php/s/cTSkg6imbGeyIEP/download'

# Download the images from the cloud add print the progress
def download_data():
    print("Downloading data folder...")
    _download_data_zip()
    print("Download complete!")

    print("Unzipping the folder...")
    _unzip_folder()
    print("Unzip complete!")

    print("Removing zip file...")
    os.remove('data.zip')

    print("Done!")

# Download the folder from the cloud
def _download_data_zip():
    global data
    r = requests.get(data, allow_redirects=True)
    open('data.zip', 'wb').write(r.content)

# Unzip the images using python
def _unzip_folder():
    with zipfile.ZipFile('data.zip', 'r') as zip_ref:
        zip_ref.extractall('')

