from datetime import datetime
import json
import os

class WaterReading:
    def __init__(self, name: str, pH: float, temperature: float, ammonia: float, timestamp: str = None):
        # Use provided timestamp if available, otherwise create new one
        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        self.name = name
        self.pH = pH
        self.temperature = temperature
        self.ammonia = ammonia

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "name": self.name,
            "pH": self.pH,
            "temperature": self.temperature,
            "ammonia": self.ammonia,
        }


class ReadingManager:
    def __init__(self, username: str = None):
        self.readings = []
        self.username = username
        self.file_path = None

        # Create a base "users" directory
        base_dir = os.path.join(os.getcwd(), "users")
        os.makedirs(base_dir, exist_ok=True)

        # Create user-specific folder
        if username:
            user_dir = os.path.join(base_dir, username)
            os.makedirs(user_dir, exist_ok=True)

            # Path to user's data file
            self.file_path = os.path.join(user_dir, "readings.json")
            self.load_readings()

    def add_reading(self, reading: WaterReading):
        self.readings.append(reading)
        self.save_readings()
        self.load_readings()


    def get_all(self):
        return [r.to_dict() for r in self.readings]

    def clear_readings(self):
        self.readings.clear()
        self.save_readings()

    def save_readings(self):
        """Save readings to the user's folder (JSON file)."""
        if not self.file_path:
            return
        with open(self.file_path, "w") as f:
            json.dump([r.to_dict() for r in self.readings], f, indent=4)

    def load_readings(self):
        """Load readings from the user's JSON file if it exists."""
        if not self.file_path or not os.path.exists(self.file_path):
            return
        
        with open(self.file_path, "r") as f:
            data = json.load(f)
        
        self.readings = [WaterReading(d["name"], d["pH"], d["temperature"], d["ammonia"], d["timestamp"]) for d in data]