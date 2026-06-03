import json
from datetime import datetime

def convertFromFormat1(jsonObject):
    """
    Converts Format 1 telemetry into the unified format.
    Assumes an ISO timestamp string needs to be converted to milliseconds.
    """
    # 1. Extract the ISO timestamp (e.g., "2026-06-03T15:52:42.123Z")
    iso_timestamp = jsonObject.get("timestamp") or jsonObject.get("time")
    
    # 2. Convert ISO timestamp to milliseconds since epoch
    # Note: .replace("Z", "+00:00") handles the Zulu/UTC timezone safely in Python
    dt = datetime.fromisoformat(iso_timestamp.replace("Z", "+00:00"))
    ms_epoch = int(dt.timestamp() * 1000)
    
    # 3. Construct the unified object (Map your specific keys here)
    unified_data = {
        "timestamp": ms_epoch,
        "deviceId": jsonObject.get("device_id") or jsonObject.get("id"),
        "temperature": jsonObject.get("temp") or jsonObject.get("temperature"),
        # Add or map other fields found in data-result.json
    }
    
    return unified_data


def convertFromFormat2(jsonObject):
    """
    Converts Format 2 telemetry into the unified format.
    """
    # If Format 2 already uses epoch seconds or a different ISO layout, adjust here.
    # For example, if it's already an ISO string:
    iso_timestamp = jsonObject.get("recordedAt") 
    
    dt = datetime.fromisoformat(iso_timestamp.replace("Z", "+00:00"))
    ms_epoch = int(dt.timestamp() * 1000)
    
    unified_data = {
        "timestamp": ms_epoch,
        "deviceId": jsonObject.get("sensorId"),
        "temperature": jsonObject.get("reading"),
        # Add or map other fields found in data-result.json
    }
    
    return unified_data

# The rest of your main.py file containing the test execution runner goes below...
