# Setting a Windows Firewall Rule to allow ArcGIS Server Management Ports On A Windows Machine

### Step 1
In the Start Menu Search and select "Windows Defender Firewall with Advanced Security"

### Step 2
Select "Inbound Rules" the select "New Rule..."

### Step 3
Within the "New Inbound Rule Wizard" Select the following for each step

Rule Type - Select "Port"
Protocol and Ports - select "Specific local Ports" and enter 6443,6080
Action - Select "Allow the connection" *should be selected by default*
Profile - Leave all selected *should be done by default*
Name - Give the Rule a suitable Name and Description 

Click "Finish" at the bottom to create the rule

### Step 4
Lastly Enable the Rule in the "Actions" Section of the "Windows Defender Firewall with Advanced Security" window
