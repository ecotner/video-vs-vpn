# Video vs. VPN

A simple python script that checks open UDP connections at a regular interval to see whether they are being used by BlueJeans or Microsoft Teams, turns the Cisco Anyconnect VPN off so that it doesn't interfere with your video conference experience, then resumes after so you can keep working.

## \*Disclaimer
I have only tested this on macOS Mojave version 10.14.6. Works on my machine!


## To do:
Accepting PR's if you want to help contribute!
* Create an installation script that adds the program as a startup service
* Add some kind of CLI for modifying behavior mid-operation
* Add support for Linux
    * The `lsof` command accepts different flags from the Mac version
* Add Windows support
    * I believe the `subprocess.Popen` function behaves differently on Windows
    * The location of the VPN binary is currently hardcoded and assumes a Unix filesystem structure
* Add support for more VPN's
    * Currently only supports Cisco Anyconnect
* Need support for more video conferencing apps
    * Zoom, Webex, Slack
    * maybe all we need is a config file that maps process names to the ports they use?
