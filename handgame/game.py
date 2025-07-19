import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

def detect_gesture(hand_landmarks):
    if not hand_landmarks:
        return 'none'

    # Get fingertip y-coordinates
    tips = [hand_landmarks.landmark[i] for i in [8, 12, 16, 20]]  # Index, Middle, Ring, Pinky
    dips = [hand_landmarks.landmark[i] for i in [6, 10, 14, 18]]  # First joints

    # Check for fist (all fingers down)
    fingers_down = sum(1 for tip, dip in zip(tips, dips) if tip.y > dip.y)
    if fingers_down >= 3:
        return '✊ Fist'

    # Check for palm (all fingers up)
    fingers_up = sum(1 for tip, dip in zip(tips, dips) if tip.y < dip.y)
    if fingers_up >= 3:
        return '✋ Palm'

    # Check for peace sign (index and middle up, others down)
    if tips[0].y < dips[0].y and tips[1].y < dips[1].y and tips[2].y > dips[2].y and tips[3].y > dips[3].y:
        return '✌ Peace'

    return 'No gesture'

# Main loop
while cap.isOpened():
    # Read frame from webcam
    success, image = cap.read()
    if not success:
        print("Failed to read from webcam")
        continue

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)
    
    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image and detect hands
    results = hands.process(image_rgb)

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
            
            # Detect and display gesture
            gesture = detect_gesture(hand_landmarks)
            
            # Add gesture text to image
            cv2.putText(
                image,
                f'Gesture: {gesture}',
                (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )

    # Display the image
    cv2.imshow('Hand Gesture Detection', image)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()