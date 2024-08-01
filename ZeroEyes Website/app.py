from flask import Flask,render_template,Response, request, send_file
import cv2
from YOLO_Video import video_detection
from ultralytics import YOLO
import math

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def streaming():
    return render_template('streaming.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


#-----------------------------------------------------------------------------------
@app.route('/fire')
def fire():
    return render_template('fire.html')
ALLOWED_EXTENSIONS = ['mp4']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def detect_fire(video_path):
    # Load YOLOv8 model
    model = YOLO("best (3).pt")
    classNames = ["fire"]

    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter('static/videos/output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, (frame_width, frame_height))

    while True:
        success, img = cap.read()

        if not success:
            break

        # Doing detections using YOLOv8 frame by frame
        results = model(img, stream=True)

        # Once we have the results we can check for individual bounding boxes and see how well it performs
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

        out.write(img)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

@app.route('/upload', methods=['GET','POST'])
def upload():
    if 'video' not in request.files:
        return 'No video file found'

    video = request.files['video']

    if video.filename == '':
        return 'No video file selected'

    if video and allowed_file(video.filename):
        video.save('static/videos/' + video.filename)
        
        # Perform fire detection
        detect_fire('static/videos/' + video.filename)
        print(video.filename)
        
        return render_template('fire.html', video_name= video.filename)

    return 'Invalid file type'

@app.route('/download')
def download():
    detected_video_path = 'static/videos/output.mp4'
    return send_file(detected_video_path, as_attachment=True)
#--------------------------------------------------------------------------------------------------

@app.route('/gun')
def gun():
    return render_template('gun.html')

def detect_gun(video_path):
    # Load YOLOv8 model
    model = YOLO("best.pt")
    classNames = ["Pistol","Grenade" , "Gun" , "Knife"]

    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter('static/videos/output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, (frame_width, frame_height))

    while True:
        success, img = cap.read()

        if not success:
            break

        # Doing detections using YOLOv8 frame by frame
        results = model(img, stream=True)

        # Once we have the results we can check for individual bounding boxes and see how well it performs
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

        out.write(img)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

@app.route('/upload_gun', methods=['GET','POST'])
def upload_gun():
    if 'video' not in request.files:
        return 'No video file found'

    video = request.files['video']

    if video.filename == '':
        return 'No video file selected'

    if video and allowed_file(video.filename):
        video.save('static/videos/' + video.filename)
        
        # Perform gun detection
        detect_gun('static/videos/' + video.filename)
        print(video.filename)
        
        return render_template('gun.html', video_name= video.filename)

    return 'Invalid file type'

@app.route('/download_gun')
def download_gun():
    detected_video_path = 'static/videos/output.mp4'
    return send_file(detected_video_path, as_attachment=True)


#--------------------------------------------------------------------------------------------------------
@app.route('/recog')
def recog():
    return render_template('recog.html')
@app.route('/violence')
def violence():
    return render_template('violence.html')

if __name__=="__main__":
    app.run(debug=True)
