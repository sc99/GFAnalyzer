import cv2

from Figures import Figures

DEFAULT_FONT_FACE = 1
DEFAULT_FONT_SCALE = 1.5
DEFAULT_COLOR = (0, 255, 0)
DEFAULT_THICKNESS = 2


class ImageAnalyzer:

    def __init__(self, path):
        self.image = cv2.imread(path)
        self.__gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.__canny = cv2.Canny(self.__gray, 10, 150)

    def contourize(self):
        self.__canny = cv2.dilate(self.__canny, None, iterations=1)
        self.__canny = cv2.erode(self.__canny, None, iterations=1)
        cnts, _ = cv2.findContours(self.__canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return cnts

    def analyzefigure(self, figure):
        epsilon = 0.01 * cv2.arcLength(figure, True)
        approx = cv2.approxPolyDP(figure, epsilon, True)
        x, y, w, h = cv2.boundingRect(approx)
        txtPos = (x, y - 5)
        if len(approx) == Figures.TRIANGLE.approx_length:
            cv2.putText(self.image, str(Figures.TRIANGLE), txtPos, DEFAULT_FONT_FACE, DEFAULT_FONT_SCALE, DEFAULT_COLOR,
                        DEFAULT_THICKNESS)

        elif len(approx) == Figures.SQUARE.approx_length:
            aspect_ratio = float(w) / h
            print('Aspect ratio: ', aspect_ratio)
            if aspect_ratio == 1:
                cv2.putText(self.image, str(Figures.SQUARE), txtPos, DEFAULT_FONT_FACE, DEFAULT_FONT_SCALE,
                            DEFAULT_COLOR, DEFAULT_THICKNESS)
            else:
                cv2.putText(self.image, str(Figures.RECTANGLE), txtPos, DEFAULT_FONT_FACE, DEFAULT_FONT_SCALE,
                            DEFAULT_COLOR, DEFAULT_THICKNESS)

        elif len(approx) == Figures.PENTAGON.approx_length:
            cv2.putText(self.image, str(Figures.PENTAGON), txtPos, DEFAULT_FONT_FACE, DEFAULT_FONT_SCALE, DEFAULT_COLOR,
                        DEFAULT_THICKNESS)

        elif len(approx) == Figures.HEXAGON.approx_length:
            cv2.putText(self.image, str(Figures.HEXAGON), txtPos, DEFAULT_FONT_FACE, DEFAULT_FONT_SCALE, DEFAULT_COLOR,
                        DEFAULT_THICKNESS)

        elif len(approx) > Figures.CIRCLE.approx_length:
            cv2.putText(self.image, str(Figures.CIRCLE), txtPos, DEFAULT_FONT_FACE, DEFAULT_FONT_SCALE, DEFAULT_COLOR,
                        DEFAULT_THICKNESS)
        else:
            cv2.putText(self.image, 'Unknown', txtPos, DEFAULT_FONT_FACE, DEFAULT_FONT_SCALE, DEFAULT_COLOR,
                        DEFAULT_THICKNESS)

        cv2.drawContours(self.image, [approx], 0, (0, 255, 0), 2)
        cv2.imshow('Analyzed Image', self.image)
        cv2.waitKey(0)
