import socket

from core.logger import logger


def grab_banner(target, port, timeout):
    """
    Grab service banner from an open TCP port.
    """

    sock = None

    try:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(timeout)

        sock.connect((target, port))

        # ==================================
        # HTTP Services
        # ==================================

        if port in (80, 8080, 8000):
            request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"Connection: close\r\n\r\n"
            )

            sock.sendall(
                request.encode()
            )

        # ==================================
        # Receive Banner
        # ==================================

        banner = sock.recv(4096)

        # ==================================
        # Decode Banner
        # ==================================

        try:
            data = banner.decode(
                errors="ignore"
            ).strip()

        except UnicodeDecodeError:

            logger.error(
                f"Decode error | Port={port}"
            )

            return None

        # ==================================
        # Cleanup
        # ==================================

        if not data:
            return None

        # Remove common unwanted SSH message
        data = data.replace(
            "Protocol mismatch.",
            ""
        ).strip()

        return data

    except socket.timeout:

        logger.error(
            f"Banner timeout | Port={port}"
        )

        return None

    except ConnectionResetError:

        logger.error(
            f"Connection reset | Port={port}"
        )

        return None

    except ConnectionRefusedError:

        logger.error(
            f"Connection refused | Port={port}"
        )

        return None

    except Exception as e:

        logger.error(
            f"Banner grabbing failed | Port={port} | Error={e}"
        )

        return None

    finally:

        if sock:
            sock.close()