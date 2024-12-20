<h4 align="center"> If you find this GitHub repo useful, please consider giving it a star! ⭐️ </h4> 
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

<img width="100%" align="centre" src="https://github.com/spyboy-productions/CloakQuest3r/blob/main/image/cloakquest3r.png" />

<be>

CloakQuest3r is a powerful Python tool meticulously crafted to uncover the true IP address of websites safeguarded by Cloudflare and other alternatives, a widely adopted web security and performance enhancement service. Its core mission is to accurately discern the actual IP address of web servers that are concealed behind Cloudflare's protective shield. Subdomain scanning is employed as a key technique in this pursuit. This tool is an invaluable resource for penetration testers, security professionals, and web administrators seeking to perform comprehensive security assessments and identify vulnerabilities that may be obscured by Cloudflare's security measures.


### 🚀 Run Online Free On `Google Colab`, `Google Shell`, `Binder`

<!-- 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github//spyboy-productions/CloakQuest3r/blob/main/cloakquest3r.ipynb)

[![Open in Cloud Shell](https://user-images.githubusercontent.com/27065646/92304704-8d146d80-ef80-11ea-8c29-0deaabb1c702.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/spyboy-productions/CloakQuest3r&tutorial=README.md)
-->

<p align="center">
<a href="https://colab.research.google.com/github//spyboy-productions/CloakQuest3r/blob/main/cloakquest3r.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="40"></a>
<a href="https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/spyboy-productions/CloakQuest3r&tutorial=README.md"><img src="https://user-images.githubusercontent.com/27065646/92304704-8d146d80-ef80-11ea-8c29-0deaabb1c702.png" alt="Open in Cloud Shell" height="40" ></a>
<a href="https://mybinder.org/v2/gh/spyboy-productions/CloakQuest3r/HEAD"><img src="https://mybinder.org/badge_logo.svg" alt="Open In Binder" height="40" ></a>
</p>


**Key Features:**
- **Real IP Detection:** CloakQuest3r excels in the art of discovering the real IP address of web servers employing Cloudflare's services. This crucial information is paramount for conducting comprehensive penetration tests and ensuring the security of web assets.

- **Subdomain Scanning:** Subdomain scanning is harnessed as a fundamental component in the process of finding the real IP address. It aids in the identification of the actual server responsible for hosting the website and its associated subdomains.

- **IP address History:** Retrieve historical IP address information for a given domain. It uses the ViewDNS service to fetch and display details such as IP address, location, owner, and last seen date.

- **SSL Certificate Analysis:** Extract and analyze SSL certificates associated with the target domain. This could provide additional information about the hosting infrastructure and potentially reveal the true IP address.

- **SecurityTrails API (optional):**  If you add your free SecurityTrails API key to the config.ini file, you can retrieve historical IP information from SecurityTrails.

- **Threaded Scanning:** To enhance efficiency and expedite the real IP detection process, CloakQuest3r utilizes threading. This feature enables the scanning of a substantial list of subdomains without significantly extending the execution time.

- **Detailed Reporting:** The tool provides comprehensive output, including the total number of subdomains scanned, the total number of subdomains found, and the time taken for the scan. Any real IP addresses unveiled during the process are also presented, facilitating in-depth analysis and penetration testing.

With CloakQuest3r, you can confidently evaluate website security, unveil hidden vulnerabilities, and secure your web assets by disclosing the true IP address concealed behind Cloudflare's protective layers.

#### Featured:

`CloakQuest3r` is one of the `Top 20 Most Popular Hacking Tools` in 2023 by `KitPloit`

- [Top 20 Most Popular Hacking Tools in 2023](https://www.kitploit.com/2023/12/top-20-most-popular-hacking-tools-in.html)

#### Limitation

```diff

- Sometimes it can't detect the real Ip.

- CloakQuest3r combines multiple indicators to uncover real IP addresses behind Cloudflare. While subdomain scanning is a part of the process, we do not assume that all subdomains' A records point to the target host. The tool is designed to provide valuable insights but may not work in every scenario. We welcome any specific suggestions for improvement.

- We created a proof of concept.

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
1. Run with a single command-line argument: the target domain you want to analyze.
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

3. The tool will check if the website is using Cloudflare. If not, it will inform you and ask if you still want to proceed.

4. If Cloudflare is detected, it will first print historical IP records and then it will scan for subdomains and identify their real IP addresses.

5. You will receive detailed output, including the number of subdomains scanned, the total number of subdomains found, and the time taken for the scan.
   
6. Any real IP addresses found will be displayed, allowing you to conduct further analysis and penetration testing.

it simplifies the process of assessing website security by providing a clear, organized, and informative report. Use it to enhance your security assessments, identify potential vulnerabilities, and secure your web assets.

---

**Optional**: [SecurityTrails API](https://securitytrails.com/)

Retrieves historical IP information from SecurityTrails. if you have an API key add it to the configuration file (config.ini).

Upon initial execution of the script, it generates a config.ini file with the following content:

```ini
[DEFAULT]
securitytrails_api_key = your_api_key
```

Subsequently, the script attempts to retrieve data from the SecurityTrails API. If the retrieval fails due to reasons such as quota limitations or site unavailability, the corresponding function is gracefully skipped.

<!-- 
#### Run It Online on replit.com 
It is just a demo and not all functionality is available. Please install the tool to access its full potential.

[![Run on Repl.it](https://repl.it/badge/github/spyboy-productions/CloakQuest3r)](https://replit.com/@spyb0y/CloakQuest3r)
-->
---
#### Contribution:

Contributions and feature requests are welcome! If you encounter any issues or have ideas for improvement, feel free to open an issue or submit a pull request.

#### 😴🥱😪💤 ToDo:

- Discover IP through website API calls (POC)
- Save all info on a Txt/CSV file.

#### 💬 If having an issue [Chat here](https://discord.gg/ZChEmMwE8d)
[![Discord Server](https://discord.com/api/guilds/726495265330298973/embed.png)](https://discord.gg/ZChEmMwE8d)

### ⭔ Snapshots:
---
<img width="100%" align="centre" src="https://github.com/spyboy-productions/CloakQuest3r/blob/main/image/snapshot_cloak.png" />
<!-- 
<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/1141162711464550430/1185878687388807238/Screenshot_2023-12-16_at_4.51.00_PM.png" />

<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/1141162711464550430/1185878687820828742/Screenshot_2023-12-16_at_4.51.45_PM.png" />
-->
<h4 align="center"> ‼️ Other Useful Tools 🤓 </h4> 

[R4ven](https://github.com/spyboy-productions/r4ven) Track Someone's Location Over The Internet.

[Facad1ng](https://github.com/spyboy-productions/Facad1ng) is a URL masking tool designed to help you Hide Phishing URLs.

[Omnisci3nt](https://github.com/spyboy-productions/omnisci3nt) is a powerful web reconnaissance tool.

[WebSecProbe](https://github.com/spyboy-productions/WebSecProbe) bypass 403.

[Valid8Proxy](https://github.com/spyboy-productions/Valid8Proxy) fetches, validates, and stores working proxies.

<h4 align="center"> If you find this GitHub repo useful, please consider giving it a star! ⭐️ </h4> 
