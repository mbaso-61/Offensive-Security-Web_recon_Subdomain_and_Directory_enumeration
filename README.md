# Web Enumeration Tool

A simple Python CLI tool for **subdomain** and **directory enumeration** against a target domain or URL. Built as a learning project for pentesting / bug bounty reconnaissance.

>  **Disclaimer** — Use this tool **only** on systems you own or CTF.

---

## Features

-  **Subdomain enumeration** from a wordlist
-  **Directory / file enumeration** from a wordlist
-  Simple interactive menu (no dependencies beyond `requests`)
-  Loads wordlists, skips empty lines

---

##  Requirements

- Python **3.8+**
- [`requests`](https://pypi.org/project/requests/)

Install dependencies:

```bash
pip install requests
```

---

## Installation

```bash
git clone https://github.com/mbaso-61/Offensive-Security-Web_recon_Subdomain_and_Directory_enumeration.git
cd Offensive-Security-Web_recon_Subdomain_and_Directory_enumeration
pip install -r requirements.txt
```

---

## Usage

Run the script:
```bash
python Subdomain_and_Directory_enumeration.py
```

You'll get an interactive menu:
```bash
--- Web Enumeration Menu ---
1. Enumerate Subdomains
2. Enumerate Directories
3. Exit
```

### 1 - Subdomain enumeration

Enter the target domain (e.g., example.com)

Provide the path to a wordlist (e.g., subdomains.txt)

Found subdomains are printed as [+] Found: http://sub.example.com

### 2 - Directory enumeration

Enter the target URL (e.g., http://example.com)

Provide the path to a wordlist (e.g., common.txt)

Non-404 responses are printed as [+] 200 - http://example.com/admin

### 3 - Exit

Close the program.

---

## Wordlist Examples

Where to find wordlists:

[SecLists](https://github.com/danielmiessler/SecLists)

---

## Roadmap / Improvements to do

The current version is a learning MVP from my TryHackMe courses. Here's what to do next, in priority order.

### Bug fixes 

□ Catch requests.exceptions.RequestException broadly (SSL, redirects, invalid URL) — currently only ConnectionError and Timeout are caught, so the program can crash mid-scan.

□ In enumerate_subdomains, check the HTTP status — right now a 404 counts as "Found".

□ Allow the menu to loop instead of break after one operation.

### Performance

□ Add multithreading (concurrent.futures.ThreadPoolExecutor) — sequential is very slow on large wordlists.

□ Use requests.Session() for keep-alive and a custom User-Agent.

□ Use HEAD requests instead of GET when possible (much faster).

□ Add retries with urllib3.util.Retry.

### Features

□ Support HTTPS + HTTP fallback (currently hard-coded to http://).

□ Configurable file extensions for dir enum (.php, .bak, .html, .git, …) via --extensions.

□ Save results to a file (-o results.txt, JSON, CSV).

□ Filter by HTTP status code or response size (soft-404 detection).

□ DNS-only mode (resolve without HTTP).

□ Rate limiting (--delay) to avoid hammering the target.

□ Respect robots.txt.




