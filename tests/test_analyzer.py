from core.analyzer import analyze_banner


def test_ssh_banner_analysis():
    banner = "SSH-2.0-OpenSSH_9.0"

    result = analyze_banner(banner)

    assert result is not None