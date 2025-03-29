from analyzer import extract_frames, analyze_frames

video = "mock_SentryClips/2025-03-28_20-42-34/2025-03-28_20-42-34-front.mp4"

frames = extract_frames(video, frame_numbers=[10, 12, 14])  # or more
if analyze_frames(frames, min_person_frames=2):
    print("🚨 Person lingered — alert triggered.")
else:
    print("✅ Quick appearance — no alert sent.")
