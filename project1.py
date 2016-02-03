#Trying to working out an alternative way to getting the images

#Using setMediaPath has worked so far, but is there a way 
#to make it a little more condensed but still able 
#able to access images 1 through 9?

setMediaPath("C:\\Project1Images") 
pict1 = makePicture("1.png")
pict2 = makePicture("2.png")
pict3 = makePicture("3.png")
pict4 = makePicture("4.png")
pict5 = makePicture("5.png")
pict6 = makePicture("6.png")
pict7 = makePicture("7.png")
pict8 = makePicture("8.png")
pict9 = makePicture("9.png")

#make empty picture with width and height of the project picts
width = getWidth(pict1)
height = getHeight(pict1)
emptyPicts = makeEmptyPicture(width, height)
#explore(pict1)


#Since we're supposed to find a way to remove the annoying tourist from the image 
#I imagine figuring out how to remove him would be the first step

#what are some of the ways we can go about selecting/isolating the pixels he's comprised of?

#Given their variance, is there a way we can isolate the pixels within a specific RGB range?