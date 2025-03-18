import argparse
from modules.image_processing import process_image
from modules.text_to_speech import generate_narration
from modules.video_generation import create_video
from modules.utils import validate_inputs

def main():
    """
    Example Usage:
    --------------
    To generate a video from an image with background music and a caption, run:

    python main.py --image "example/test.jpg" --text "Hello!" --caption "Golden sunlight kisses the river, dancing through the trees, as mountains stand tall in peaceful harmony"--music "example/audio.mp3"

    This will:
    - Process the image (apply grayscale and rotation to the image and overlay the text).
    - Generate voiceover narration for the provided text.
    - Create a 10-second video with background music and caption.
    - Save the final video as 'output.mp4'.

    Refrence: https://docs.python.org/3/library/argparse.html
    """



    parser=argparse.ArgumentParser(description="Generated Video From an Image")
    parser.add_argument("--image", required=True, help="Path to the image file")
    parser.add_argument("--text", required=True, default="Text to overlay on image",
                        help="Text input from User to overlay on the video")
    parser.add_argument("--music", required=True, help="Path to the music file")
    parser.add_argument("--caption", default="Caption to Dscribe the Generated Video",
                        help="Text input from User to overlay on the video")

    args=parser.parse_args()
    validate_inputs(args.image, args.music)
    prossesed_image = process_image(args.image, args.text)
    narration = generate_narration(args.caption)
    video = create_video(prossesed_image, narration, args.music)
    print("Video successfullay has been created")

if __name__ == "__main__":
    main()


