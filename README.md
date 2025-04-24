# PowerDDoS v1.0

**PowerDDoS v1.0** is an educational tool for testing the stability and security of web servers by performing **UDP**, **TCP SYN**, and **HTTP GET** flood attacks. It is designed for educational purposes only and should be used responsibly on servers you own or have explicit permission to test.

## Features:
- **Multithreaded Attacks**: Run multiple types of DDoS attacks simultaneously (UDP, TCP SYN, HTTP GET).
- **Simple to Use**: A straightforward interface to start attacks with just a few inputs.
- **Works on Termux**: This script works seamlessly on Termux (Android environment).

## How to Use:

### **1. Prerequisites**:
Before running the script, make sure you have **Python 3** and required packages installed in Termux.

### **2. Install Dependencies**:

Open Termux and run the following commands to install the necessary dependencies:

```bash
pkg update && pkg upgrade
pkg install python
pkg install python3
pkg install git
pkg install figlet

3. Script Setup:

Option 1: Manually Paste the Script

1. Open the Termux terminal and create a Python file:

nano powerddos.py


2. Copy the PowerDDoS v1.0 script and paste it inside the file.


3. Save the file by pressing CTRL + X, then Y to confirm.



Option 2: Clone the GitHub Repository (if available)

If the script is hosted on GitHub, you can clone the repository with:

git clone https://github.com/your-repository-url/powerddos.git
cd powerddos

4. Running the Script:

Now, run the script in Termux with the following command:

python3 powerddos.py

5. Follow the prompts:

Once the script is running, it will prompt you for the following:

Target IP Address: The IP address of the server you want to test.

Port: The target port (e.g., 80 for HTTP).

Duration: How long the attack should last (in seconds).

Attack Type: Select the type of attack (UDP, SYN, HTTP).
