Simple PHP RCE Webshells, upload this through FTP/Website and execute it.

Resources: 
Mime Types: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
File Extensions: https://fileinfo.com/filetypes/common
File Extensions v2: https://www.geeksforgeeks.org/list-of-file-formats/

#EXECUTION
1. Upload
2. Backtrack and find out where the file is stored (you may have to fuzz for it)
3. If you have found it, for example "httpx://GR1FF1N.com/files/avatars/images/webshell.php"
4. To execute you need to run the following URL: "httpx://GR1FF1N.com/files/avatars/images/webshell.php?command=whoami"
