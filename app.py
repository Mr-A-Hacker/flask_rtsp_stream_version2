from flask import Flask, Response, render_template
import cv2
import os
import time
import threading
from datetime import datetime, timedelta

app = Flask(__name__)
RTSP_URL = "rtsp://192.168.2.224:554/stream1"

def get_camera():
    return cv2.VideoCapture(RTSP_URL)

def generate_frames():
    cam = get_camera()
    while True:
        success, frame = cam.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cam.release()

def record_video_loop():
    while True:
        cam = get_camera()
        width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recordings/stream_{timestamp}.avi"
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))

        start_time = time.time()
        while time.time() - start_time < 1800:  # 30 minutes
            success, frame = cam.read()
            if success:
                out.write(frame)
            else:
                print("⚠️ Frame read failed")
                break
        out.release()
        cam.release()
        time.sleep(1)

def cleanup_old_videos():
    while True:
        now = datetime.now()
        for fname in os.listdir("recordings"):
            fpath = os.path.join("recordings", fname)
            if os.path.isfile(fpath):
                created = datetime.fromtimestamp(os.path.getctime(fpath))
                if now - created > timedelta(hours=4):  # changed from 2 to 4
                    os.remove(fpath)
        time.sleep(300)  # every 5 minutes

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs("recordings", exist_ok=True)
    threading.Thread(target=record_video_loop, daemon=True).start()
    threading.Thread(target=cleanup_old_videos, daemon=True).start()
    app.run(host='0.0.0.0', port=5051, threaded=True)
