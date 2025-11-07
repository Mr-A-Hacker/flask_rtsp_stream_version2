# flask_rtsp_stream_version2

**Upgraded LAN-only RTSP viewer and recorder** — rebuilt from scratch for forensic logging, cinematic deployment, and Raspberry Pi optimization.

This is the newer version of [`flask_rtsp_stream`](https://github.com/Mr-A-Hacker/flask_rtsp_stream), now with:

- 🎥 **30-minute video recording segments**
- 🧹 **Auto-deletion after 4 hours**
- 🧵 Safe threading with isolated camera instances
- 🖥️ MJPEG stream viewer with fullscreen toggle
- 🔄 Auto-refresh every 10 minutes (frontend only)
- 🛡️ LAN-only operation — no cloud, no exposure

---

## 🚀 Quick Start

```bash
git clone https://github.com/Mr-A-Hacker/flask_rtsp_stream_version2.git
cd flask_rtsp_stream_version2
pip install flask opencv-python
python app.py
```

Access the stream at:  
`http://<your-local-IP>:5051`

---

## 🧠 FFmpeg MJPEG Loop (Optional)

Use this loop to serve MJPEG from your RTSP camera:

```bash
while true; do
  ffmpeg -rtsp_transport tcp \
         -i rtsp://192.168.2.224:554/stream1 \
         -vf scale=640:360 \
         -f mjpeg http://0.0.0.0:8090/feed.mjpg
  echo "⚠️ FFmpeg exited. Restarting in 2 seconds..."
  sleep 2
done
```

Access MJPEG at:  
`http://<your-local-IP>:8090/feed.mjpg`

---

## 🛠️ Tech Stack

- Python 3  
- Flask  
- OpenCV  
- HTML/CSS (Bootstrap optional)  
- Threading + Local file system

---

## 📂 Repository Structure

```
flask_rtsp_stream_version2/
├── app.py                 # Flask app with MJPEG stream, recording, cleanup
├── templates/
│   └── index.html         # Viewer with fullscreen + auto-refresh
├── recordings/            # Auto-created folder for saved .avi files
└── README.md              # Cinematic GitHub documentation
```

---

## 📡 RTSP Compatibility

Tested with:
- Raspberry Pi 4 (Raspbian)
- Ubuntu 22.04
- RTSP camera with H.264 stream

---

## 🎞️ Recording Logic

- Records **30-minute** `.avi` segments
- Saves to `recordings/` folder
- Deletes files older than **4 hours**
- Resolution matches camera stream dynamically
- All storage is local — no cloud dependencies

---

## 💡 Viewer Features

- MJPEG stream via `/video_feed`
- Fullscreen toggle in browser
- Auto-refresh every 10 minutes
- Designed for LAN-only access

---

## 🔐 Security Notes

- No external APIs
- No user tracking
- No cloud uploads
- All data stays on your device

---

## 🧠 Legacy Intent

Built and maintained by [Mr-A-Hacker](https://github.com/Mr-A-Hacker)  
For forensic clarity, teachable deployment, and cinematic documentation.


<img width="374" height="328" alt="5" src="https://github.com/user-attachments/assets/255c6e49-bcd0-4b65-a845-c7e8e2bb94ab" />
