"""
Server Registry - Manages client registration and peer list retrieval.
"""

from typing import Dict, List

def register_client(client_registry: Dict[str, str], client_id: str, client_ip: str) -> bool:
    """
    Registers a client in the server’s registry.

    Args:
        client_registry (Dict[str, str]): Dictionary of active clients.
        client_id (str): Unique identifier of the client.
        client_ip (str): IP address of the client.

    Returns:
        bool: True if the client was successfully registered, False otherwise.
    """
    # TODO: Add client to registry; handle duplicate client IDs
    # HINT: Use client_id as a unique key for each client.
    pass

def unregister_client(client_registry: Dict[str, str], client_id: str) -> bool:
    """
    Unregisters a client from the server.

    Args:
        client_registry (Dict[str, str]): Dictionary of active clients.
        client_id (str): Unique identifier of the client to remove.

    Returns:
        bool: True if unregistration succeeds, False otherwise.
    """
    # TODO: Remove client from registry safely
    pass

def get_peer_list(client_registry: Dict[str, str], client_id: str) -> List[str]:
    """
    Retrieves a list of active peers, excluding the requesting client.

    Args:
        client_registry (Dict[str, str]): Dictionary of active clients.
        client_id (str): ID of the requesting client.

    Returns:
        List[str]: List of IPs of other active clients.
    """
    # TODO: Return list of client IPs, excluding the requester
    # HINT: Filter client_id from the returned list.
    pass
