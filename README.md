# Human Emojis - Emotion Detection App

A professional Streamlit web application for real-time emotion detection from images and videos using [DeepFace](https://github.com/serengil/deepface).

---

## 🚀 Features

- **Image Emotion Detection:** Upload an image and instantly receive emotion analysis.
- **Video Emotion Detection:** Upload a video and view detected emotions on sampled frames.
- **Modern, Intuitive UI:** Clean interface with responsive feedback and easy navigation.
- **Local Processing:** All computations are performed locally for privacy and speed.

---

## 🛠️ Requirements

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [DeepFace](https://github.com/serengil/deepface)
- OpenCV (`opencv-python`)
- Pillow (`PIL`)
- NumPy

---

## ⚙️ Installation

Install all dependencies with:

```bash
pip install streamlit deepface opencv-python pillow numpy
```

---

## ▶️ Usage

1. **Clone the repository or download the files.**
2. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
3. **Open the local URL provided by Streamlit in your browser.**
4. **Select "Upload Image" or "Upload Video" and upload your file to begin emotion detection.**

---

## 📁 File Structure

```
deep_face/
│
├── app.py         # Main Streamlit application
├── README.md      # Project documentation
```

---

## 💡 Notes

- For optimal results, use clear, front-facing images or videos with good lighting.
- All processing is performed locally; your data is never sent to external servers.
- The app supports common image formats (`jpg`, `jpeg`, `png`) and video formats (`mp4`, `avi`, `mov`).

---

## 📄 License

This project is intended for educational and research purposes only.

---