import os
import requests # type: ignore

def banner():
    print(r"""
          
 ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗ ██████╗  ██████╗  ██╗██████╗ ██████╗ 
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗╚════██╗╚════██╗██╔═████╗███║██╔══██╗██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝ █████╔╝ █████╔╝██║██╔██║╚██║██████╔╝██║  ██║
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗ ╚═══██╗ ╚═══██╗████╔╝██║ ██║██╔══██╗██║  ██║
╚██████╗   ██║   ██████╔╝███████╗██║  ██║██████╔╝██████╔╝╚██████╔╝ ██║██║  ██║██████╔╝
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                      

    Cyber3301RD Web Tool - Ethical Hacking Framework
    """)

def test_payloads(url, payload_file):
    try:
        with open(payload_file, "r", encoding="utf-8") as file:  # Dosyayı UTF-8 olarak açıyoruz
            payloads = file.readlines()

        print(f"\n[+] Testing payloads on: {url}")
        for payload in payloads:
            payload = payload.strip()
            response = requests.get(url, params={"q": payload})  # GET isteğiyle test et
            if payload in response.text:
                print(f"[!] Potential Vulnerability Found with Payload: {payload}")
            else:
                print(f"[-] Payload Failed: {payload}")
    except Exception as e:
        print(f"[!] Error: {e}")

def main_menu():
    banner()
    print("Select an option:")
    print("1. ARP Spoofing")
    print("2. DNS Spoofing")
    print("3. View XSS Payloads")
    print("4. View SQL Injection Payloads")
    print("5. Test XSS Payloads on a Website")
    print("6. Test SQL Injection Payloads on a Website")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        os.system("python3 core/arp_spoofing.py")
    elif choice == "2":
        os.system("python3 core/dns_spoofing.py")
    elif choice == "3":
        with open("payloads/xss_payloads.txt", "r", encoding="utf-8") as file:
            print(file.read())
    elif choice == "4":
        with open("payloads/sql_payloads.txt", "r", encoding="utf-8") as file:
            print(file.read())
    elif choice == "5":
        url = input("Enter the target URL (e.g., http://example.com): ")
        test_payloads(url, "payloads/xss_payloads.txt")
    elif choice == "6":
        url = input("Enter the target URL (e.g., http://example.com): ")
        test_payloads(url, "payloads/sql_payloads.txt")
    elif choice == "7":
        print("Exiting...")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
