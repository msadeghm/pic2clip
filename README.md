# Image to Video Generator  

This Python-based application transforms an image into a video clip by overlaying text, adding background music, and generating a caption with a voiceover narration.  

## Features  
- 📷 **Image Processing**:  
  - Loads an image and applies transformations (grayscale and rotation).
  - Overlays user-defined text on the image.
- 🎞️ **Video Creation**:  
  - Converts the processed image into a video with a duration of 10 seconds.  
  - Adds background music, ensuring it plays throughout the video.  
  - Generates captions and a voiceover narration for the video.  
- ⚙️ **Configurable Options**:  
  - Allows users to specify text, image, and background music via command-line arguments.  

## Installation  

Ensure you have Python installed (preferably 3.8 or later). Then, install the required dependencies:  

```bash
pip install -r requirements.txt
```

## Usage
Run the script with the required parameters:

```bash
python main.py --image "path_to_image.jpg" --text "Your text" --caption "Your caption" --music "path_to_the_music.mp3"
```

## Example Usage:
```bash
python main.py --image "example/test.jpg" --text "Hello!" --caption "Golden sunlight kisses the river, dancing through the trees, as mountains stand tall in peaceful harmony" --music "example/audio.mp3"
```
This will generate a 10-second video with the given image, overlay the text, add background music, generate captions (caption is optional), and create a voiceover narration.

## Project Structure

```
📁 project_root/
│── 📜 main.py              
│── 📜 README.md
│── 📜 requirements.txt
│── 📁 example/
│── 📁 modules/
│   │── 📜 image_processing.py
│   │── 📜 video_generation.py
│   │── 📜 text_to_speech.py
│   │── 📜 utils.py
```

## Notes
* The voiceover narration is generated from the captions but not from the overlaid text on the image.
* FFmpeg must be installed on your system. Download it from FFmpeg.org and ensure it's added to your system PATH.
* Resizing image feature is added and need to be enabled by user in case of need.  


## Contributing
Feel free to fork this repository, improve it, and submit pull requests!

## License
This project is licensed under the MIT License.
