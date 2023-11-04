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

<be>

CloakQuest3r is a powerful Python tool meticulously crafted to uncover the true IP address of websites safeguarded by Cloudflare, a widely adopted web security and performance enhancement service. Its core mission is to accurately discern the actual IP address of web servers that are concealed behind Cloudflare's protective shield. Subdomain scanning is employed as a key technique in this pursuit. This tool is an invaluable resource for penetration testers, security professionals, and web administrators seeking to perform comprehensive security assessments and identify vulnerabilities that may be obscured by Cloudflare's security measures.

**Key Features:**
- **Real IP Detection:** CloakQuest3r excels in the art of discovering the real IP address of web servers employing Cloudflare's services. This crucial information is paramount for conducting comprehensive penetration tests and ensuring the security of web assets.

- **Subdomain Scanning:** Subdomain scanning is harnessed as a fundamental component in the process of finding the real IP address. It aids in the identification of the actual server responsible for hosting the website and its associated subdomains.

- **Threaded Scanning:** To enhance efficiency and expedite the real IP detection process, CloakQuest3r utilizes threading. This feature enables scanning of a substantial list of subdomains without significantly extending the execution time.

- **Detailed Reporting:** The tool provides comprehensive output, including the total number of subdomains scanned, the total number of subdomains found, and the time taken for the scan. Any real IP addresses unveiled during the process are also presented, facilitating in-depth analysis and penetration testing.

With CloakQuest3r, you can confidently evaluate website security, unveil hidden vulnerabilities, and secure your web assets by disclosing the true IP address concealed behind Cloudflare's protective layers.

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
   python cloakquest3r.py example.com
   ```

2. The tool will check if the website is using Cloudflare. If not, it will inform you that subdomain scanning is unnecessary.

3. If Cloudflare is detected, CloudScan will scan for subdomains and identify their real IP addresses.

4. You will receive detailed output, including the number of subdomains scanned, the total number of subdomains found, and the time taken for the scan.

---

#### 💬 If having an issue [Chat here](https://discord.gg/ZChEmMwE8d)
[![Discord Server](https://discord.com/api/guilds/726495265330298973/embed.png)](https://discord.gg/ZChEmMwE8d)

### ⭔ Snapshots:
---

5. Any real IP addresses found will be displayed, allowing you to conduct further analysis and penetration testing.

CloudScan simplifies the process of assessing website security by providing a clear, organized, and informative report. Use it to enhance your security assessments, identify potential vulnerabilities, and secure your web assets.
