import streamlit as st
from deepface import DeepFace
import cv2
import numpy as np
from PIL import Image
import tempfile

st.set_page_config(page_title="Human Emojis - Emotion Detection", layout="centered")

st.title("😊 Human Emojis - Emotion Detection App")
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f5f7fa;
    }
    .sidebar .sidebar-content {
        background: #e3e6ec;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def Analyze_Emotion(img):
    try:
        analysis = DeepFace.analyze(
            img,
            actions=['emotion'],
            enforce_detection=False
        )
        return analysis[0]['emotion']
    except Exception as e:
        st.error(f"Error analyzing image: {e}")
        return None

option = st.selectbox('Select an option', ('Upload Image', 'Upload Video'))

if option == 'Upload Image':
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png" , "jfif"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        st.image(img_array, caption='Uploaded Image', use_column_width=True)
        emotion_scores = Analyze_Emotion(img_array)
        if emotion_scores:
            detected_emotion = max(emotion_scores, key=emotion_scores.get)
            st.success(f"**Detected Emotion:** {detected_emotion}")
        else:
            st.warning("No emotion detected or an error occurred.")

elif option == 'Upload Video':
    video_file = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov"])
    if video_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
            temp_video.write(video_file.read())
            temp_video_path = temp_video.name
        cap = cv2.VideoCapture(temp_video_path)
        frame_count = 0
        frame_rate = 50
        stframe = st.empty()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1
            if frame_count % frame_rate == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                emotion_scores = Analyze_Emotion(frame_rgb)
                if emotion_scores:
                    detected_emotion = max(emotion_scores, key=emotion_scores.get)
                    cv2.putText(frame_rgb, f"Emotion: {detected_emotion}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                else:
                    cv2.putText(frame_rgb, "No emotion detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                stframe.image(frame_rgb, channels="RGB", caption=f'Video Frame {frame_count}')
        cap.release()
        cv2.destroyAllWindows()
