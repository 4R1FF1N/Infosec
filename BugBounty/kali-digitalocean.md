<h2> How to Setup Kali on Digital Ocean in 10 minutes </h2>

Getting Kali on Digital Ocean can be a bit retarded to set-up. So I found the fastest solution.

```
1. Setup A DEBIAN DROPLET on Digital Ocean.
2. Log in through SSH.
3. Change the sources List in /etc/apt/sources.lst
```
Paste the following command into the terminal.<br>
`echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list`

Then
```
sudo apt update && sudo apt upgrade
```

Then check the latest version of Kali here -> https://http.kali.org/kali/pool/main/k/kali-archive-keyring/
<br> For Example `https://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2024.1_all.deb`
```
wget https://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_{distro release year}_all.deb
apt install ./kali-archive-keyring_{distro release year}_all.deb
sudo apt update && sudo apt upgrade
sudo reboot
```
After reboot install all your tools -> https://www.kali.org/docs/general-use/metapackages/
