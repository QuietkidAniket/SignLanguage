# from PIL import Image
import numpy as np
import cv2 
import time


def showsign(x,name):
    cv2.imshow(name,x.reshape(400,400))
    cv2.waitKey(1)
    cv2.destroyAllWindows()

def read_set():
    image_set = np.load("dataset/image_set.npy", allow_pickle=True)
    for image in image_set:
        image[1] = image[1].reshape(400,400)
    image_map = dict(zip(image_set[:,0].tolist(), image_set[:,1].tolist() ) )
    return image_map


image_map = read_set()


text = input("Please enter the text below : ").lower()

print(" ---------------------- Showing the American Sign Language Hand signs ! -------------------\n\n")


for c in list(text):
    if c == " ":
       time.sleep(1)
       continue
    try:
        showsign(image_map[c], c)
    except:
        continue
    time.sleep(1)

print("-------------------------Done Showing all the hand signs ! -----------------")

