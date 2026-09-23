import requests
import sys

def load_wordlist(filepath): #function for loading a wordlist
    """Read a wordlist file and return a list of stripped lines."""
    try:
        with open(filepath, "r") as f:
            words = [line.strip() for line in f if line.strip()]
        print(f"[*] Loaded {len(words)} entries from {filepath}")
        return words
    except FileNotFoundError:
        print(f"[!] Error: '{filepath}' not found.")
        return []

def enumerate_subdomains(domain, wordlist): #function for enumerating subdomains
    """Test each subdomain candidate against the target domain."""
    found = []

    for sub in wordlist:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=3)
            print(f"[+] Found: {url}")
            found.append(url)
        except requests.ConnectionError:
            pass
        except requests.Timeout:
            pass

    return found

def enumerate_directories(target_url, wordlist):
    """Test each directory/file candidate against the target URL."""
    found = []

    for entry in wordlist:
        url = f"{target_url}/{entry}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code != 404:
                print(f"[+] {r.status_code} - {url}")
                found.append(url)
        except requests.ConnectionError:
            pass
        except requests.Timeout:
            pass

    return found

#-----------------------------menu-----------------------------

def show_menu():
    print("\n--- Web Enumeration Menu ---")
    print("1. Enumerate Subdomains")
    print("2. Enumerate Directories")
    print("3. Exit")

def get_target_domain():
    domain = input("Enter the target domain (e.g., example.com): ").strip()
    if not domain:
        print("[!] No domain entered. Exiting.")
        sys.exit(1)
    return domain

def get_target_url():
    target_url = input("Enter the target URL (e.g., http://example.com): ").strip()
    if not target_url:
        print("[!] No target URL entered. Exiting.")
        sys.exit(1)
    return target_url

def get_wordlist_path():
    wordlist_path = input("Enter the path to the wordlist file: ").strip()
    if not wordlist_path:
        print("[!] No wordlist file path entered. Exiting.")
        sys.exit(1)
    return wordlist_path

#-----------------------------main-----------------------------

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            domain = get_target_domain()
            print(f"[*] Starting subdomain enumeration for {domain}")
            wordlist = load_wordlist(get_wordlist_path())
            enumerate_subdomains(domain, wordlist)
            print("[*] Subdomain enumeration completed.")
            break

        elif choice == '2':
            target_url = get_target_url()
            print(f"[*] Starting directory enumeration for {target_url}")
            wordlist = load_wordlist(get_wordlist_path())
            enumerate_directories(target_url, wordlist)
            print("[*] Directory enumeration completed.")
            break

        elif choice == '3':
            print("Exiting...")
            sys.exit(0)

        else:
            print("[!] Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()

