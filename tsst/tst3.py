import cv2

# 讀取原始圖片
image = cv2.imread(r'C:/Users/User/Desktop/abc.jpg')  # 換成你的圖
(h, w) = image.shape[:2]
new_size = (int(w * 1.5), int(h * 1.5))  # 放大 1.5 倍

# 不同插值法
methods = {
    "INTER_NEAREST": cv2.INTER_NEAREST,
    "INTER_LINEAR": cv2.INTER_LINEAR,
    "INTER_AREA": cv2.INTER_AREA,
    "INTER_CUBIC": cv2.INTER_CUBIC,
    "INTER_LANCZOS4": cv2.INTER_LANCZOS4
}

# 執行縮放並顯示結果
for name, method in methods.items():
    resized = cv2.resize(image, new_size, interpolation=method)
    cv2.imshow(name, resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
