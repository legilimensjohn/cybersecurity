def format_packet_data(packet):
    """Format the packet data for display."""
    return f"Packet: {packet.summary()}"

def log_message(message):
    """Log a message to the console."""
    print(f"[LOG] {message}")
