import numpy as np
import cv2 as cv
import glob
import undistort
# import pickle




################ 寻找角点 #############################

chessboardSize = (11,8)
frameSize = (1280,720)



# termination criteria OpenCV默认参数，不用动
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 20
objp = objp * size_of_chessboard_squares_mm


# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


images = glob.glob('images/*.jpg')

for image in images:

    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 寻找棋盘角点
    ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)

    if ret == True:

        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # 绘制找到的角点
        cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(1000)
    else:
        # 寻找角点失败
        print('Not Found!')


cv.destroyAllWindows()




############## CALIBRATION #######################################################

ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, frameSize, None, None)
# cameraMatrix 相机内参矩阵
# dist 畸变矩阵（四维）
# rvecs rotationVector 旋转向量
# tvecs translationVector 平移向量



print(cameraMatrix)
print(dist)

# 存储信息
# pickle.dump((cameraMatrix, dist), open( "out/calibration.pkl", "wb" ))
# pickle.dump(cameraMatrix, open( "out/cameraMatrix.pkl", "wb" ))
# pickle.dump(dist, open( "out/dist.pkl", "wb" ))


# 测试畸变修正结果
# undistort.undistort(cameraMatrix,dist)






