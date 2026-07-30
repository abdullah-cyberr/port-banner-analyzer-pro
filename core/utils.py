import socket


def resolve_target(target):
    """
    Resolve hostname to IP address.
    Returns:
        (hostname, ip_address)
    Raises:
        socket.gaierror if hostname is invalid.
    """

    ip_address = socket.gethostbyname(target)
    hostname = socket.getfqdn(ip_address)

    return hostname, ip_address