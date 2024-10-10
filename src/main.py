import cv2
import numpy as np
import tensorflow as tf

# 딥러닝 모델 로드 (사전 학습된 모델 경로를 지정)
model = tf.keras.models.load_model('models/wasp_detector.h5')

# 카메라에서 실시간 영상 받기
cap = cv2.VideoCapture(0)

def preprocess_frame(frame):
    """
    입력된 프레임을 모델에 맞게 전처리하는 함수
    """
    img = cv2.resize(frame, (224, 224))  # 모델에 맞는 크기로 조정
    img = img / 255.0  # 정규화
    img = np.expand_dims(img, axis=0)  # 배치를 위한 차원 추가
    return img

def predict_wasp(frame):
    """
    프레임에서 말벌을 탐지하는 함수
    """
    processed_frame = preprocess_frame(frame)
    prediction = model.predict(processed_frame)
    
    # 예측 결과 (0: 말벌 없음, 1: 말벌 있음)
    if prediction[0][0] > 0.5:
        return True  # 말벌 탐지됨
    return False

while True:
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:
        break

    # 말벌 탐지
    if predict_wasp(frame):
        cv2.putText(frame, "Wasp Detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "No Wasp", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 결과 영상 출력
    cv2.imshow("Wasp Monitoring", frame)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
