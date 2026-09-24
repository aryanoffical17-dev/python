import dns.resolver

def check_mx(domain):
    try:
        answers = dns.resolver.resolve(domain, "MX")

        print(f"MX records found for {domain}:")

        for record in answers:
            print(record.exchange)

        return True

    except dns.resolver.NoAnswer:
        print("No MX records found.")
        return False

    except dns.resolver.NXDOMAIN:
        print("Domain does not exist.")
        return False

check_mx("gmail.com")