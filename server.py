# This program acts as a simple server, which in its first iteration accepts up to X
# connections and allows these users to broadcast to all

# Hopefully we will upgrade this later to include
# - Usernames
# - Private Messaging

# Note: I have used the following tutorial/code as the basis of my code:
# Python socket - chat server and client with code example
# published on Binary Tides by Silver Moon (March 31 2013)

import socket, select


