<p align="center">
    <a href="https://spyboy.in/twitter">
      <img src="https://img.shields.io/badge/-TWITTER-black?logo=twitter&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://spyboy.in/">
      <img src="https://img.shields.io/badge/-spyboy.in-black?logo=google&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://spyboy.blog/">
      <img src="https://img.shields.io/badge/-spyboy.blog-black?logo=wordpress&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://spyboy.in/Discord">
      <img src="https://img.shields.io/badge/-Discord-black?logo=discord&style=for-the-badge">
    </a>
  
</p>

<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/1141162711464550430/1182112665364074536/cloak.png" />

<be>

CloakQuest3r is a powerful Python tool meticulously crafted to uncover the true IP address of websites safeguarded by Cloudflare, a widely adopted web security and performance enhancement service. Its core mission is to accurately discern the actual IP address of web servers that are concealed behind Cloudflare's protective shield. Subdomain scanning is employed as a key technique in this pursuit. This tool is an invaluable resource for penetration testers, security professionals, and web administrators seeking to perform comprehensive security assessments and identify vulnerabilities that may be obscured by Cloudflare's security measures.

**Key Features:**
- **Real IP Detection:** CloakQuest3r excels in the art of discovering the real IP address of web servers employing Cloudflare's services. This crucial information is paramount for conducting comprehensive penetration tests and ensuring the security of web assets.

- **Subdomain Scanning:** Subdomain scanning is harnessed as a fundamental component in the process of finding the real IP address. It aids in the identification of the actual server responsible for hosting the website and its associated subdomains.

- **IP address History:** Retrieve historical IP address information for a given domain. It uses the ViewDNS service to fetch and display details such as IP address, location, owner, and last seen date.

- **SSL Certificate Analysis:** Extract and analyze SSL certificates associated with the target domain. This could provide additional information about the hosting infrastructure and potentially reveal the true IP address.

- **Threaded Scanning:** To enhance efficiency and expedite the real IP detection process, CloakQuest3r utilizes threading. This feature enables scanning of a substantial list of subdomains without significantly extending the execution time.

- **Detailed Reporting:** The tool provides comprehensive output, including the total number of subdomains scanned, the total number of subdomains found, and the time taken for the scan. Any real IP addresses unveiled during the process are also presented, facilitating in-depth analysis and penetration testing.

With CloakQuest3r, you can confidently evaluate website security, unveil hidden vulnerabilities, and secure your web assets by disclosing the true IP address concealed behind Cloudflare's protective layers.

#### Limitation

```diff

- Sometimes it can't detect the real Ip.

- CloakQuest3r combines multiple indicators to uncover real IP addresses behind Cloudflare. While subdomain scanning is a part of the process, we do not assume that all subdomains' A records point to the target host. The tool is designed to provide valuable insights but may not work in every scenario. We welcome any specific suggestions for improvement. 

1. False Negatives: CloakReveal3r may not always accurately identify the real IP address behind Cloudflare, particularly for websites with complex network configurations or strict security measures.

2. Dynamic Environments: Websites' infrastructure and configurations can change over time. The tool may not capture these changes, potentially leading to outdated information.

3. Subdomain Variation: While the tool scans subdomains, it doesn't guarantee that all subdomains' A records will point to the primary host. Some subdomains may also be protected by Cloudflare.

```
<h4 align="center"> This tool is a Proof of Concept and is for Educational Purposes Only. </h4> 

---

<h4 align="center">
  OS compatibility :
  <br><br>
  <img src="https://img.shields.io/badge/Windows-05122A?style=for-the-badge&logo=windows">
  <img src="https://img.shields.io/badge/Linux-05122A?style=for-the-badge&logo=linux">
  <img src="https://img.shields.io/badge/Android-05122A?style=for-the-badge&logo=android">
  <img src="https://img.shields.io/badge/macOS-05122A?style=for-the-badge&logo=macos">
</h4>

<h4 align="center"> 
Requirements:
<br><br>
<img src="https://img.shields.io/badge/Python-05122A?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Git-05122A?style=for-the-badge&logo=git">
</h4>


**How to Use:**
1. Run CloudScan with a single command-line argument: the target domain you want to analyze.
   ```
    git clone https://github.com/spyboy-productions/CloakQuest3r.git
    ```
    ```
    cd CloakQuest3r
    ```
    ```
    pip3 install -r requirements.txt
    ```
    `For Termux(android) User` use the command given below if having trouble installing `cryptography` using requirements.txt

    `pkg install python-cryptography` 

   ```
   python cloakquest3r.py example.com
   ```

3. The tool will check if the website is using Cloudflare. If not, it will inform you that subdomain scanning is unnecessary.

4. If Cloudflare is detected, CloudScan will scan for subdomains and identify their real IP addresses.

5. You will receive detailed output, including the number of subdomains scanned, the total number of subdomains found, and the time taken for the scan.
   
6. Any real IP addresses found will be displayed, allowing you to conduct further analysis and penetration testing.

CloudScan simplifies the process of assessing website security by providing a clear, organized, and informative report. Use it to enhance your security assessments, identify potential vulnerabilities, and secure your web assets.

#### Run It Online:

Run it online on replit.com : https://replit.com/@spyb0y/CloakQuest3r

---
#### Contribution:

Contributions and feature requests are welcome! If you encounter any issues or have ideas for improvement, feel free to open an issue or submit a pull request.

#### 😴🥱😪💤 ToDo:

- Add free API (ex: securitytrails)
- Discover IP through website API calls (POC)
- Save all info on a Txt/CSV file.

#### 💬 If having an issue [Chat here](https://discord.gg/ZChEmMwE8d)
[![Discord Server](https://discord.com/api/guilds/726495265330298973/embed.png)](https://discord.gg/ZChEmMwE8d)

### ⭔ Snapshots:
---
<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/746328746491117611/1170359842687418488/Screenshot_2023-11-04_at_7.21.44_PM.png" />

