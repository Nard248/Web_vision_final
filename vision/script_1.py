def detect_text_my(word, path, name):
    import os
    from google.cloud import vision
    import io
    from PIL import Image, ImageDraw
    from Web_vision_final.settings import MEDIA_ROOT

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Nard\Desktop\Web_vision_final\vision\token.json'

    client = vision.ImageAnnotatorClient()
    img = Image.open(path)
    width, height = img.size
    new_width = 1050
    new_height = height * (new_width / width)
    img.thumbnail((int(new_width), int(new_height)))
    buffer = io.BytesIO()
    img.save(buffer, "JPEG")
    content = buffer.getvalue()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    for text in texts:
        if text.description == word:
            img1 = ImageDraw.Draw(img)
            img1.rectangle([(text.bounding_poly.vertices[0].x - 10,
                             text.bounding_poly.vertices[0].y - 10),
                            (text.bounding_poly.vertices[2].x + 10,
                             text.bounding_poly.vertices[2].y + 10)], outline='red')
    directory = MEDIA_ROOT + '/Processed'
    img.save(directory + '/' + name + '.jpeg')
    return f'media/Processed/{name}.jpeg'
    # os.chdir(MEDIA_ROOT + '/Processed')
    # name = name + '.jpeg'
    # cv2.imwrite(f'{name}', img)
    # return f'media/Processed/{name}'

    # texts = response.text_annotations
    #
    # for text in texts:
    #     vertices = (['({},{})'.format(vertex.x, vertex.y)
    #                  for vertex in text.bounding_poly.vertices])
    #
    # if response.error.message:
    #     raise Exception(
    #         '{}\nFor more info on error messages, check: '
    #         'https://cloud.google.com/apis/design/errors'.format(
    #             response.error.message))

# def detect_text(path):
#     from google.cloud import vision
#     import io
#     client = vision.ImageAnnotatorClient()
#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()
#
#     image = vision.Image(content=content)
#
#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     print('Texts:')
#
#     for text in texts:
#         print('\n"{}"'.format(text))
#
#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                      for vertex in text.bounding_poly.vertices])
#
#         print('bounds: {}'.format(','.join(vertices)))
#
#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))
