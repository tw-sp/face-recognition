import datetime
import os
import cv2


def takes_photos_in_web_cam(image_name_prefix):
    image_height = 300
    image_width = 300
    win_name = "Frame"

    capture = cv2.VideoCapture()
    capture.open(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, image_height)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, image_width)
    cv2.namedWindow(win_name)

    images_filenames = []
    image_id = 0
    photo_session_id = generate_unique_id()

    file_name_base = image_name_prefix + photo_session_id
    ext = '.jpg'
    dir_path = os.path.dirname(os.path.realpath(__file__))

    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
            cv2.imshow(win_name, frame)

        key = cv2.waitKey(33)
        if key == 27:  # ESC
            break
        elif key == 13:  # Enter
            image_id += 1
            file_name = os.path.join(dir_path, 'photos', file_name_base + '-' + '{0:02d}'.format(image_id) + ext)
            images_filenames.append(file_name)
            cv2.imwrite(file_name, frame)
            print "Photo %d - %s" % (image_id, file_name)
    return images_filenames


def generate_unique_id():
    prefix = datetime.datetime.now().strftime("%Y-%m-%d-")
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time(0))
    suffix = '{0:05d}'.format((now - midnight).seconds)
    return prefix + suffix


if __name__ == "__main__":
    takes_photos_in_web_cam('TestPrefix-')
