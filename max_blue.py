# Import necessary image processing library
#	Documentation: https://pillow.readthedocs.io/en/stable/index.html
from PIL import Image

# WRITE TOGETHER
def max_blue(image):
	"""Sets the blue component of the RGB color of every pixel in the picture to the maximum value. An example of manipulating one component of the color of a pixel."""
	# load the pixel data into an accessible format
	pixels = image.load() 
	width = image.width # get image width in pixels
	#print(width) # 900px
	height = image.height # get image height in pixels
	#print(height) # 600px
	
	# iterate through (access) each pixel in the image
	for x in range(width): 
		for y in range(height):
			# a pixel is represented by a tuple of RGB values 
			#	e.g. (0,255,0) is a fully green pixel
			# access each pixel's color tuple
			color_tuple = pixels[x, y] 
			# unpack each color_tuple into its RGB values
			r, g, b = color_tuple
			
			if x == 0 and y == 0:
				print(r,g,b) # see top-left pixel at 0,0
				
			# Modifies the pixel at the given x,y position, replacing it with a new rgb color tuple
			image.putpixel((x, y), (r, g, 255)) 

	# save the new image to the file tree as a PNG file
	image.save("max_blue.png", "png")

# WRITE ON YOUR OWN - NO COPY/PASTE!
def max_red(image):
	"""Sets the red component of the RGB color of every pixel in the picture to the maximum value."""
	pixels = image.load()
	width = image.width 
	height = image.height
	for x in range(width): 
		for y in range(height):
			r, g, b = pixels[x, y]
			image.putpixel((x, y), (255, g, b))
	image.save("max_red.png", "png") 

def max_green(image):
	"""Sets the green component of the RGB color of every pixel in the picture to the maximum value."""
	pixels = image.load()
	width = image.width 
	height = image.height
	for x in range(width): 
		for y in range(height):
			r, g, b = pixels[x, y]
			image.putpixel((x, y), (r, 255, b))
	image.save("max_green.png", "png")  

# MAIN CODE

# open source image and convert to RGB format (if it wasn't already)
orig_image = Image.open("huskie.jpg").convert('RGB')

# call a function and pass to it the original image (only call one function at a time)
max_blue(orig_image)
#max_red(orig_image)
#max_green(orig_image)
