# Try to import dependencies
try:
    from PIL import Image
    import tqdm

except ModuleNotFoundError:
    print("Sorry, something went wrong while importing dependencies.\nPlease make sure that all dependencies are propperly installed.")


class ImageToAscii:
    def __init__(self, image, scale, output_file_path, print_to_console="false"):
        self.scale = scale
        self.output_file_path = output_file_path
        self.print_to_console = print_to_console

        self.image = image

        try:

            # Opens the image and converts it to grayscale
            self.image = Image.open(image).convert("L")

            # Divides the resize factor by the current width and height to resize the image
            self.image.thumbnail(
                (self.image.width//self.scale, self.image.height//self.scale))

            # Gets all the pixels from the image. Since the image was converted to grayscale,
            # all pixels are an integer from 0 --> 255
            self.pixels = self.image.load()

            # List of ascii characters to represent the brightness, (darkest to lightest pixel)
            self.ascii_chars = ['@', '#', '%', '$',
                                '£', '*', '+', ':', ';', ',', '.']

            self.main()

        except Exception as oopsie:
            print(
                f"\nSorry, something went wrong while handling the file '{self.image}'.\nError: {oopsie.args[1]}")

    def main(self):
        self.loop_trough_pixels()

    def loop_trough_pixels(self):
        # Keeps track of the current pixel location
        img_size = 0

        # The output to be written to the file
        result = ""
        for y in tqdm.tqdm(range(self.image.height)):
            for x in range(self.image.width):
                img_size += 1

                # Maps the pixel brightness from 0 --> 255, to 0 --> 10
                pixel = self.pixels[x, y] // 25

                result += self.ascii_chars[pixel]

                # If the current pixel position is greater than
                # the image width
                if img_size >= self.image.width:
                    result += "\n"
                    img_size = 0

        self.write_to_file(result)
        if self.print_to_console:
            if self.print_to_console.lower() == "true":
                print()
                print(result)

    def write_to_file(self, content):
        with open(self.output_file_path, "a") as file:
            file.write(content)
