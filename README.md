# Service Drop
This is a program designed to constantly run in the background checking for internet connection.  
If internet connection is lost, an email will be crafted containing the time of disconnection and reconnection.  
When connection is reestablished, the email will be sent from an email of your choice to another.  

This was primarily for my friend who has an inconsistent connection to complain to his ISP.

## Requirements
Requires *nix  
Requires Python 3  
Requires the datetime package  

Run these commands to install the requirements:  
`sudo apt install python3`  
`sudo apt install python3-pip`  
`pip3 install datetime`  

## Usage
Due to the simplistic nature of this script, all arguments are just variables at the top of the document.

They may all be changed to suit your specific email requirements,  
but I would recommend leaving the email password as an argument.

`python3 servicedrop.py PASSWORD` or `./servicedrop.py PASSWORD`
