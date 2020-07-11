# 导入opencv模块
import cv2

# 捕捉帧，默认摄像头是0 但是我测试之后1才可以正常显示
capture = cv2.VideoCapture(0)
# 循环显示帧
while 1:
    ret, frame = capture.read()
    # 显示窗口第一个参数是窗口名，第二个参数是内容
    cv2.imshow('frame', frame)

    cv2.imwrite('1.jpg', frame)
    if cv2.waitKey(1) == ord('q'):  # 按Q退出
        break


capture.release()  # 释放摄像头
cv2.destroyAllWindows()
