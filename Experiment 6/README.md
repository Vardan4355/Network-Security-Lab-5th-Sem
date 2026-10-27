# Experiment 6: Establish Remote Login Using SSH

## Aim
To establish a secure remote shell connection to a Linux host using SSH and verify the remote login.

## Theory
SSH (Secure Shell) provides an encrypted connection for remotely accessing and managing another computer. The client authenticates the server using its host key and then authenticates the user with a password or key pair. SSH is widely used for secure administration, file transfer, and remote command execution.

## Tools Used
- Kali Linux SSH client
- Metasploitable 2 virtual machine
- Virtual machines connected to the same lab network

## Methodology

### 1. Start the SSH service on Kali
The SSH service was started on the Kali machine:

```bash
sudo service ssh start
```

### 2. Connect to the remote host
The Metasploitable 2 host used in this experiment was reachable at `192.168.25.129`. Connect with the lab account:

```bash
ssh -o HostKeyAlgorithms=+ssh-rsa msfadmin@192.168.25.129
```

The `HostKeyAlgorithms` option enables the legacy RSA host-key algorithm required by this older lab target. Use this compatibility option only for the isolated lab host; do not weaken SSH settings on public systems.

At the first connection, SSH prompts to confirm the server's host-key fingerprint. Verify the fingerprint through a trusted channel before accepting it. Enter the account password when prompted; default lab credentials were used for this exercise.

### 3. Verify the remote session
After logging in, run commands such as:

```bash
whoami
hostname
pwd
```

The output should identify the remote account and host and show the current directory on that host. The session can be closed with `exit`.

## Screenshots

### 1. Successful SSH login
This screenshot shows the SSH connection being established and a shell opened on the remote Metasploitable host.

![Successful SSH login](https://github.com/4316sushil39/Network-Security-Lab/raw/main/Exp-6/Screenshots/01-ssh-login.png)

### 2. Remote host and network details
This screenshot shows commands run in the remote shell, including the SSH version and network interface details for the target.

![Remote host and network details](https://github.com/4316sushil39/Network-Security-Lab/raw/main/Exp-6/Screenshots/02-remote-host-details.png)

## Result
The SSH connection to the Metasploitable 2 host was established successfully. The remote shell and host details were verified.

## Conclusion
This experiment demonstrated remote login over SSH and verification of the connected host. SSH encrypts the remote session; users should verify host keys and use proper compatibility settings only in trusted lab environments.
