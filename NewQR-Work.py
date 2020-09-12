import cv2
import pyzbar.pyzbar as pyzbar
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
font = cv2.FONT_HERSHEY_PLAIN
ret, frame = cap.read()


def Imageinfo():
    global Qr_info, ret
    while ret:
        ret, frame = cap.read()
        if ret:
            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                Qr_info = obj.data.decode('utf-8')
                cap.release()
                cv2.destroyAllWindows()
            else:
                cv2.putText(frame, "Ready to scan", (50, 50), font, 2, (255, 0, 0), 3)
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27 or key == ord('q'):
                break
    cv2.destroyAllWindows()
    return Qr_info


QR = Imageinfo()

if QR == 'place':
    print("scanning for the available table")
    time.sleep(4)
    print("Your table number 6 is allotted for your dine\nEnjoy your Meal\n\nScan for your Menu ;) ")
    time.sleep(5)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frame = cap.read()
    QR = Imageinfo()

if QR == 'Hello':
    print("\n")
    print("Greetings \nPlease look at our delicious recipes ")
    with open('Menu') as f:
        data = f.read().splitlines()
        print(data)
    order = input(str("Enter your order with recipe id\n->:"))
    SplitORD = order.split()
    SplitORD = list(SplitORD)
    print("preparing ORD", SplitORD)
    length = len(SplitORD)
    print("You have ordered", length, "Orders\n")
    bill = 0

    print("Your order is:")
    for i in range(0, length):
        for rec in data:
            if rec[:2] == SplitORD[i]:
                amount = int(rec[-3:])
                bill = bill + amount
                print(rec)
    #        else:
    #            print("not working \n")

    print("your recipe is being cooked")
    print("Your amount is", bill, "Rs including tax")
    print("Thank you for ordering")
else:
    print("Unauthorised User")
