# DNS Tester - Finding sub-domains tool

#### Basic Pentest tool to find the DNS just testing sub-domains of a URL.

## Install Socket Library
#### Linux 
###### First way
```
python3-pip pip install dns-resolver
```
###### Second way
```
pip install dnspython
```
___
#### Windows 
###### First way
```
pip install dns-resolver
```
###### Second way
```
pip install dnspython
```
___
### Import on project
```
import dns.resolver
```

### Creat the Resolver object
```
import dns.resolver

res = dns.resolver().Resolver()
```

### OS used
>Kali Linux VM
>
>Windows 10 - main OS

