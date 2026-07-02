import time
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
WATCH_DIR = "Incoming_Images"
RESULT_FILE = "results.json"
def extract_disaster_from_filename(image_name):
    name = image_name.lower()
    # ❌ Pre-disaster → no disaster
    if "pre_disaster" in name:
        return None
    base = os.path.basename(name)
    parts = base.replace(".jpg", "").replace(".png", "").split("_")
    # Special cases
    if parts[0] in ["hurricane", "socialfire", "social", "fire"]:
        return parts[0].capitalize()
    # Normal case → 2nd word
    if len(parts) > 1:
        return parts[1].capitalize()
    return "Unknown"
class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.lower().endswith((".jpg", ".png", ".jpeg")):
            self.process_image(event.src_path)
    def process_image(self, path):
        image_name = os.path.basename(path)
        # Decide source
        if "satellite" in path.lower():
            source = "Satellite"
        elif "drone" in path.lower():
            source = "Drone"
        else:
            source = "Unknown"
        disaster = extract_disaster_from_filename(image_name)
        result = {
            "detected": disaster is not None,
            "label": disaster,
            "confidence": 85.0,  # keep model confidence placeholder
            "source": source,
            "image": image_name
        }
        with open(RESULT_FILE, "w") as f:
            json.dump(result, f, indent=4)
        print(f"✅ Image processed → {image_name} | Disaster: {disaster}")
if __name__ == "__main__":
    os.makedirs(f"{WATCH_DIR}/drone", exist_ok=True)
    os.makedirs(f"{WATCH_DIR}/satellite", exist_ok=True)
    observer = Observer()
    observer.schedule(ImageHandler(), WATCH_DIR, recursive=True)
    observer.start()
    print("👀 Watching Incoming_Images folder...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
