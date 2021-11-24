from skimage import feature
import cv2
import numpy as np
import matplotlib.pyplot as plt

#prewframe = np.zeros((512,512),dtype=np.dtype(np.uint8))
prewframe = cv2.imread('some_100000.png',cv2.IMREAD_GRAYSCALE)

class LocalBinaryPatterns:
    def __init__(self, numPoints, radius):
        # store the number of points and radius
        self.numPoints = numPoints
        self.radius = radius

    def describe(self, image, eps=1e-7):
        # compute the Local Binary Pattern representation
        # of the image, and then use the LBP representation
        # to build the histogram of patterns
        lbp = feature.local_binary_pattern(image, self.numPoints,
            self.radius, method="uniform")
        (hist, _) = np.histogram(lbp.ravel(),
            bins=np.arange(0, self.numPoints + 3),
            range=(0, self.numPoints + 2))

        # normalize the histogram
        hist = hist.astype("float")
        hist /= (hist.sum() + eps)

        # return the histogram of Local Binary Patterns
        return hist

desc = LocalBinaryPatterns(24, 8)
image = cv2.imread("diff\\some_7272.png",cv2.IMREAD_GRAYSCALE)
hist = desc.describe(image)

plt.plot(hist,'b-')
plt.ylabel('Feature Vectors')
plt.show()


for i in range(1, 10360):
    frame = cv2.imread('some_'+str(100000+i)+'.png',cv2.IMREAD_GRAYSCALE)

    diff = cv2.subtract(frame,prewframe)
    
    cv2.imshow('Frame',diff)
    
    prewframe = frame.copy()

    cv2.waitKey(25)

    cv2.imwrite('diff\\some_'+str(i)+'.png',diff)

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
