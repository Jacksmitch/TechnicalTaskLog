# Binding a certificate to port 443 in IIS For Windows 10

### Pre Requisites
Make sure you have IIS Manager installed and any other Microsoft SDKs installed and a certificate created.

### Step 1
Open up IIS Manager and in the Connections panel lick the "Sites" folder and select your site within the "Sites" folder. 

### Step 2
Next with your site selected in the Actions panel on the right click on "Bindings" option.

### Step 3
With the "Site Binding" window click on "Add..." if you do not have a already created binding for port 443 (if you have one select in the click "Edit..."). Then in the "Add Site Binding" window set type to https then make sure the IP address is "All Unassigned" and the Port is set to 443. Then at the bottom of the window with in the SSL certificate box select your created certificate the click OK.

### Thats All
See the below link if you need to see how to create a Self-Signed Certificate.

[Link]
