<h1>Fuzzing</h1>
Fuzzing is a Process of content Discovery (Subdomains, Files, Directories)

<b>One of the best tools is FFUF</b>

To install FFUF on Linux use this:
(comes preinstalled on Kali Lincox)
```
sudo apt install ffuf
```

Directory FUZZing
```
ffuf -u https://example.com/FUZZ -w {directory_wordlist}
```

Files FUZZing
```
ffuf -u https://example.com/files/FUZZ -w {files_wordlist}
```

Subdomain Enum
```
ffuf -u https://example.com -w {subdomain_wordlist} -H "Host: FUZZ.example.com"
```
