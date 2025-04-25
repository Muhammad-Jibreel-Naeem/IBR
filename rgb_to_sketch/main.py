import cv2

# ——— Initialize webcam ———
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Couldn’t open your webcam. Did you scare it off?")

# ——— Main loop ———
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for speed (optional)
    frame = cv2.resize(frame, (640, 480))

    # Convert to gray (not RGB!)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Invert grayscale
    inv = 255 - gray

    # Blur the inverted image
    blur = cv2.GaussianBlur(inv, (21, 21), sigmaX=0, sigmaY=0)

    # Invert the blurred image
    inv_blur = 255 - blur

    # Create pencil-sketch by color dodge
    sketch = cv2.divide(gray, inv_blur, scale=256.0)

    # Convert sketch to BGR for side-by-side comparison
    sketch_bgr = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

    # Concatenate RGB (left) and Sketch (right) side by side
    combined = cv2.hconcat([frame, sketch_bgr])

    # Show side-by-side original & sketch
    cv2.imshow("Real-time Sketch Artist (Press Q to quit)", combined)

    # Quit on 'q' key
    if cv2.waitKey(1) & 0xFF in (ord('q'), ord('Q')):
        break

cap.release()
cv2.destroyAllWindows()