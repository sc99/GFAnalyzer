from ImageAnalyzer import ImageAnalyzer


imgAnalyzer = ImageAnalyzer('sample.png')
for c in imgAnalyzer.contourize():
    imgAnalyzer.analyzefigure(c)
