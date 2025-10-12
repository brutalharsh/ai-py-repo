import time
import threading
import logging
from datetime import datetime, timedelta
from typing import Callable, List, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TaskError(Exception):
    """Custom exception class for task-related errors."""
    pass


class Task:
    def __init__(self, func: Callable, run_at: Optional[float] = None, interval: Optional[float] = None):
        """
        Initialize a task with a function, a run time, and/or an interval.

        :param func: The function to be executed.
        :param run_at: The specific time at which the task will be executed (timestamp).
        :param interval: The interval in seconds at which the task will repeat.
        """
        self.func = func
        self.run_at = run_at
        self.interval = interval
        self.is_repeating = interval is not None
        self.thread = None

    def run(self):
        """Run the task and handle any exceptions."""
        try:
            self.func()
        except Exception as e:
            logging.error(f"Error while running task: {e}")

    def schedule_next_run(self):
        """Schedule the next run for repeating tasks."""
        if self.is_repeating:
            self.run_at = time.time() + self.interval


class TaskScheduler:
    def __init__(self):
        """Initialize the TaskScheduler."""
        self.tasks: List[Task] = []
        self.running = False
        self.lock = threading.Lock()

    def schedule_task(self, func: Callable, run_at: float):
        """
        Schedule a one-time task.

        :param func: The function to be executed.
        :param run_at: The specific time at which the task will be executed (timestamp).
        """
        if run_at <= time.time():
            raise TaskError("run_at time must be in the future.")
        with self.lock:
            self.tasks.append(Task(func, run_at=run_at))
            logging.info(f"Scheduled one-time task at {datetime.fromtimestamp(run_at)}")

    def schedule_repeating_task(self, func: Callable, interval: float):
        """
        Schedule a repeating task.

        :param func: The function to be executed.
        :param interval: The interval in seconds at which the task will repeat.
        """
        if interval <= 0:
            raise TaskError("Interval must be greater than zero.")
        with self.lock:
            self.tasks.append(Task(func, interval=interval, run_at=time.time() + interval))
            logging.info(f"Scheduled repeating task every {interval} seconds")

    def start(self):
        """Start the task scheduler."""
        self.running = True
        threading.Thread(target=self._run).start()
        logging.info("Task scheduler started")

    def stop(self):
        """Stop the task scheduler."""
        with self.lock:
            self.running = False
        logging.info("Task scheduler stopped")

    def _run(self):
        """Run the scheduler loop to execute tasks."""
        while self.running:
            now = time.time()
            with self.lock:
                for task in self.tasks[:]:
                    if task.run_at <= now:
                        task.thread = threading.Thread(target=task.run)
                        task.thread.start()
                        if task.is_repeating:
                            task.schedule_next_run()
                        else:
                            self.tasks.remove(task)
            time.sleep(1)

    def list_tasks(self):
        """List all currently scheduled tasks."""
        with self.lock:
            for task in self.tasks:
                logging.info(f"Task scheduled at {datetime.fromtimestamp(task.run_at)}, repeating: {task.is_repeating}")

    def cancel_task(self, func: Callable):
        """
        Cancel a specific task.

        :param func: The function of the task to be cancelled.
        """
        with self.lock:
            self.tasks = [task for task in self.tasks if task.func != func]
            logging.info("Task cancelled")


if __name__ == "__main__":
    def sample_task():
        print("Task executed at", time.ctime())

    def failing_task():
        raise ValueError("Intentional error")

    scheduler = TaskScheduler()

    try:
        # Schedule a one-time task
        scheduler.schedule_task(sample_task, run_at=time.time() + 5)

        # Schedule a repeating task every 10 seconds
        scheduler.schedule_repeating_task(sample_task, interval=10)

        # Schedule a task that will raise an error
        scheduler.schedule_task(failing_task, run_at=time.time() + 15)

        # Start the scheduler
        scheduler.start()

        # Let the scheduler run for 30 seconds
        time.sleep(30)

        # Stop the scheduler
        scheduler.stop()

    except TaskError as e:
        logging.error(f"TaskError: {e}")