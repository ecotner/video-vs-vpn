# Video vs. VPN

A simple python script that checks open UDP connections at a regular interval to see whether they are being used by BlueJeans or Microsoft Teams, then turns the Cisco Anyconnect VPN off or on so that it doesn't interfere with your video conference experience, then resumes after so you can keep working.

## \*Disclaimer
I have only tested this on macOS Mojave version 10.14.6. Works on my machine!


## To do:
* Add support for Linux
    * The `lsof` command accepts different flags from the Mac version
* Add Windows support
    * I believe the `subprocess.Popen` function behaves differently on Windows
    * The location of the VPN binary is currently hardcoded and assumes a Unix filesystem structure
* Add support for more VPN's
    * Currently only supports Cisco Anyconnect
* Need support for more video conferencing apps
    * Zoom
    * Webex
    * Slack
    * more???
