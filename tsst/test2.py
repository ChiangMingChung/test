import cv2
import numpy as np

# 讀取圖片
image = cv2.imread(r'C:/Users/User/Desktop/abc.jpg')  # 換成你的圖片路徑

# 取得影像尺寸
(h, w) = image.shape[:2]
center = (w // 2, h // 2)  # 以影像中心為旋轉中心

# 建立旋轉矩陣 (正值逆時針，負值順時針)
M1 = cv2.getRotationMatrix2D(center, 15, 1.0)
M2 = cv2.getRotationMatrix2D(center, -30, 1.0)

# 執行仿射轉換 (旋轉)
rotated_15 = cv2.warpAffine(image, M1, (w, h))
rotated_neg30 = cv2.warpAffine(image, M2, (w, h))

# 顯示結果
cv2.imshow('Rotated 15 Degrees', rotated_15)
cv2.imshow('Rotated -30 Degrees', rotated_neg30)
cv2.waitKey(0)
cv2.destroyAllWindows()
