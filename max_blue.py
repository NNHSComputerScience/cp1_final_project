# Import necessary image processing library
#	Documentation: https://pillow.readthedocs.io/en/stable/index.html
from PIL import Image

# WRITE TOGETHER
def max_blue(image):
	"""Sets the blue component of the RGB color of every pixel in the picture to the maximum value. An example of manipulating one component of the color of a pixel."""
	pixels = image.load() # loads the pixel data into an accessible format
	width = image.width # get image width in pixels
	#print(width) # 900px
	height = image.height
	#print(height) # 600px
	
	# iterate through each pixel in the image
	for x in range(width): 
		for y in range(height):
			# a pixel is represented by a tuple of RGB values (e.g. (0,255,255))
			r, g, b = pixels[x, y] # access each pixel and unpack its RGB values
			if x == 0 and y == 0:
				print(pixels[x, y]) # see top-left pixel at 0,0
			image.putpixel((x, y), (r, g, 255)) # Modifies the pixel at the given x,y position.

	# save the new image
	image.save("max_blue.png", "png")

# WRITE ON YOUR OWN - NO COPY/PASTE!
def max_red(image):
	"""Sets the red component of the RGB color of every pixel in the picture to the maximum value."""
	pass

def max_green(image):
	"""Sets the green component of the RGB color of every pixel in the picture to the maximum value."""
	pass

# MAIN CODE

# open source image and convert to RGB format (if it wasn't already)
orig_image = Image.open("huskie.jpg").convert('RGB')

# call a function and pass to it the original image (only call one function at a time)
max_blue(orig_image)
#max_red(orig_image)
#max_green(orig_image)
