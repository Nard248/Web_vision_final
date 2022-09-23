# from Web_vision_final.settings import MEDIA_ROOT
# import easyocr
# import cv2
# import numpy as np
# import os
# reader = easyocr.Reader(['en'])
#
#
# def search_for_text(word, path, name):
#     img = cv2.imread(path)
#     width = img.shape[1]
#     height = img.shape[0]
#     img = cv2.resize(img, dsize=(1300, int((1300/width) * height)))
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     result = reader.readtext(img)
#     for detection in result:
#         text = detection[1]
#         if word in text:
#             top_left = tuple(detection[0][0])
#             bottom_right = tuple(detection[0][2])
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             img = cv2.rectangle(img, tuple([top_left[0]-30, top_left[1]-30]), tuple([bottom_right[0]+30, bottom_right[1]+30]), (0, 255, 0), 3)
#             img = cv2.putText(img, text, tuple([top_left[0]-35, top_left[1]-35]), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
#             os.chdir(MEDIA_ROOT + '/Processed')
#             name = name + '.jpeg'
#             cv2.imwrite(f'{name}', img)
#             return f'media/Processed/{name}'
#         # else:
#         #     img = cv2.imread(path)
#         #     os.chdir(MEDIA_ROOT + '/Processed')
#         #     name = name + '.jpeg'
#         #     cv2.imwrite(f'{name}', img)
#         #     return f'media/Processed/{name}'
#
#
# # print(search_for_text('WAITING', f'{MEDIA_ROOT}/Uploads/sign_small.jpg', 'testettst'))