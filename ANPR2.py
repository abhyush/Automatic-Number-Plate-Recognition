import cv2
import imutils
import pytesseract

# Set the Tesseract path (remove this line if Tesseract is in your system PATH)
# pytesseract.pytesseract.tesseract_cmd = 'opt/homebrew/bin/tesseract'

img = cv2.imread('car.jpg')
img = imutils.resize(img, width=400)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.bilateralFilter(gray_img, 12, 18, 18)
edged = cv2.Canny(gray_img, 40, 300)

contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
screenCnt = None

for c in contours:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is not None:
    x, y, w, h = cv2.boundingRect(screenCnt)
    new_img = img[y:y+h, x:x+w]
    cv2.imwrite('7.png', new_img)

    Cropped_loc = '7.png'
    cv2.imshow("Cropped", cv2.imread(Cropped_loc))
    plate = pytesseract.image_to_string(Cropped_loc, lang='eng')

    if plate:
        print("Number plate is:", plate)
    else:
        print("No text detected on the license plate.")
else:
    print("License plate not found.")

cv2.waitKey(0)
cv2.destroyAllWindows()
