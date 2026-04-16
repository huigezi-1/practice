import sys

def is_ip(s):
    parts = s.split(".")
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        
        if not part.isdigit():
            return False
        
        num = int(part)
        
        if num <0 or num >255:
            return False
        
    return True

def process_ip_input():
    total_found = 0
    unique_ips = []

    while True:
        line = sys.stdin.readline()

        if not line:
            break

        line = line.strip()

        words = line.split()

        for word in words:

            if is_ip(word):
                total_found += 1

                if word not in unique_ips:
                    unique_ips.append(word)

    print(f"Total IPs found (with duplicates): {total_found}")
    print(f"Unique IPs: {len(unique_ips)}")
    print(f"Result: {unique_ips}")
    

if __name__ == "__main__":
    process_ip_input()
