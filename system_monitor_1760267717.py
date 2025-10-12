import system_resource_monitor as srm

def main():
    """
    The main function to start the system resource monitor.
    It initializes the monitor with a specified refresh interval and starts it.
    """
    try:
        # Initialize the SystemResourceMonitor with a refresh interval of 2 seconds
        monitor = srm.SystemResourceMonitor(refresh_interval=2)
        monitor.start()
    except Exception as e:
        # Handle any exceptions that occur and print the error message
        print(f"Error: {e}")

if __name__ == "__main__":
    """
    Example usage:
    This code block will only run if the module is executed as the main script.
    """
    main()