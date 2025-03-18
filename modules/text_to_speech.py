from gtts import gTTS

def generate_narration(caption, output_audio="example/output_narration.mp3"):

    """
    The generate_narration function converts the input text to speech and save it as a MP3 file

    Input Parameters
        caption(str): Input caption
        output_audio(str):  Path to save the created audio from the text

    Return Parameters:
        str: Path of the created audio

    Refrence:
        https://gtts.readthedocs.io/en/latest/
    """

    tts = gTTS(text=caption, lang="en")
    tts.save(output_audio)
    return output_audio
