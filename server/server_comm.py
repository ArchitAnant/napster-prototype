"""
Server Communication - Handles requests for client registration and peer discovery.
"""

from typing import Tuple
import socket
from server_registry import get_peer_list
# from server.server_registry import register_client, get_peer_list

def handle_registration_request(data: Tuple[str, str]) -> bool:
    """
    Processes a client registration request.

    Args:
        data (Tuple[str, str]): Tuple containing client_id and client_ip.

    Returns:
        bool: True if registration is successful, False otherwise.
    """
    client_id, client_ip = data
    # TODO: Use register_client to add client to registry
    # HINT: Extract client_id, client_ip from data tuple.
    pass

def handle_discovery_request(client_id: str) -> list[str]:
    """
    Processes a peer discovery request from a client.

    Args:
        client_id (str): Unique identifier of the client requesting peers.

    Returns:
        list[str]: List of IPs of available peers.
    """
    # TODO: Use get_peer_list to get list of other active peers
    pass

def sample_cp_interraction(connection : socket,client_registry,client_id):

    connection.sendall("Welcome client!\nDiscovering Peers".encode())
    peers = get_peer_list(client_registry,client_id)
    connection.sendall(f"{peers}".encode())
    # connection.close()

