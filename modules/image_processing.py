from PIL import Image, ImageDraw, ImageFont

def process_image(image_path, text="Generated Video From an Image", output_path="example/output_image.jpg",
                  grayescale=True, resize=None, rotate_angle=20):
    """
    The process_image function loads the image selected by user and applies
    selected and defined transformations according the user choices

    Input Parameters:
        image_path(str): Path to the image
        text(str): Text (caption) to overlay on the image
        out_put_path(str): Path to save the transformed image
        grayescale(bool): Convert image to grayescale if it is 'True'
        resize(tuple): Resize image to (w, h) if the tuple value is defined
        rotate_angle(float): Rotate image by specified degrees. If >360, it will use reminder of divition by 360

     Return Parameters:
        str: Path of the transformed image

    Refrences:
        https://pillow.readthedocs.io/en/stable/index.html
    """

    image = Image.open(image_path)

    if grayescale:
        try:
            image=image.convert("L")
        except OSError:
            print("Image can't be transformed to grayscale")

    if resize:
        image=image.resize(resize)

    if isinstance(rotate_angle, (int, float)):
        rotate_angle %=360
        if rotate_angle !=0:
            try:
                image = image.rotate(rotate_angle, expand=True)
            except Exception as err:
                print(f"Error for rotating the image: {e}")
    else:
        print("Error: rotate angle must be a number")

    draw = ImageDraw.Draw(image)
    font_size, font_path = 80, "C:/Windows/Fonts/times.ttf"
    font = ImageFont.truetype(font_path, font_size)
    text_position = (image.width/2, image.height/2)
    draw.text(text_position, text, fill="white", font=font)

    image.save(output_path)
    return output_path
