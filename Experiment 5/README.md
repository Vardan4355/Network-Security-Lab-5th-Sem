# Experiment 5: TLS Handshake Analysis Using Wireshark

## Aim
To capture HTTPS traffic and analyze the TLS handshake using Wireshark.

## Theory
TLS (Transport Layer Security) is used to secure communication over the internet. It protects data from eavesdropping and verifies the identity of the server. When a browser connects to a secure website, it starts a TLS handshake before actual data transfer begins.

During the handshake, the client and server agree on:
- the TLS version
- the encryption method
- the key exchange parameters
- the certificate details needed for trust

## Tools Used
- Wireshark
- A browser using HTTPS
- Captured packet files

## Methodology
1. Start Wireshark and begin packet capture.
2. Open a secure website in the browser.
3. Stop the capture and save the packet file.
4. Inspect the ClientHello message.
5. Inspect the ServerHello response.
6. View the server certificate.
7. Decrypt the session if the TLS key log is available.

## Step 1: Capture the HTTPS traffic
We opened Wireshark and started capturing traffic while visiting a secure website. The captured packet files are shown below.

> [Original TLS Handshake Capture](https://github.com/4316sushil39/Network-Security-Lab/raw/main/Exp-5/Outputs/Exp5_tls_handshake.pcapng)
>
> [Decrypted TLS Capture](https://github.com/4316sushil39/Network-Security-Lab/raw/main/Exp-5/Outputs/Exp5_tls_decrypted.pcapng)

## Step 2: ClientHello Message
The ClientHello message is sent by the client to the server. It tells the server which TLS versions and security options the client supports.

![ClientHello Packet](https://github.com/4316sushil39/Network-Security-Lab/raw/main/Exp-5/Outputs/clienthello.png)

### Observation
From the ClientHello packet, we can see:
- the client supports TLS 1.2 and TLS 1.3
- multiple cipher suites are offered
- key exchange information is shared

## Step 3: ServerHello Message
The server responds with ServerHello. This message tells the client which TLS version and cipher suite were selected.

![ServerHello Packet](https://github.com/4316sushil39/Network-Security-Lab/raw/main/Exp-5/Outputs/serverhello.png)

### Observation
The ServerHello message shows:
- the selected TLS version
- the chosen cipher suite
- the server's key exchange details

## Step 4: Decrypt the TLS Traffic
Wireshark can decrypt the captured session if the TLS key log file is available. This allows us to see the later handshake messages that are normally hidden.

![Decrypted TLS Handshake](https://github.com/4316sushil39/Network-Security-Lab/raw/main/Exp-5/Outputs/decrypted.png)

### Observation
After decryption, messages such as:
- EncryptedExtensions
- Certificate
- CertificateVerify
- Finished

can be seen clearly. This proves that the client and server are successfully negotiating and preparing the secure session.

## Step 5: Inspect the Server Certificate
The certificate is used to verify the identity of the server. It contains the issuer, validity period, public key, and algorithm information.

![Certificate Details](https://github.com/4316sushil39/Network-Security-Lab/raw/main/Exp-5/Outputs/certificate.png)

### Observation
From the certificate, we can identify:
- the certificate holder
- the issuer
- the validity period
- the public key
- the security algorithm used

## Result
The TLS handshake was successfully captured and analyzed. We observed the ClientHello message, ServerHello response, certificate exchange, and the decrypted handshake process.

## Improvements
- Compare the handshake of different websites to understand how TLS versions and cipher suites differ in real traffic.
- Use a browser with TLS 1.3 enabled to study the modern secure connection process in detail.
- Analyze certificate chains and trust relationships to see how HTTPS verifies website identity.
- Capture traffic from multiple sessions to observe how the same server behaves under different conditions.

## Discussion
TLS is the security method used in HTTPS. It helps protect user data by encrypting communication and verifying the server identity. Wireshark allows us to view the details of this process and better understand how secure connections are established.

## Conclusion
This experiment helped us understand how a secure HTTPS connection is created. By analyzing ClientHello, ServerHello, and the certificate, we learned how TLS ensures confidentiality, integrity, and authentication during web communication.
