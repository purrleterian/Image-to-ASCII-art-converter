# Try to import dependencies
try:
    # For image manipulation
    from PIL import Image

    # For the progress bar
    from tqdm import tqdm

except ModuleNotFoundError:
    # If any of the dependencies are not found
    print("Sorry, something went wrong while importing dependencies.\nPlease make sure that all dependencies are propperly installed.")

    #TODO: add a 'requirements.txt' file, or just add the dependencies to the README.md

class ImageToAscii:
    def __init__(self, image, scale, output_file_path, print_to_console="false", reverse="false"):
        # Command line arguments

        self.scale = scale
        self.output_file_path = output_file_path
        self.print_to_console = print_to_console
        self.reverse = reverse

        self.image = image

        # ----------------------- #

        try:

            # Opens the image and converts it to grayscale
            self.image = Image.open(image).convert("L")

            # Divides the resize factor by the current width and height to resize the image
            self.image.thumbnail((self.image.width//self.scale, self.image.height//self.scale))

            # Gets all the pixels from the image. Since the image was converted to grayscale,
            # all pixels are an integer from 0 --> 255
            self.pixels = self.image.load()

            # List of ascii characters to represent the brightness, (darkest to lightest pixel)
            self.ascii_chars = ['@', '#', '%', '$', '£', '*', '+', ';', ':', ',', '.']

            if self.reverse == "true":
                # reversed() returns an iterator, thus it has to be converted
                # into a list
                self.ascii_chars = list(reversed(self.ascii_chars))

            self.main()

        except Exception as oopsie:
            print(
                f"\nSorry, something went wrong while handling the file '{self.image}'.\nError: {oopsie.args[1]}")

    def main(self):
        self.clear_file()
        self.loop_through_pixels()
        print(f"Done, the output contains: {len(self.result)} characters.")

    def loop_through_pixels(self):
        # Keeps track of the current pixel location
        pixel_position = 0

        # The output to be written to the file
        self.result = ""
        for y in tqdm(range(self.image.height)):
            for x in range(self.image.width):
                pixel_position += 1

                # Maps the pixel brightness from 0 --> 255, to 0 --> 10
                pixel = self.pixels[x, y] // 25

                self.result += self.ascii_chars[pixel]

                # If the current pixel position is greater than
                # the image width...
                if pixel_position >= self.image.width:
                    self.result += "\n" # ... Go to the next line ...
                    pixel_position = 0 #  ... And resets the current pixel position

        self.write_to_file(self.result)
        if self.print_to_console:
            if self.print_to_console.lower() == "true":
                print("\n" + self.result)

    def write_to_file(self, content):
        # "a" means append mode. In that mode, it adds contents to the file
        # if the file already exists, and if it doesn't exists, it creates the file
        with open(self.output_file_path, "a") as file:
            file.write(content)


    def clear_file(self):
        # "W" means write mode. In that mode, it replaces all the contents of the file
        with open(self.output_file_path, "w") as file:
            file.write("")
