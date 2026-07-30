import argparse
import socket

from core.utils import resolve_target
from core.scanner import scan_ports
from core.banner import grab_banner
from core.analyzer import analyze_banner
from core.exporter import export_json, export_csv
from core.logger import setup_logger
from core.colors import Colors


VERSION = "1.0"


def print_banner():

    print(Colors.INFO + "=" * 50 + Colors.RESET)

    print(
         Colors.SUCCESS +
          "      Port Banner Analyzer Pro"
          + Colors.RESET
)

    print(
         Colors.WARNING +
        "              v1.0"
         + Colors.RESET
)

    print(Colors.INFO + "=" * 50 + Colors.RESET)



def create_parser():

    parser = argparse.ArgumentParser(
        description="Port Banner Analyzer Pro"
    )


    parser.add_argument(
        "target",
        help="Target IP address or domain"
    )


    parser.add_argument(
        "-s",
        "--start",
        type=int,
        required=True,
        help="Starting port number"
    )


    parser.add_argument(
        "-e",
        "--end",
        type=int,
        required=True,
        help="Ending port number"
    )


    parser.add_argument(
        "--timeout",
        type=float,
        default=2.0,
        help="Socket timeout in seconds (default: 2.0)"
    )


    parser.add_argument(
        "--threads",
        type=int,
        default=50,
        help="Number of threads (default: 50)"
    )


    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}"
    )


    return parser




def main():

    print_banner()

    logger = setup_logger()


    try:

        logger.info("=" * 60)
        logger.info("Application Started")


        parser = create_parser()

        args = parser.parse_args()



        # ==========================
        # DNS Resolution
        # ==========================

        try:

            hostname, ip_address = resolve_target(
                args.target
            )


        except socket.gaierror:

            logger.error(
                f"DNS Resolution Failed | Target={args.target}"
            )

            print(
                f"\n[ERROR] Unable to resolve hostname: {args.target}"
            )

            return



        print(f"\nTarget      : {hostname}")
        print(f"IP Address  : {ip_address}")
        print(f"Start Port  : {args.start}")
        print(f"End Port    : {args.end}")
        print(f"Timeout     : {args.timeout}")
        print(f"Threads     : {args.threads}")


        print("\nScanning...")


        logger.info(
            f"Scan Started | Target={args.target} | "
            f"Ports={args.start}-{args.end}"
        )


        print("-" * 50)



        open_ports = scan_ports(
            args.target,
            args.start,
            args.end,
            args.timeout,
            args.threads
        )



        if not open_ports:

            print("No open ports found.")

            logger.info(
                "Scan Completed | No Open Ports"
            )

            return



        # Store scan results

        results = []



        for port in open_ports:


            print(
                 Colors.SUCCESS +
                 f"[OPEN] Port {port}"
                 + Colors.RESET
             )

 
            logger.info(
                f"Open Port Found: {port}"
            )


            banner = grab_banner(
                args.target,
                port,
                args.timeout
            )


            if banner:


                print(
                     Colors.INFO +
                     "Banner:"
                     + Colors.RESET
                 )
                
                preview_lines = banner.splitlines()[:8]

                print("\n".join(preview_lines))

                if len(banner.splitlines()) > 8:
                    print("...")
                    print("[Banner Truncated]")


                logger.info(
                    f"Banner Grabbed | Port={port}"
                )


                analysis = analyze_banner(
                    banner
                )


            else:


                print(
                    "Banner: Not Available"
                )


                logger.warning(
                    f"No Banner | Port={port}"
                )


                analysis = {

                    "service": "Unknown",
                    "software": "Unknown",
                    "version": "Unknown",
                    "vendor": "Unknown",
                    "os_hint": "Unknown"

                }


                banner = ""



            results.append({

                "port": port,
                "banner": banner,
                "service": analysis["service"],
                "software": analysis["software"],
                "version": analysis["version"],
                "vendor": analysis["vendor"],
                "os_hint": analysis["os_hint"],
                "risk": analysis.get("risk", [])

            })



            print(
                 Colors.WARNING +
                 "\nAnalysis:" +
                 Colors.RESET
)

            print(
                 Colors.INFO +
                 f"Service  : {analysis['service']}" +
                 Colors.RESET
)

            print(
                 f"Software : {analysis['software']}"
)

            print(
                 Colors.SUCCESS +
                 f"Version  : {analysis['version']}" +
                 Colors.RESET
)

            print(
                 f"Vendor   : {analysis['vendor']}"
             )

            print(
                 f"OS Hint  : {analysis['os_hint']}"
             )


            if analysis.get("risk"):

                 print("\nSecurity Risk:")

                 print("-" * 20)
                 risk_data = analysis["risk"]

                 print(
                         f"Level  : {risk_data['level']}"
                     )

                 print(
                         f"Score  : {risk_data.get('score', analysis.get('risk_score', 0))}/100"
)

                 print(
                         f"Severity : {risk_data.get('severity', analysis.get('severity', 'LOW'))}"
)
                 if risk_data["cves"]:
                    print("\nCVEs:")
                    for cve in risk_data["cves"]:
                        print(f" - {cve}")


                 if risk_data["reasons"]:
                         print("\nReasons:")

                         for reason in risk_data["reasons"]:
                             print(f" - {reason}")

                 if risk_data["details"]:
                        print("\nRecommendations:")
                        for detail in risk_data["details"]:
                            if "recommendation" in detail:
                                print(
                                    f"- {detail['recommendation']}"
                                )

                 print()

            else:

                 print("\nSecurity Risk: None")
        print(
            f"Total Open Ports: {len(open_ports)}"
        )



        json_file = export_json(results)

        csv_file = export_csv(results)



        logger.info(
            f"JSON Report Saved: {json_file}"
        )


        logger.info(
            f"CSV Report Saved: {csv_file}"
        )



        print("\nReports Saved")

        print(
            f"JSON : {json_file}"
        )

        print(
            f"CSV  : {csv_file}"
        )


        logger.info(
            "Scan Completed Successfully"
        )



    except KeyboardInterrupt:


        print("\n")

        print(
            "[!] Scan interrupted by user"
        )


        logger.warning(
            "Scan interrupted by user"
        )


        print(
            "[!] Shutdown completed"
        )


        logger.info(
            "Application shutdown completed"
        )



    except Exception as e:

        logger.exception(
             "Unexpected Application Error"
    )

        print(
          "\n[ERROR] Application failed unexpectedly."
    )

        print(
         "Check logs/scanner.log for details."
    )





if __name__ == "__main__":

    main()