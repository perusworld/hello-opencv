import cv2


class RGBHistogram:

    def __init__(self, bins):
        self.bins = bins

    def describe(self, img):
        hist = cv2.calcHist([img], [0, 1, 2], None, self.bins, [0, 256, 0,256, 0,256])
        cv2.normalize(hist, hist)
        return hist.flatten()
