import argparse
import glob
import os
import cv2
import cPickle

from modules.indexer import IMGIndexer

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--src", help="Src Img Dir", default="images")
ap.add_argument("-d", "--dest", help="Dest Idx Dir", default="index")
ap.add_argument("-i", "--idx", help="Idx File Name", default="opt.idx")
ap.add_argument("-e", "--ext", help="Img Extensions", default="*.*")
args = vars(ap.parse_args())

indexer = IMGIndexer(args["src"], args["dest"], args["idx"], args["ext"])
indexer.begin()
