def format_packet_data(packet):
    """Format the packet data for display."""
    return f"Packet: {packet.summary()}"

def log_message(message):
    """Log a message to the console."""
    print(f"[LOG] {message}")

def handle_exception(e):
    """Handle exceptions and log the error message."""
    log_message(f"Error: {str(e)}")