

setMediaFolder("C:\\Project1Images")
Folder = ["1.png","2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]

#You need to define an empty lists to make use of functions starting at line 19
pictures = []
redPixelList = []
greenPixelList = []
bluePixelList = []

for pict in Folder:
  image = makePicture(pict)
  pictures.append(image) #this will add the pictures to a list

  
#makes a blank for the output image 
PictWidth = getWidth(image)
PictHeight = getHeight(image)
OutputImage = makeEmptyPicture(PictWidth, PictHeight)
show(OutputImage)
  
  
  
redPixelAverage = 0
greenPixelAverage = 0
bluePixelAverage = 0
  
for x in range(0, PictWidth):
  for y in range(0, PictHeight):
    for imageNumber in range(0,9):
    
      pixel = getPixel(pictures[imageNumber], x, y)
      
      red = getRed(pixel)
      green = getGreen(pixel)
      blue = getBlue(pixel)
      
      redPixelList.append(red)
      greenPixelList.append(green)
      bluePixelList.append(blue)
      
      
      
      #redPixelAverage += redPixelList[imageNumber]
      #43601 sum of red pixels 
      
      
#The median function below is something that I found via GitHub
#at https://gist.github.com/ProProgrammer/6703163
def len_even(y):
  if len(y) % 2 == 0:
    return True
  else:
    return False


def median(x):
  y = sorted(x)
  if not len_even(y):
    return y[(len(y) / 2)]
  else:
    mid_position1 = y[(len(y) / 2) - 1]
    mid_position2 = y[(len(y) / 2)]
    return (mid_position1 + mid_position2) / 2.0



RedMedian = median(redPixelList)
redPixelList = []
redPixelList.append(RedMedian)


GreenMedian  = median(greenPixelList)
greenPixelList = []
greenPixelList.append(GreenMedian)


BlueMedian = median(bluePixelList)
bluePixelList = []
bluePixelList.append(BlueMedian)

      
    
      
    #stating the red/green/bluePixelList lists empty clears them of the values that were appended previously 
    #redPixelList = [] 
    #greenPixelList = []
    #bluePixelList = []
    

    

