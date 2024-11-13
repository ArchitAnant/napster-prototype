# Napster-Prototype

This is a simplified Napster-like peer-to-peer file-sharing application prototype. The project consists of a server-client architecture where clients can register, discover peers, and share files in a distributed system. The project includes modular components with prototypes, comments, and hints to help participants ideate and implement their solutions during a hackathon.

## Project Structure

The project is divided into multiple directories to maintain modularity and scalability:

```
napster-prototype/
│
├── client/
│   ├── client_main.py              # Entry point for the client-side application.
│   ├── client_handler.py           # Handles client-side file operations (e.g., download, upload).
│   ├── client_registry.py          # Manages client registration and client-specific details.
│   ├── client_comm.py              # Manages communication with the server (requests, responses).
│   └── client_utils.py             # General-purpose utility functions for client-side.
│
├── server/
│   ├── server_main.py              # Entry point for the server-side application.
│   ├── server_registry.py         # Manages registered clients and their details.
│   ├── server_comm.py             # Handles communication with clients (requests, responses).
│   ├── server_utils.py            # Utility functions for server-side operations.
│   └── server_config.py           # Configuration settings for the server.
│
├── shared/
│   ├── protocol.py                # Defines shared request/response protocols.
│   ├── constants.py               # Shared constants (e.g., server IP, buffer size).
│   ├── utils.py                   # General-purpose utilities (e.g., encoding/decoding data).
│
├── data/
│   ├── client_data.json           # Stores file information of each client.
│   ├── peer_registry.json         # Simulates server's registry of clients.
│   └── config.json                # Configuration settings for the application.
│
└── README.md                      # This README file.
```

## Features

1. **Client Registration**: Clients can register with the server using their unique client ID and IP address.
2. **Peer Discovery**: Clients can discover other active peers by requesting a list from the server.
3. **File Sharing**: Clients can share files with other peers by sending and receiving data over a network connection.
4. **Modular Codebase**: The project is organized into multiple files for easy extension and customization.
5. **Prototypes and Hints**: Code contains detailed comments, TODOs, and function signatures, making it easier to understand and extend.

## Prerequisites

- Python 3.x
- Basic knowledge of socket programming and file handling.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/napster-prototype.git
cd napster-prototype
```

## Usage

### Server Setup

1. The server listens for client registration requests and peer discovery requests.
2. Modify the `server/config.json` file to adjust server settings such as IP address and port number.
3. Start the server by running the following command:

```bash
python server/server_main.py
```

### Client Setup

1. Clients connect to the server and can perform file-sharing operations (upload/download).
2. Modify the `client/config.json` to set the server IP and port number for client communication.
3. Start the client by running the following command:

```bash
python client/client_main.py
```

### Client-Server Interaction

- **Registration**: The client sends a registration request to the server to be added to the peer registry.
- **Peer Discovery**: After registering, the client can request a list of active peers from the server.
- **File Sharing**: Clients can download files from peers or upload files to peers based on mutual discovery.

## Code Walkthrough

The code is organized in a modular way to simulate file sharing and peer-to-peer communication. Here's a brief description of key components:

### `client/client_main.py`
- **Main entry point for the client-side application**. It starts the client, handles user interactions, and manages communication with the server.

### `server/server_main.py`
- **Main entry point for the server-side application**. It listens for client requests, registers clients, and handles peer discovery requests.

### `shared/protocol.py`
- **Defines standardized request/response protocols** for communication between clients and the server. It ensures consistent messaging.

### `shared/constants.py`
- **Shared constants** like server IP, port, buffer sizes, and timeout durations that are used across both client and server.

### `data/peer_registry.json`
- **Simulates the server's registry** of active clients with their client IDs and IP addresses. This allows the server to manage and track clients.

### `client/client_registry.py` and `server/server_registry.py`
- **Handle client registration** on both sides of the application, managing the mapping of client IDs to IP addresses.


## Codebase Outline

- **Directory Structure**:

 - client.py: Simulates the client-side interactions, connecting to peers and requesting files.
 - server.py: Acts as the central index for available files and clients (like a simple peer directory).
 - peer.py: Simulates individual peers sharing files with each other.

- **Key Components**:

 - Client Registration: Prototype for clients registering their IP and files with a central server.
 - File Search & Request: Code skeleton for clients to search for and request files from other peers.
 - File Transfer: Placeholder to show where actual file-sharing logic would be implemented (e.g., download/upload functions).
 - Peer-to-Peer Connection: Simulates basic P2P connections between clients.




## File Descriptions
***Client Folder***
client/__init__.py: Allows the client directory to be treated as a package.
client/client_main.py: Entry point for the client; handles initiating connections, searching for files, and requesting downloads from peers.
client/client_discovery.py: Implements logic for discovering peers by communicating with the server to get a list of active clients.
client/client_file_handler.py: Manages local files available for sharing; includes file metadata loading, updating, and storage.
client/client_peer_comm.py: Handles direct peer-to-peer file requests and transfers.

***Server Folder***
server/__init__.py: Allows the server directory to be treated as a package.
server/server_main.py: Main server program that handles client registration and acts as a central directory for peer discovery.
server/server_directory.py: Maintains records of active clients, their shared files, and metadata for file searching.
server/server_auth.py: Placeholder module for client authentication and security functions.
server/server_logging.py: Logs client connections, requests, and errors for system tracking and debugging.

***Shared Folder***
shared/__init__.py: Allows the shared directory to be treated as a package.
shared/protocol.py: Contains communication protocol details and constants for request and response codes, making communication uniform across client-server and peer-to-peer interactions.
shared/utils.py: Utility functions for tasks such as data serialization/deserialization, IP validation, and basic error handling.

***Data Folder***
data/client_data.json: JSON file used by the client to store local file metadata (e.g., filenames, file hashes).
data/server_directory.json: JSON file used by the server to maintain a directory of available files and active clients.

**README.md**
README.md: Provides documentation for setting up and running the prototype, as well as a brief description of each module and example commands.