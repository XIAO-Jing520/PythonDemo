from PIL import Image
import pickle
from sys import exit
import os


def past_0_all(box):
    all_img = Image.open("all.jpg")
    im = Image.open("0.jpg")
    im_ss = im.resize((400, 400))
    im_ss.save("0.jpg")
    im.close()
    im_ss.close()
    im = Image.open("0.jpg")
    # print(im.size)
    # box = (0, 0, 400, 400)
    region = all_img.crop(box)
    print(box)
    # print(region.size)
    region = im
    all_img.paste(region, box)

    all_img.save("all.jpg")


max_x = 4000
max_y = 4000
derta = 400

if os.path.exists('box.pickle'):

    with open('box.pickle', 'rb') as f:
        box = pickle.load(f)
else:
    box = [0, 0, 400, 400]

print(box)
if box[3] == max_y:

    box[3] = 400
    box[1] = 0
    box[0] += derta
    box[2] += derta
    if box[0] == max_x:
        print('超过最大值')
        exit()
else:
    box[1] += derta
    box[3] += derta

past_0_all(tuple(box))


with open('box.pickle', 'wb') as f:

    pickle.dump(box, f)


    '''
faceset中的face token为： 61a2e1b2bb3d8c75e60859dfd43ef599

------------------------------------------------------------search------------------------------------------------------------
  {'faces': [{'face_rectangle': {'height': 332,
                                 'left': 197,
                                 'top': 215,
                                 'width': 332},
              'face_token': '72696a8de9e859963c04f965f3357389'}],
   'image_id': 'wuucei/DHpGkxVIzfyyeFw==',
   'request_id': '1550974144,77e5c362-29b1-4c8e-96f2-1749d83c1614',
   'results': [{'confidence': 16.978,
                'face_token': '61a2e1b2bb3d8c75e60859dfd43ef599',
                'user_id': ''}],
   'thresholds': {'1e-3': 62.327, '1e-4': 69.101, '1e-5': 73.975},
   'time_used': 958}
    '''
