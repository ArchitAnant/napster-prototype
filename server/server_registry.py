"""
Server Registry - Manages client registration and peer list retrieval.
"""

from typing import Dict, List
import subprocess as sb
import re
from ipaddress import ip_address,ip_network

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
    # Add client to registry; handle duplicate client IDs
    # HINT: Use client_id as a unique key for each client.
    try:
        if client_ip not in client_registry.values():
            client_registry[client_id] = client_ip
            return True
        else:
            raise Exception
    except:
        return False

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
    # Return list of client IPs, excluding the requester
    # HINT: Filter client_id from the returned list.
    result = sb.run("arp -a", shell=True, stdout=sb.PIPE, stderr=sb.PIPE)
    raw_lines = result.stdout.decode('UTF-8').split("\n")
    pattern = r"\((.*?)\)"
    ips = []

    for line in raw_lines:
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            if is_private_ip(ip):
                if ip not in client_registry.values():
                    ips.append(ip)

    return ips

def is_private_ip(ip):
    private_ranges = [
        ip_network("10.0.0.0/8"),
        ip_network("172.16.0.0/12"),
        ip_network("192.168.0.0/16"),
    ]
    ip_obj = ip_address(ip)
    return any(ip_obj in private_range for private_range in private_ranges)

