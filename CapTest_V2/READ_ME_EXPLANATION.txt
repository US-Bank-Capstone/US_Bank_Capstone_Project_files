Hello there,

The folder of CapTest_V2 contains a prototype configuration on how you can use a CSV file to modify specific configurations located within a Jinja2 file template directory. This is a proof of concept and not the final product of this project. 

Jinja (aka Jinja2) is a template engine that allows the user to create various files based on a template given. For this example, we will be using a "show run" configuration file from a test router as our template. 
NOTE: This is for testing purposes. Your configurations will likely be different than mine if you want to make your own template file.
To make our tempalte file compatiable with our program, we will need to ask ourselves 1 question:

What do we want to modify within the configuration file?

We will be modifying the following:

*Hostname
*IP address
*Subnet Mask
*Router OSPF


JINJA2 FILE EXPLANATION

To modify these sections of the our Jinja2 file, we will need to identify these sections as variables. To create a jinja2 variable, use, " {{ *name of variable* }} ".
For example, hostname R1 will be called: hostname {{ router_name }}. 

*view the router_template.j2 file to view further examples for the ip address, subnet mask, and ospf*


CSV FILE EXPLANATION

The CSV file will contain the specific information for our template. The values placed within the file will be placed in rows (horizontal) or collums (vertical)

For example:

r1,192.168.64.1,255.255.255.0,69

The imformation above is typed into "rows" starting at row 0. 
Example: r1 = row 0, 192.168.64.1 = row 1, 255.255.255.0 = row 2, etc. 

NOTE: There cannot be any spaces between commas and their values between the commas. If there is no information for a row but you need to add more information after that row, leave the space empty.
	Ex. r1,,255.255.255.0,69
	Let's say you for some reason, do not have an new ip address but you have information for a new subnet mask. You will leave the row 1 value blank but continue to the next rows. 


CONFIGURATION FILE EXPLANATION

The configuration builder file is a standard python file named "conf_builder.py". This will call upon the csv file that is holding our specific information and the template file directory that has our template.
The following is the configuration used by the conf_builder.py file. 

________________________________________________________________________________

import csv

from jinja2 import Environment, FileSystemLoader

#This will go to the Templates Directory where our router_template.j2 file is located
file_loader = FileSystemLoader('Templates')

#This loads the environment
env = Environment(loader=file_loader)

templateRT = env.get_template('router_template.j2')
#This will create a with statement for the IP_info_router.csv file

with open ("ip_info_router.csv") as f:
    csv_data=csv.reader(f)
    for row in csv_data: 
        csv_router_name = row[0]
        csv_ip_address = row[1]
        csv_subnet_mask = row[2]
        csv_router_ospf = row[3]
        csv_NTP_conf = row[4]
        
        #render unique data over template. The name of the items in the j2 file must match with the names below. 
        #for example, if you have a value for the hostname ( [[ router_name ]] ), you must use the same name below. 
        #So in this case, our csv_router_name will go with router_name since we used router_name in the j2 router template file.
        
        output = templateRT.render(router_name=csv_router_name, 
                                    ip_address=csv_ip_address, 
                                    subnet_mask=csv_subnet_mask, 
                                    router_ospf=csv_router_ospf)
    with open(csv_router_name + ".txt","w") as txtf:
        txtf.write(output)

#To print out this function, open terminal in visual studio and type "python3 *name of file*" (The file name will be conf_builder.py)
#I can print out the documents as txt files (txtf) 

________________________________________________________________________________






