import cv2

# 讀取影像（請將檔名換成你自己的路徑）
image = cv2.imread('C:/Users/User/Desktop/abc.jpg')

# 顯示影像
cv2.imshow('abc', image)

# 等待任意鍵盤輸入後關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
