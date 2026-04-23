import os
import socket
import platform

# Stage 1
def menu():
    # Display Menu
    while True:
        print("\nMain Menu")
        print("B - Ping a host")
        print("O - Port Scan ")
        print("M - Route Trace")
        print("T - Help")
        print("Q - Quit")

        choice = input("Choose the task you want to perform: ").strip().upper()

        if choice == "B":
            ping_host()
        elif choice == "O":
            port_scan()
        elif choice == "M":
            route_trace()
        elif choice == "T":
            help()
        elif choice == "Q":
            print("Program has been closed. See You Soon!😊")
            break
        else:
            print("Error !!! \nInvalid choice! Please select a valid option.")


# STAGE 2
# Ping
def ping_host():
    print("\nTo Ping  Host or IP ")

    while True:
        # User enters hostnames or IPs separated by commas
        targets = input("Enter hostnames or IP addresses (Separated by commas',' for two or more.").strip().split(',')
        targets = [target.strip() for target in targets if target.strip()]  # Remove extra spaces and empty inputs

        if not targets:
            print("Error! You must enter at least one hostname or IP address.")
            continue  # Prompt again if input is empty

        for target in targets:
            print(f"\nPinging {target}...\n")
            if platform.system().lower() == "windows":
                command = f"ping -n 4 {target}"
            else:
                command = f"ping -c 4 {target}"
            os.system(command)

        # Loop to ping more host until user exit
        while True:
            more = input("Do you want to ping another host or IP address? (Y/N): ").strip().upper()
            if more in ["Y", "N"]:
                break  # Valid choice, exit loop
            print(f"Error! '{more}' is not a valid option. Please enter 'Y' for Yes or 'N' for No.")

        if more == "N":
            break  # Exit ping a host

# Port Scan
def port_scan():
    while True:
        print("\nTo Scan for open ports on a target system.")
        target = input("Enter a hostname or IP address: ").strip()

        try:
            # Resolve hostname to IP if necessary
            target_ip = socket.gethostbyname(target)
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))

            print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")

            # Flag to track if any open ports are found
            open_ports_found = False

            for port in range(start_port, end_port + 1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)  # Lower timeout for faster scanning
                result = sock.connect_ex((target_ip, port))

                if result == 0:
                    print(f"Port {port} is open.")
                    open_ports_found = True
                sock.close()

            # If no open ports were found, print this message
            if not open_ports_found:
                print("No open port found.")

        except socket.gaierror:
            print("Error!! Invalid hostname. Could not resolve domain.")
        except ValueError:
            print("Error!! Invalid port number. Please enter numbers only.")
        except Exception as e:
            print(f"Error!! {e}")

        # Loop to scan more host until user exit
        while True:
            more = input("Do you want to scan another host or IP address? (Y/N): ").strip().upper()
            if more in ["Y", "N"]:
                break  # Valid choice, exit loop
            print(f"Error! '{more}' is not a valid option. Please enter 'Y' for Yes or 'N' for No.")

        if more == "N":
            break  # Exit scanning


# Route Trace
def route_trace():
    while True:
        print("\nTo Trace the route to a destination.")

        targets = input("Enter hostnames or IP addresses (separated by commas if multiple): ").strip().split(',')
        targets = [target.strip() for target in targets]  # Strip extra spaces

        for target in targets:
            print(f"\nTracing route to {target}...\n")
            if platform.system().lower() == "windows":
                command = f"tracert {target}"
            else:
                command = f"traceroute {target}"
            os.system(command)

        # Loop to route_trace more host until user exit
        while True:
            more = input("Do you want to trace another host or IP address? (Y/N): ").strip().upper()
            if more in ["Y", "N"]:
                break  # Valid choice, exit loop
            print(f"Error! '{more}' is not a valid option. Please enter 'Y' for Yes or 'N' for No.")

        if more == "N":
            break  # Exit tracing

# Help
def help():
    print("\nHelp Menu")
    print("B - Ping a Host: Checks if a host is reachable.")
    print("O - Port Scan: Scans a range of open ports on a host.")
    print("M - Route Trace: Shows the path packets take to reach a destination.")
    print("T - Help: Displays help menu.")
    print("Q - Quit: Exit the program.")
    input("\nPress Enter to return to the 'Main Menu'") # Return to Main Menu


if __name__ == "__main__":
    menu()
