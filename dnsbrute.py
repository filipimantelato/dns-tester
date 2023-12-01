import dns.resolver

res = dns.resolver.Resolver()
file = open("/home/eagle/subdomains-10k.txt", "r")
subdomains = file.read().splitlines()

target = ""
target = input("Enter site's URL: ")

for subdomain in subdomains:
	try:
		sub_target = subdomain + "." + target
		result = res.resolve(sub_target, "A")
		for ip in result:
			print(sub_target,"->", ip)
	except:
		pass
