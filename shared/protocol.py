"""
Shared Protocol - Defines request and response types and shared constants for client-server communication.
"""

from enum import Enum
from typing import Dict, Any

class RequestType(Enum):
    """Enum representing types of requests a client can make to the server."""
    REGISTER = "register"
    DISCOVER_PEERS = "discover_peers"
    REQUEST_FILE = "request_file"
    SEND_FILE = "send_file"

class ResponseType(Enum):
    """Enum representing response types the server can return."""
    SUCCESS = "success"
    FAILURE = "failure"
    FILE_NOT_FOUND = "file_not_found"
    FILE_DATA = "file_data"

def create_request(request_type: RequestType, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Constructs a standardized request dictionary.

    Args:
        request_type (RequestType): Type of the request (e.g., REGISTER, DISCOVER_PEERS).
        data (Dict[str, Any]): Additional data for the request.

    Returns:
        Dict[str, Any]: A dictionary representing the request.
    """
    # TODO: Build a dictionary with request_type and data
    pass

def parse_response(response: Dict[str, Any]) -> ResponseType:
    """
    Parses a server response and identifies its type.

    Args:
        response (Dict[str, Any]): Dictionary containing response details.

    Returns:
        ResponseType: Type of the response (e.g., SUCCESS, FAILURE).
    """
    # TODO: Extract response type from response dictionary
    pass
