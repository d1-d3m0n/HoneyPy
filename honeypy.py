import argparse
from ssh_honeypot import *
from web_honeypot import *
from logger_config import ssh_logger, error_logger


# parse arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-a','--address',type=str,required=True)
    parser.add_argument('-p','--port',type=int,required=True)
    parser.add_argument('-u','--username',type=str)
    parser.add_argument('-pw','--password',type=str)

    parser.add_argument('-s','--ssh',action="store_true")
    parser.add_argument('-w','--http',action="store_true")

    args = parser.parse_args()

    try:
        if args.ssh:
            print("[-]Running SSH HoneyPot....")
            username = args.username if args.username else None
            password = args.password if args.password else None
            honeypot(args.address, args.port, username, password)

        elif args.http:
            print("[-]Running HTTP HoneyPot....")
            username = args.username if args.username else "admin"
            password = args.password if args.password else "password"


            print(f"Port: {args.port} Username: {args.username} Password: {args.password}")
            run_web_honeypot(args.port,args.username,args.password)

         
        else:
            print("[!]Choose a particular honeypot type(SSH --ssh) or (HTTP --http).")

    except Exception as e:
        print(f"\n Exiting HONEYPOT....Error: {e}\n")
