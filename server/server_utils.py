"""
Server Utilities - Provides helper functions for logging, connections, and data formatting.
"""

import logging

def setup_logging():
    """
    Configures logging for the server to monitor events and errors.
    """
    # TODO: Setup Python logging with timestamp and log level
    pass

def format_client_data(client_id: str, client_ip: str) -> dict:
    """
    Formats client data for consistent storage.

    Args:
        client_id (str): Unique identifier of the client.
        client_ip (str): IP address of the client.

    Returns:
        dict: Dictionary containing formatted client information.
    """
    # TODO: Return client data as a dictionary for uniformity
    pass

def clean_up_on_exit(client_registry):
    """
    Cleans up resources and logs out clients when the server shuts down.
    
    Args:
        client_registry: The current client registry to clear.
    """
    # TODO: Handle server exit, remove clients, log status.
    pass
