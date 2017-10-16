__author__ = 'regepanda'
import cv2.cv as cv
import numpy as np
import cv2
import time

# img = cv2.imread("1.jpg")
# emptyImage = np.zeros(img.shape, np.uint8)
#
# emptyImage2 = img.copy()
#
# emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("EmptyImage3", emptyImage3)
# cv2.waitKey (0)
# cv2.destroyAllWindows()





# capture = cv.CaptureFromFile('2.avi')
# print(capture)
# nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))
#
# fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)
#
# wait = int(1 / fps * 1000 / 1)
#
# duration = (nbFrames * fps) / 1000
#
# print 'Num. Frames = ', nbFrames
# print 'Frame Rate = ', fps, 'fps'
# print 'Duration = ', duration, 'sec'
#
# for f in xrange(nbFrames):
#     frameImg = cv.QueryFrame(capture)
#     print cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_POS_FRAMES)
#     cv.ShowImage("The Video", frameImg)
#     cv.WaitKey(wait)





# cap = cv2.VideoCapture('2.avi')
# print cap.isOpened()
# if cap.isOpened():
#     print "cap is opened"
#     while (True):
#         re, img = cap.read()
#         cv2.imshow("video output", img)
#         k = cv2.waitKey(10) & 0xFF
#         if k == 27:
#             break
# cap.release()
# cv2.destroyAllWindows()






videoCapture = cv2.VideoCapture('2.avi')
print(videoCapture)
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
print(fps)
size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
print(size)

videoWriter = cv2.VideoWriter('oto_other.mp4', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)

success, frame = videoCapture.read()
print(success)
print(frame)
while success:
    cv2.imshow("Oto Video", frame)
    cv2.waitKey(1000 / int(fps))
    videoWriter.write(frame)
    success, frame = videoCapture.read()
