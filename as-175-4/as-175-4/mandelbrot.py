from cImage import *
import random

###########################################################################
# Given a pixel, calculate and return its intensity (ie, Red + Green + Blue).
###########################################################################
def instensity(pixel):
    return int(pixel.getRed() + pixel.getGreen() + pixel.getBlue())

###########################################################################
# Given an integer n, generate a list of n RGB colors, 
# sorted by intensity.  Return a list of Pixels named 'color_list'
###########################################################################
def generate_random_color_table(n):
    random.seed(69)
    #Make 149 random colours
    for i in range(n):
        color_list.append(Pixel(random.randint(0,255), 
                                random.randint(0,255), 
                                random.randint(0,255)))
    #Add colour black at escape value in list
    color_list.append(Pixel(0, 0, 0))
    #Sort the list ascending based on intensity
    color_list.sort(key = instensity, reverse = True)
    return color_list

###########################################################################
# Check if the point (x,y) is close to the image's border.
###########################################################################
def is_close_to_border(x, y):
    bounds = 10
    #Check if the click was to close to the edge of the window
    if x - bounds <= 0 or y - bounds <= 0 or x + bounds >= window_size or y + bounds >= window_size:
        return True
    return False 

###########################################################################
# The Mandelbrot function returns the escape value for a complex number c.
# If the algorithm does not escape within N iterations, return N.
# Do not modify this function.
###########################################################################
def escape_value(c, N):
    z = 0
    for n in range(N):
        if abs(z) > 2:
            return n
        z = z*z + c
    return N

###########################################################################
#Input:
#    img: the image to be modified
#    lower_x: the lower x bound of the Mandelbrot range
#    upper_x: the upper x bound of the Mandelbrot range
#    lower_y: the lower y bound of the Mandelbrot range
#    upper_y: the upper y bound of the Mandelbrot range
#    
#    Determine the color of each pixel in the image, according to the 
#    Mandelbrot set. You will need to scale x and y values into the 
#    Mandelbrot range, and supply a complex number c
#    to escape_value(c, N), whose return value 
#    will indicate which color should be chosen.
###########################################################################
def draw_at(img, lower_x, upper_x, lower_y, upper_y):
    #Initilize the image window
    myImageWindow = ImageWin("Mandelbrot Set", window_size, window_size)
    count = 0
    #Zoom in 3 times on the initial image
    while count < 4:
        #Go through all pixels in the image
        for col in range(window_size):
            for row in range(window_size):
                #calculate the complex variables based on scaled values 
                c = complex(
                    (scale(col, upper_x, lower_x)),
                    (scale(row, upper_y, lower_y)))
                #Set the pixel at the current location based on escape value calculated
                img.setPixel(col, row, color_list[escape_value(c, N)])
        #Draw the image
        img.draw(myImageWindow)
        #Get the click from user to zoom in on specific location
        mouseClick = myImageWindow.getMouse()
        #Check if click out of range
        if is_close_to_border(mouseClick[0], mouseClick[1]):
            myImageWindow._close()
            break
        #Scale the location of the click values
        click = ((scale(mouseClick[0], upper_x, lower_x)),
                (scale(mouseClick[1], upper_y, lower_y)))
        #Change the interval length
        half = (upper_x - lower_x) / 4.0
        #Set new bounds for the set
        lower_x = click[0]-half
        upper_x = click[0]+half
        lower_y = click[1]-half
        upper_y = click[1]+half
        #Increment the interval for the exit count
        count += 1
    myImageWindow._close()

###########################################################################
#Scale Function
#   Scales the values of the upper and lower ranges with relation to image
###########################################################################
def scale(coord, upper, lower):
    return ((upper - lower)/float(window_size) * (coord)) + lower

###########################################################################
# Main function
# You will need to create an initial Mandelbrot image with the initial range
# Specified here.  Your program should also allow the user to zoom up to
# three times: each zoom scales the image by a factor of 2, and will centre
# the new image on the location clicked in the previous step.  After 3 zooms,
# a click will close the image.  If the user clicks too close to the edge 
# of the image, the image will close.
###########################################################################
def main():
    global N, window_size, color_list
    # settings
    window_size = 200
    N = 150
    color_list = []
    
    # initial mandelbrot set range
    lower_x = -3
    upper_x = 1
    lower_y = -2
    upper_y = 2
    #Make the list of colours
    generate_random_color_table(N)
    #Initilize an empty image
    newImage = EmptyImage(window_size, window_size)
    #Call the draw function
    draw_at(newImage, lower_x, upper_x, lower_y, upper_y)

if __name__ == '__main__':
    main()

