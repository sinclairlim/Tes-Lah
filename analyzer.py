import os
import cv2
from dotenv import load_dotenv
from pathlib import Path
from inference_sdk import InferenceHTTPClient

# Load env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# Roboflow API info
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")
ROBOFLOW_WORKSPACE = os.getenv("ROBOFLOW_WORKSPACE")
ROBOFLOW_WORKFLOW_ID = os.getenv("ROBOFLOW_WORKFLOW_ID")

# Roboflow client setup
client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=ROBOFLOW_API_KEY
)

def extract_frames(video_path, frame_numbers=[10, 12, 14]):
    cap = cv2.VideoCapture(video_path)
    extracted = []

    for num in frame_numbers:
        cap.set(cv2.CAP_PROP_POS_FRAMES, num)
        ret, frame = cap.read()
        if ret:
            path = f"frame_{num}.jpg"
            cv2.imwrite(path, frame)
            extracted.append(path)
            print(f"🖼️ Frame {num} extracted → {path}")
        else:
            print(f"⚠️ Failed to extract frame {num}")

    return extracted


def analyze_frames(image_paths, min_person_frames=2):
    person_frames = 0

    for path in image_paths:
        result = client.run_workflow(
            workspace_name=ROBOFLOW_WORKSPACE,
            workflow_id=ROBOFLOW_WORKFLOW_ID,
            images={"image": path},
            use_cache=True
        )

        if isinstance(result, list) and len(result) > 0:
            predictions = result[0].get("model_predictions", {}).get("predictions", [])
        else:
            predictions = []

        print(f"🔎 Results for {path} → {predictions}")

        # Check for "person" in current frame
        for pred in predictions:
            label = pred.get("class", pred.get("name", "")).lower()
            if label == "person":
                person_frames += 1
                break  # Only count once per frame

    print(f"🧮 Person detected in {person_frames} frame(s)")

    if person_frames >= min_person_frames:
        print("🚨 Threshold met — person confirmed.")
        return True
    else:
        print("✅ Person did not persist — no alert.")
        return False

def is_person_detected(detected_objects):
    return "person" in detected_objects

if __name__ == "__main__":
    test_video = "mock_SentryClips/2025-03-29_20-45-00/front.mp4"
    frame = extract_frame(test_video)
    if frame:
        objects = analyze_frame(frame)
        if is_person_detected(objects):
            print("🚨 Person detected!")
        else:
            print("✅ No person detected.")
