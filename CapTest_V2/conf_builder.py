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




