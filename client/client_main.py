"""
Client Main - Entry point for initiating client operations.
Handles connecting to server, discovering peers, searching for files, and initiating peer-to-peer file transfers.
"""

from client.client_discovery import discover_peers
from client.client_file_handler import load_local_files, search_local_files
from client.client_peer_comm import request_file_from_peer
from shared.protocol import RequestType, ResponseType

class Client:
    def __init__(self, server_ip: str, client_id: str):
        """
        Initialize the client with server IP and unique client ID.
        
        Args:
            server_ip (str): IP address of the central server.
            client_id (str): Unique identifier for the client.
        """
        self.server_ip = server_ip
        self.client_id = client_id
        self.peer_list = []  # List of active peers discovered
        self.local_files = load_local_files()  # Load client’s available files for sharing

    def register_with_server(self) -> bool:
        """
        Registers client with the central server, making its file info available to other clients.
        
        Returns:
            bool: True if registration succeeds, False otherwise.
        """
        # TODO: Send client metadata to the server for registration.
        pass

    def discover_peers(self) -> list[str]:
        """
        Communicates with the server to get a list of active peers.
        
        Returns:
            list[str]: A list of peer IPs available for file sharing.
        """
        # TODO: Retrieve a list of active peers from the server
        # Example: self.peer_list = discover_peers(self.server_ip, self.client_id)
        pass

    def search_file(self, filename: str) -> list[str]:
        """
        Search for a file across local files and discovered peers.
        
        Args:
            filename (str): Name of the file to search for.
        
        Returns:
            list[str]: List of peers sharing the requested file.
        """
        # TODO: Search local files first, then contact each peer for the file
        # Example: return search_local_files(filename) or remote search
        pass

    def request_file(self, peer_ip: str, filename: str) -> ResponseType:
        """
        Requests a file from a specific peer.
        
        Args:
            peer_ip (str): IP address of the peer hosting the file.
            filename (str): Name of the file to request.
        
        Returns:
            ResponseType: The response from the peer, either file data or an error.
        """
        # TODO: Initiate P2P request to download the file from peer
        # Example: return request_file_from_peer(peer_ip, filename)
        pass

    def run(self):
        """
        Main loop to initiate registration, discover peers, and prompt for file searches and downloads.
        """
        # Register client with the central server
        if not self.register_with_server():
            print("Failed to register with the server.")
            return

        # Discover peers available for file sharing
        self.peer_list = self.discover_peers()
        print(f"Discovered peers: {self.peer_list}")

        # Example interaction loop (for user inputs in real implementation)
        # TODO: Implement command-line or GUI interaction for file search and download
        pass


# Example usage:
if __name__ == "__main__":
    client = Client(server_ip="192.168.1.1", client_id="client_001")
    client.run()
