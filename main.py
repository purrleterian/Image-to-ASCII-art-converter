from PIL import Image
from ImageToAscii import ImageToAscii
import argparse


def main():
    descString = "Converts an image into a series of ascii characters"

    parser = argparse.ArgumentParser(description=descString)

    parser.add_argument("--file", dest="imgPath",
                        required=True, help="The path to the image to be converted")
    parser.add_argument("--scale", dest="scale", required=True,
                        help="The scale of the image to resize it by")
    parser.add_argument("--output", dest="outputFile",
                        required=False, help="The name/path of the output file + .txt")
    parser.add_argument("--print", dest="printToConsole", required=False,
                        help="Decides if it should print the output to the console or not. False by default")

    args = parser.parse_args()

    ita = ImageToAscii(args.imgPath, int(args.scale),
                       args.outputFile, args.printToConsole)


if __name__ == "__main__":
    main()
