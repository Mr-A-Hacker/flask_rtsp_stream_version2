> ## 👋 Start Here
> An iteration of the Flask RTSP streaming project. **For users:** this repository documents another stage of the camera-streaming experiments and is useful for comparing versions.
>
> **Safety:** Use security, camera, scanning, and network features only on systems and networks you own or are explicitly authorized to test.

---

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


## ⚙️ Camera IP Setup (Critical Step)

Before running the project, you **must update the camera IP address** in `app.py` to match your own RTSP camera.

### 🔍 Step 1: Find Your Camera’s IP

To locate your RTSP camera’s IP address:

- Log into your **router’s admin panel** (usually at `192.168.0.1` or `192.168.1.1`)
- Look under **Connected Devices** or **DHCP Clients**
- Find the device name that matches your camera brand/model
- Copy the IP address (e.g., `192.168.2.101`)

Alternatively, you can use a network scanner like `arp -a` or `nmap` to discover active devices.

#### 🧪 Optional: Use `nmap` to scan your LAN

```bash
nmap -sn 192.168.2.0/24
```

This command sends ping requests across your subnet and lists active devices with their IPs.
### 📝 Step 2: Update `app.py`

Open the file `app.py` in any code editor.  
Find the line that looks like this:

```python
camera_ip = "rtsp://192.168.2.244:554/stream1"
```

Replace `192.168.2.244` with your actual camera IP. For example:

```python
camera_ip = "rtsp://192.168.2.101:554/stream1"
```

Save the file.

### ✅ Step 3: Run the App

Now you're ready to launch:

```bash
python app.py
```

Access the stream at:  
`http://<your-local-IP>:5051`




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
