import json
from typing import Dict, Any

class ConfigManager:
    """
    A utility class for managing JSON configuration files.

    Methods
    -------
    read_config(file_path: str) -> Dict[str, Any]:
        Reads configuration from a JSON file.
    
    write_config(file_path: str, config: Dict[str, Any]) -> None:
        Writes configuration to a JSON file.
    
    update_config(file_path: str, updates: Dict[str, Any]) -> None:
        Updates the configuration file with the provided updates.
    """

    @staticmethod
    def read_config(file_path: str) -> Dict[str, Any]:
        """
        Reads configuration from a JSON file.

        Parameters
        ----------
        file_path : str
            The path to the configuration file.

        Returns
        -------
        Dict[str, Any]
            The configuration settings.

        Raises
        ------
        FileNotFoundError
            If the configuration file is not found.
        json.JSONDecodeError
            If the configuration file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                config = json.load(file)
            return config
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in configuration file: {file_path}")

    @staticmethod
    def write_config(file_path: str, config: Dict[str, Any]) -> None:
        """
        Writes configuration to a JSON file.

        Parameters
        ----------
        file_path : str
            The path to the configuration file.
        config : Dict[str, Any]
            The configuration settings to be written.

        Raises
        ------
        IOError
            If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(config, file, indent=4)
        except IOError:
            raise IOError(f"Error writing to configuration file: {file_path}")

    @staticmethod
    def update_config(file_path: str, updates: Dict[str, Any]) -> None:
        """
        Updates the configuration file with the provided updates.

        Parameters
        ----------
        file_path : str
            The path to the configuration file.
        updates : Dict[str, Any]
            The configuration updates to be applied.

        Raises
        ------
        FileNotFoundError
            If the configuration file is not found.
        json.JSONDecodeError
            If the configuration file contains invalid JSON.
        IOError
            If there is an issue writing to the file.
        """
        try:
            config = ConfigManager.read_config(file_path)
            config.update(updates)
            ConfigManager.write_config(file_path, config)
        except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
            raise e

if __name__ == "__main__":
    config_path = "config.json"
    
    # Example configuration updates
    updates = {
        "setting1": "newValue",
        "setting2": 42
    }

    try:
        # Read config
        config = ConfigManager.read_config(config_path)
        print("Current config:", config)

        # Update config
        ConfigManager.update_config(config_path, updates)
        print("Updated config:", ConfigManager.read_config(config_path))

        # Write new config
        new_config = {"newSetting": "newValue"}
        ConfigManager.write_config("new_config.json", new_config)
        print("New config written to new_config.json")

    except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
        print(f"An error occurred: {e}")