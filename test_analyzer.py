from core.analyzer import analyze_banner


banner = "SSH-2.0-OpenSSH_9.0"


result = analyze_banner(banner)


print(result)