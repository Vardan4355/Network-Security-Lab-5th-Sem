# Experiment 10: Firewall and Intrusion Detection Setup with pfSense and Snort

## Aim

To configure an IDS on the pfSense firewall, review the LAN firewall policy, generate controlled test traffic, and verify that Snort produces corresponding alerts.

## Tools and Lab Setup

- pfSense firewall virtual machine
- Kali Linux virtual machine on the pfSense LAN
- Snort package enabled on the pfSense LAN interface
- Alert-only (blocking mode disabled) IDS configuration
- Example lab network: `192.168.1.0/24`

## Theory

A firewall checks packets against its ordered rules and decides whether to allow or block traffic. Rule evaluation is performed from top to bottom, so the final result depends on both rule order and interface direction.

An intrusion detection system (IDS) inspects traffic and compares it with detection rules. Snort can operate in alert-only mode, generating notifications without actively blocking packets. This makes it suitable for learning and traffic validation before a prevention policy is enabled.

A firewall and IDS provide complementary control: the firewall enforces policy, while the IDS identifies traffic that matches suspicious patterns or protocol signatures.

## Procedure

### 1. Record the pfSense network addresses

Start pfSense and check the console. Confirm the LAN address and the WebConfigurator address before opening the management interface.

In this lab:

- LAN network: `192.168.1.0/24`
- pfSense LAN address: `192.168.1.1/24`

![pfSense console showing network addresses](Screenshots/step_1_pfsense_console.png)

### 2. Open the pfSense WebConfigurator

From Kali or another device on the pfSense LAN, open:

```text
https://192.168.1.1
```

Sign in with the credentials configured for the laboratory environment.

![pfSense sign-in page](Screenshots/step_2_pfsense_login.png)

### 3. Review the LAN firewall rules

Navigate to:

**Firewall > Rules > LAN**

Review the source, destination, protocol, action, logging option, and rule order. Apply only the approved lab policy changes, then click **Apply Changes**.

Before testing, verify that ICMP is allowed and that no higher-priority rule unexpectedly blocks traffic.

![LAN firewall rules](Screenshots/step_3_firewall_rules.png)

### 4. Verify Kali's network configuration

Open a terminal on Kali and run:

```bash
ip -br address
ip route
```

Confirm that Kali has an address on the pfSense LAN. The test system used in this lab has:

```text
192.168.1.10/24
```

![Kali network interface and IP address](Screenshots/step_4_kali_network.png)

### 5. Enable Snort monitoring on the LAN interface

Navigate to:

**Services > Snort > Interfaces**

Enable Snort on the pfSense **LAN** interface and save the settings. Keep **Blocking Mode** disabled for the initial validation so that alerts are generated without stopping traffic.

After saving, check that the interface status shows Snort running.

![Snort interface status](Screenshots/step_5_snort_interface.png)

### 6. Generate controlled ICMP test traffic

From Kali, send four ICMP echo requests to the pfSense LAN address:

```bash
ping -c 4 192.168.1.1
```

The replies confirm end-to-end connectivity and provide simple traffic for the IDS to inspect.

For additional protocol testing, approved scanners such as `nmap` may be used to generate controlled TCP traffic:

```bash
sudo nmap -sS -Pn 192.168.1.1
```

> Use the Nmap example only inside an authorized lab network.

![Ping test from Kali to pfSense](Screenshots/step_6_ping_test.png)

### 7. Verify the alerts

Open:

**Services > Snort > Alerts**

Select the LAN interface and refresh the list. Match alerts to the test time and source address (`192.168.1.10`) while checking the SID, message, protocol, and destination fields.

For an alert-only setup, successful ping replies and an IDS event can occur together.

![Snort alert log showing ICMP events](Screenshots/step_7_snort_alerts.png)

## Improvements Added

- **Baseline before testing:** Record the firewall and IDS state before making changes to distinguish existing alerts from test-generated alerts.
- **Timestamp-based verification:** Filter the alert log by source address and test time instead of assuming every visible alert belongs to this experiment.
- **Alert retention:** Export or capture a screenshot of the relevant Snort entries for repeatable lab evidence.
- **Custom detection rule:** For a basic custom ICMP signature, a lab rule can be added to the Snort local rules file in an approved environment:

  ```text
  alert icmp 192.168.1.10 any -> 192.168.1.1 any (msg:"Lab ICMP test from Kali"; sid:1000001; rev:1;)
  ```

  Reload Snort after updating its rule set and confirm the SID appears in the alert list.

- **Safe progression to prevention:** Test in alert-only mode first. Blocking mode should only be enabled after rule tuning and false-positive review, because overly broad rules can interrupt legitimate traffic.

## Troubleshooting

- **No ping replies:** Verify the Kali address, pfSense LAN gateway, virtual-machine network mode, and LAN firewall rules.
- **No Snort alerts:** Confirm that Snort is enabled on LAN, that rules are downloaded and selected, that the interface process is running, and that the IDS alert view has the correct interface selected.
- **Too many alerts:** Filter by source address and recent time, and review whether broad community rules produce unrelated background traffic.
- **Certificate warning:** pfSense uses a self-signed management certificate. Verify the address and use the lab's approved certificate trust procedure.

## Result

The pfSense LAN firewall policy was reviewed, Kali was connected to the LAN, Snort was enabled on the LAN interface in alert-only mode, and controlled ICMP traffic was generated. The relevant activity was visible in the Snort alert interface.

## Discussion

The IDS does not replace firewall rules. The firewall defines which traffic is permitted, and the IDS helps security personnel identify and investigate traffic patterns that match configured signatures. Snort alert logs should be correlated with timestamps, source addresses, firewall rules, and packet captures to reduce false conclusions.

## Conclusion

This experiment demonstrates a basic defensive monitoring workflow using pfSense and Snort: validate network reachability, review firewall policy, enable alert-based monitoring, generate controlled traffic, and correlate IDS alerts with the test source and time.
