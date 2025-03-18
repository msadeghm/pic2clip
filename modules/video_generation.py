import ffmpeg

def create_video(image_path, narration_path, music_path, output_path="example/output.mp4"):

    """
    The create_video function generate the video file using the image, backgrund music and narration.

    Input Parameters
        image_path(str): Path to the image
        narration_audio(str):  Path to narration_audio
        music_audio(str): Path to the music audio

    Return Parameters:
        str: Path of the created video

    Refrence:
        https://github.com/jiashaokun/ffmpeg
    """

    duration = 10
    video = ffmpeg.input(image_path, loop=1, t=duration, framerate=1)
    narration = ffmpeg.input(narration_path)

    music = (
        ffmpeg.input(music_path, stream_loop=-1)
        .filter("atrim", duration=duration)
        .filter("asetpts", "PTS-STARTPTS")
    )

    mixed_audio = ffmpeg.filter([narration, music], "amix", duration="longest", dropout_transition=0)
    output = ffmpeg.output(video, mixed_audio, output_path, vcodec="libx264", acodec="aac", strict="experimental")
    ffmpeg.run(output)
    return output_path
