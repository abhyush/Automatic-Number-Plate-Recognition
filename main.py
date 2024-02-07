import cv2
import imutils
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'pytesseract.pytesseract.tesseract_cmd'
img = cv2.imread('car.jpg')
# Resizing our image
img = imutils.resize(img, width=400)
# Display image with 400 pixels cv2.imshow("original image", img) cv2.waitKey(0)
# Converting to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Display gray image cv2.imshow("greyed image", gray_img) cv2.waitKey(0)
# Reducing the noise
gray_img = cv2.bilateralFilter(gray_img, 12, 18, 18)
cv2.imshow("smoothened image", gray_img)
cv2.waitKey(0)
# Detect the edges
# cv2.canny helps to detect edges
edged = cv2.Canny(gray_img, 40, 300)
cv2.imshow("edged image", edged)
cv2.waitKey(0)
# Recognizing the image's contours from its edges
contours, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1 = img.copy()
cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
cv2.imshow("contours", img1)
cv2.waitKey(0)
# Sorting out the known contours
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
screenCnt = None
img2 = img.copy()
cv2.drawContours(img2, contours, -1, (0, 255, 0), 3)
cv2.imshow("Top 30 contours", img2)
cv2.waitKey(0)
# Locating the four-sided contour
i = 7
for c in contours:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
    if len(approx) == 4:
        screenCnt = approx
# Removing the rectangular portion that is known as the license plate.
    x, y, w, h = cv2.boundingRect(c)
    new_img = img[y:y+h, x:x+w]
    cv2.imwrite('./'+str(i)+'.png', new_img)
    i += 1
    break
# Drawing the chosen contour on the original image
cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("image with detected license plate", img)
cv2.waitKey(0)
# Obtaining text from the license plate's cropped image
Cropped_loc = './7.png'
cv2.imshow("cropped", cv2.imread(Cropped_loc))
plate = pytesseract.image_to_string(Cropped_loc, lang='eng')
print("Number plate is:", plate)
cv2.waitKey(0)
cv2.destroyAllWindows()
