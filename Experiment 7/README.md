# Experiment 7: Wireshark Analysis of a WPA2 EAPOL Handshake

## Aim
To identify and examine the four EAPOL-Key frames involved in a WPA2 four-way handshake using an existing Wireshark capture.

## Objectives
- Locate EAPOL-Key frames in a supplied capture.
- Identify the four messages of the WPA2 four-way handshake.
- Examine key fields and observe the exchange sequence.
- Record findings without attempting to recover credentials or interfere with wireless traffic.

## Theory
After a wireless client has associated with a WPA2 network, the client and access point perform a four-way handshake. The exchange confirms that both sides possess the required key material and establishes session keys for protected communication.

The handshake consists of four EAPOL-Key messages:

1. **Message 1:** The access point sends a nonce to the client.
2. **Message 2:** The client replies with its nonce and a message integrity check (MIC).
3. **Message 3:** The access point sends key-installation information and a MIC.
4. **Message 4:** The client acknowledges the exchange.

The exact fields shown can vary with the capture and Wireshark version. A capture may not contain all four messages, or some frames may be difficult to distinguish if the recording began late or packets were missed.

## Tools and Materials
- Wireshark
- An existing, authorized WPA2 packet capture (`.pcap` or `.pcapng`)
- A computer with permission to inspect the capture

## Procedure

1. Open Wireshark and load the supplied capture file using **File → Open**.
2. In the display-filter bar, enter:
   ```text
   eapol
   ```
   Apply the filter to show EAPOL packets.
3. Select each EAPOL packet and expand the **IEEE 802.1X Authentication** and **Key** sections in the packet details pane.
4. Examine the packet list and details to identify the handshake sequence. Use the source and destination addresses, packet order, replay information, nonce fields, and key information as supporting clues.
5. Record the frame number and relevant observations for each message. Do not infer missing messages if the capture does not contain enough evidence.
6. Clear the display filter to restore the full capture, then close the file when finished.

## Observation Table

| Message | Direction | Fields or indicators to examine | Observation |
|---|---|---|---|
| 1 | Access point → client | EAPOL-Key packet; key information; replay information; authenticator nonce | |
| 2 | Client → access point | EAPOL-Key packet; supplicant nonce; MIC; replay information | |
| 3 | Access point → client | EAPOL-Key packet; MIC; key-installation or secure indicators; replay information | |
| 4 | Client → access point | EAPOL-Key packet; MIC; secure indicator; replay information | |

## Results
The EAPOL-Key frames present in the supplied capture were filtered and examined. The handshake messages identified were:

- Message 1 — Frame number: ______
- Message 2 — Frame number: ______
- Message 3 — Frame number: ______
- Message 4 — Frame number: ______

If a message was not present or could not be identified, note that here: ____________________.

## Discussion
The four-way handshake is a sequence of EAPOL-Key exchanges between a client and an access point. Message direction, packet order, and fields such as nonce, MIC, replay information, and key-information flags help distinguish the messages. Wireshark’s packet details pane is useful for examining these fields, but the exact presentation can vary by capture and software version.

A capture may show only part of the handshake because recording started late, packets were lost, or the relevant exchange did not occur during capture. Therefore, conclusions should be based only on frames actually present. This experiment is limited to passive analysis of an authorized, existing capture; it does not involve capturing traffic from other networks or attempting password recovery.

## Improvements
- Record the capture filename and Wireshark version for reproducibility.
- Include frame numbers and packet directions in the observation table.
- Note any missing or unclear handshake messages rather than assuming they are present.
- Use only captures you are authorized to analyze, and keep screenshots readable while hiding sensitive details.

## Conclusion
The supplied capture was analyzed in Wireshark to locate and examine WPA2 EAPOL-Key traffic. The available frames were classified as handshake messages where the packet sequence and fields supported that identification.
