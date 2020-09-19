import subprocess
import time
import re
import os

BLUEJEANS = {
    "port_range": "5000",
    "proc_pattern": re.compile(r"bluejeans", flags=re.IGNORECASE),
}
MSFT_TEAMS = {
    "port_range": "50007-50060",
    "proc_pattern": re.compile(r"microsoft", flags=re.IGNORECASE),
}


def is_process_open(port_range, proc_pattern):
    # check ports, return process names
    cmd = f"lsof -nP -iUDP:{port_range} -Fc"
    out = subprocess.run(cmd.split(), capture_output=True, text=True).stdout
    if isinstance(out, str):
        # check if one of those processes matches the pattern
        out = [re.search(proc_pattern, s) for s in out.split("\n")]
        if any(out):
            return True
    return False


def connect_vpn():
    password = os.environ.get("ATD_PASSWORD")
    if password is None:
        return None
    cmd = "/opt/cisco/anyconnect/bin/vpn -s connect work.atd-us.com"
    credentials = f"\n\n{password}\n\n"
    with subprocess.Popen(
        cmd.split(),
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ) as p:
        p.communicate(input=credentials.encode())


def disconnect_vpn():
    cmd = "/opt/cisco/anyconnect/bin/vpn disconnect"
    subprocess.run(cmd.split(), capture_output=True)

def is_vpn_on():
    cmd = "/opt/cisco/anyconnect/bin/vpn state"
    out = subprocess.run(cmd.split(), capture_output=True, text=True).stdout
    if not isinstance(out, str):
        return False
    status = re.search("state: (\w+)", out).group(1)
    if status == "Connected":
        return True
    return False


while True:
    bj_open = is_process_open(**BLUEJEANS)
    teams_open = is_process_open(**MSFT_TEAMS)
    vpn_on = is_vpn_on()
    print("BlueJeans: ", "listening" if bj_open else "closed")
    print("Teams: ", "listening" if teams_open else "closed")
    print("VPN is on: ", vpn_on)
    if any([bj_open, teams_open]) and vpn_on:
        print("disconnecting!")
        disconnect_vpn()
    elif all([not bj_open, not teams_open]) and not vpn_on:
        print("reconnecting!")
        connect_vpn()
    print()
    time.sleep(2)
