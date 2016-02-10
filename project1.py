#IT FINALLY WORKS!!!!

setMediaFolder("C:\\Project1Images")
Folder = ["1.png","2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]

def pixelMedian(pixelList):
  listLength = len(pixelList)
  sortedValues = sorted(pixelList)
  middleIndex = ((listLength + 1)/2)-1
  return sortedValues[middleIndex]
  
#def makeNewColor(newRed, newGreen, newBlue, x, y, OutputImage):
   #newColor = makeColor(newRed, newGreen, newBlue)
   #ImagePixel = getPixel(OutputImage, x, y) 
   #setRed(ImagePixel, newRed)
   #setGreen(ImagePixel, newGreen)
   #setBlue(ImagePixel, newBlue)
   #setColor(ImagePixel, newColor)
   #print newColor
   #print ImagePixel
   #return newColor


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
          

    RedMedian = pixelMedian(redPixelList)
    redPixelList = []
    #redPixelList.append(RedMedian)
    #print redPixelList

    GreenMedian  = pixelMedian(greenPixelList)
    greenPixelList = []
    #greenPixelList.append(GreenMedian)
    #print greenPixelList

    BlueMedian = pixelMedian(bluePixelList)
    bluePixelList = []
    #bluePixelList.append(BlueMedian)
    #print bluePixelList
      
    #makeNewColor(RedMedian, GreenMedian, BlueMedian, x, y, OutputImage)
    ImagePixel = getPixel(OutputImage, x, y) 
    setRed(ImagePixel, GreenMedian)
    setGreen(ImagePixel, GreenMedian)
    setBlue(ImagePixel, BlueMedian)


show(OutputImage)

      
    #stating the red/green/bluePixelList lists empty clears them of the values that were appended previously 
    #redPixelList = [] 
    #greenPixelList = []
    #bluePixelList = []
    

    

