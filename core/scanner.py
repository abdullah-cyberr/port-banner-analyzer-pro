import socket

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)

from core.logger import setup_logger

logger = setup_logger()


def check_port(target, port, timeout):
    """
    Check whether a TCP port is open
    """

    try:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(timeout)

        result = sock.connect_ex(
            (target, port)
        )

        sock.close()

        if result == 0:
            return port

        logger.debug(
            f"Port {port} closed (code={result})"
        )

        return None


    except socket.timeout:
        logger.error(
            f"Timeout | Port={port}"
        )

        return None


    except ConnectionRefusedError:
        logger.warning(
            f"Connection Refused | Port={port}"
        )

        return None


    except OSError as e:
        logger.error(
            f"OS Error | Port={port} | {e}"
        )

        return None


    except Exception as e:
        logger.error(
            f"Unexpected Error | Port={port} | {e}"
        )

        return None



def scan_ports(target, start_port, end_port, timeout, threads):
    """
    Multi-threaded port scanning
    """

    open_ports = []

    total_ports = end_port - start_port + 1
    completed = 0


    with ThreadPoolExecutor(
        max_workers=threads
    ) as executor:


        futures = []


        for port in range(start_port, end_port + 1):

            future = executor.submit(
                check_port,
                target,
                port,
                timeout
            )

            futures.append(future)



        for future in as_completed(futures):

            completed += 1

            result = future.result()

            if result:
                open_ports.append(result)

    print(
         f"\nScan completed: {total_ports} ports checked"
    )
    return open_ports