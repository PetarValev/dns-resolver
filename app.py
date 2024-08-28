import dns.resolver
from colorama import Fore, Style, init


init(autoreset=True)


def print_header():
    print(Fore.GREEN + Style.BRIGHT + "=" * 50)
    print(Fore.GREEN + Style.BRIGHT + " DNS Resolver Tool")
    print(Fore.GREEN + Style.BRIGHT + "=" * 50)


def print_footer():
    print(Fore.GREEN + Style.BRIGHT + "=" * 50)


def get_user_input():
    return input(Fore.CYAN + Style.BRIGHT + "Enter the domain you want to query: ")


def perform_dns_query(domain, record_types):
    print(Fore.YELLOW + Style.BRIGHT + "\nPerforming DNS lookups...\n")

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            print(Fore.MAGENTA + f"{record_type} records for {domain}:")
            for rdata in answers:
                print(Fore.WHITE + f" - {rdata}")
        except dns.resolver.NoAnswer:
            print(Fore.RED + f"No {record_type} record found for {domain}")
        except dns.resolver.NXDOMAIN:
            print(Fore.RED + f"Domain {domain} does not exist")
        except Exception as e:
            print(Fore.RED + f"Error retrieving {record_type} records: {e}")


def main():
    print_header()

    target_domain = get_user_input()

    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

    perform_dns_query(target_domain, record_types)

    print_footer()


if __name__ == "__main__":
    main()
