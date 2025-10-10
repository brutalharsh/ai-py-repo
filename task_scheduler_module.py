import schedule
import time
import logging
from datetime import datetime
from threading import Thread, Event

# Setting up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

class TaskScheduler:
    """
    A class used to schedule and automate tasks.

    Methods
    -------
    add_task(task, schedule_time, *args, **kwargs)
        Schedules a given task at the specified time.
    
    run_pending()
        Runs all tasks that are scheduled to run.
    
    start_scheduler(interval=1)
        Starts the scheduler to run tasks at specified intervals.
    
    stop_scheduler()
        Stops the scheduler.
    """
    
    def __init__(self):
        """
        Initializes the TaskScheduler with an empty task list and an event to stop the scheduler.
        """
        self.tasks = []
        self.stop_event = Event()
        self.scheduler_thread = None

    def add_task(self, task, schedule_time, *args, **kwargs):
        """
        Schedules a given task at the specified time.

        Parameters
        ----------
        task : function
            The task function to be scheduled.
        schedule_time : str
            The time when the task should be scheduled (e.g., "every().day.at('10:30')").
        *args : tuple
            Additional positional arguments to pass to the task function.
        **kwargs : dict
            Additional keyword arguments to pass to the task function.
        """
        try:
            job = eval(f"schedule.{schedule_time}.do(task, *args, **kwargs)")
            self.tasks.append(job)
            logging.info(f"Task {task.__name__} scheduled to run {schedule_time}")
        except NameError as e:
            logging.error(f"Error scheduling task: invalid schedule_time format. {e}")
        except Exception as e:
            logging.error(f"Error scheduling task: {e}")

    def run_pending(self):
        """
        Runs all tasks that are scheduled to run.
        """
        try:
            schedule.run_pending()
        except Exception as e:
            logging.error(f"Error running scheduled tasks: {e}")

    def start_scheduler(self, interval=1):
        """
        Starts the scheduler to run tasks at specified intervals.

        Parameters
        ----------
        interval : int, optional
            The interval time in seconds to check for scheduled tasks (default is 1).
        """
        if self.scheduler_thread and self.scheduler_thread.is_alive():
            logging.warning("Scheduler is already running")
            return
        
        logging.info("Scheduler starting")
        self.scheduler_thread = Thread(target=self._scheduler_loop, args=(interval,))
        self.scheduler_thread.start()

    def _scheduler_loop(self, interval):
        """
        The loop that runs the scheduler, checking for pending tasks at specified intervals.

        Parameters
        ----------
        interval : int
            The interval time in seconds to check for scheduled tasks.
        """
        logging.info("Scheduler loop started")
        while not self.stop_event.is_set():
            self.run_pending()
            time.sleep(interval)
        logging.info("Scheduler loop stopped")

    def stop_scheduler(self):
        """
        Stops the scheduler.
        """
        if not self.scheduler_thread or not self.scheduler_thread.is_alive():
            logging.warning("Scheduler is not running")
            return
        
        logging.info("Stopping scheduler...")
        self.stop_event.set()
        self.scheduler_thread.join()
        self.scheduler_thread = None
        logging.info("Scheduler stopped")

def example_task(message):
    """
    Example task function to demonstrate scheduled tasks.

    Parameters
    ----------
    message : str
        The message to log.
    """
    logging.info(f"Task executed with message: {message}")

if __name__ == "__main__":
    scheduler = TaskScheduler()
    
    # Add tasks to scheduler
    scheduler.add_task(example_task, "every(10).seconds", "Hello, World!")
    
    try:
        # Start the scheduler
        scheduler.start_scheduler()
    except KeyboardInterrupt:
        # Stop the scheduler on user interrupt
        scheduler.stop_scheduler()