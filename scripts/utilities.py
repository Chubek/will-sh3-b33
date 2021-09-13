import gdown

def download_gdown(url, path):
    gdown.download(url, path, quiet=False)