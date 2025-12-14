# Import necessary modules
import psutil
import time
import logging

threshold = 80  # Set threshold to 80%

print("Monitoring CPU usage...")

try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        
        if cpu_usage > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
        else:
            print(f"CPU Usage is normal: {cpu_usage}%")
            
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
except Exception as e:
    print(f"Error occurred: {e}")
