import shutil


def load_data(*args):
    """
    The function load data to storage directory
    """
    for file in args:
        if file:
            file_location = f"storage/{file.filename}"
            with open(file_location, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
