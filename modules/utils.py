import os

def validate_inputs(image_path, music_path):

    """
    Validates_inputs function checks in input files exist and they have correct format

    Input Parameters
        image_path(str): Path to the image
        music_path(str):  Path to music file
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError("Error: Image file is not found")

    if not os.path.exists(music_path):
        raise FileNotFoundError("Error: Music file is not found")

    if not music_path.lower().endswith(".mp3"):
        raise ValueError("Error: Music file must be an mp3 file")
