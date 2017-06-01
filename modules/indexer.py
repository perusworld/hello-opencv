import glob
import os
import cv2
import cPickle

from modules.rgbhistogram import RGBHistogram


class IMGIndexer:
    def __init__(self, src, dest, idx, ext):
        self.src = src
        self.dest = dest
        self.idx = idx
        self.ext = ext

    def begin(self):
        index = {}
        desc = RGBHistogram([8, 8, 8])

        for imgPath in glob.glob("%s/%s" % (self.src, self.ext)):
            imgId = os.path.basename(imgPath)
            print "Processing %s" % imgId

            img = cv2.imread(imgPath)
            features = desc.describe(img)
            index[imgId] = features

        idxFile = open("%s/%s" % (self.dest, self.idx), "w")
        idxFile.write(cPickle.dumps(index))
        idxFile.close()

        print "Indexed %d files" % len(index)
