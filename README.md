## What is **2ASCIIpy**?

**2ASCIIpy** is a python script made by _yours truly_ that converts an image of any type (.png, .jpg, .gif, etc) to an ASCII representation of that image. It works with both grayscale, and colored images (Although, the output will allways be black and white. Duh.).

## How to use **2ASCIIpy**

To use **2ASCIIpy**, you will need to use command line arguments, as follow:

python main.py --file <PATH TO THE IMAGE> --scale <SCALE TO WHICH RESIZE THE IMAGE BY> --output <NAME/PATH TO THE OUTPUT FILE>

## Yeah, but how does it work?

- the script first creates a list of characters to represent the brightness of the pixel, going from darkest to brightest ( ['@', '#', '%', '$', '£', '*', '+', ':', ';', ',', '.'] ).

- Converts the image to grayscale, so all pixels turn into a number from 0 to 255.

- Then loops trough all pixels of the image, divides the pixel number by 25, thus converting the value from 0 to 255 to (approximately) 0 to 10.

- Them it uses that number to index the characters list, and picks a character for the output.

## Support

You can support this project by reporting bugs 🐞, suggesting fixes 🔧, and ways to optimize the code 💻. Feel free to use the code in your projects, as long as propper credit is given.

And of course, if you liked this project, please consider giving it a star ⭐.
