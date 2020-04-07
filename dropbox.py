import dropbox


dropbox_access_token= "WCXmjTxxCFAAAAAAAAAAKLXth6xdYWqFi1K3j63K3JeuRKSvVFwEes5NXWncNFoS"    #Enter your own access token
dropbox_path= "/atharwa/abc.txt"
computer_path="abc.txt"


client = dropbox.Dropbox(dropbox_access_token)
print("[SUCCESS] dropbox account linked")


client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(computer_path))
