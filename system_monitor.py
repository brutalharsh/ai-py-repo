import psutil
import time
import threading
import os
from datetime import datetime

class SystemMonitor:
    """
    A utility to monitor and log CPU and memory usage of the system.

    Attributes:
        interval (int): The interval in seconds between each log entry.
        log_file (str): The path to the file where logs will be saved.
        _monitoring (bool): A flag indicating whether the monitoring process is active.
        _thread (threading.Thread): The thread running the monitoring process.
    """

    def __init__(self, log_file='system_monitor.log', interval=5):
        """
        Initialize the SystemMonitor with the specified log file and interval.

        Args:
            log_file (str): The path to the file where logs will be saved.
            interval (int): The interval in seconds between each log entry.
        """
        self.interval = interval
        self.log_file = log_file
        self._monitoring = False
        self._thread = None

    def _log_usage(self):
        """Logs the CPU and memory usage to the specified log file."""
        with open(self.log_file, 'a') as file:
            while self._monitoring:
                try:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cpu_usage = psutil.cpu_percent(interval=1)
                    memory_info = psutil.virtual_memory()
                    memory_usage = memory_info.percent
                    log_entry = (f"{timestamp} | CPU: {cpu_usage}% | Memory: {memory_usage}% | "
                                 f"Available Memory: {memory_info.available/1024**2:.2f} MB\n")
                    file.write(log_entry)
                    print(log_entry.strip())
                    time.sleep(self.interval - 1)  # Adjust sleep to account for cpu_percent interval
                except IOError as e:
                    print(f"Error writing to log file: {e}")
                    self._monitoring = False
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    self._monitoring = False

    def start(self):
        """
        Start the monitoring process.
        """
        if not self._monitoring:
            self._monitoring = True
            self._thread = threading.Thread(target=self._log_usage)
            self._thread.start()

    def stop(self):
        """
        Stop the monitoring process.
        """
        if self._monitoring:
            self._monitoring = False
            self._thread.join()

    def status(self):
        """
        Get the current status of the monitoring process.

        Returns:
            bool: True if monitoring is active, False otherwise.
        """
        return self._monitoring

if __name__ == "__main__":
    monitor = SystemMonitor(log_file='system_usage.log', interval=5)
    try:
        monitor.start()
        # Run the monitor indefinitely or for a specific period
        while monitor.status():
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoring interrupted by user.")
    finally:
        monitor.stop()
        print("Monitoring stopped.")