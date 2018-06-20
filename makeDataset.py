import cv2

for i in range(1, 69):
    # open("./image/({}).jpg".format(i))
    img = cv2.imread("./image/({}).jpg".format(i))

    dataSet1 = img[720:740, 1510:1520]
    dataSet2 = img[720:740, 1520:1530]

    # cv2.imshow("image", img)
    cv2.imshow("data1", dataSet1)
    cv2.imshow("data2", dataSet2)

    cv2.imwrite("./dataset/{}-1.jpg".format(i), dataSet1)
    cv2.imwrite("./dataset/{}-2.jpg".format(i), dataSet2)
    cv2.waitKey()
