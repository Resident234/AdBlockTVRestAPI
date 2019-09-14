A simple flask app using vagrant. 

You need : 
 * Vagrant 
 * Virtualbox ( I am using vagrant with virtualbox)
 * Git (to clone this repo)

NOTE : You need to execute the takeover.sh from inside the created vagrant vm to make this server work. In this way the server will update itself upon code change. 

- Step 1 -
 
-- Clone this repo and cd into it .
 ```
git clone https://github.com/Frewx/vagrantFlaskProject.git && cd vagrantFlaskProject
```
- Step 2 - 
```
vagrant up
```
-- After you've done this (it will take some time) you need to connect to the machine.

- Step 3 - 
```
 vagrant ssh   to connect to the vm. From here we will execute a shell script.
```
- Step 4 -

-- cd into the /vagrant directory which we keep everyting about this vm.(This is where the script lies.)
```
 cd /vagrant
```
-- Execute the takeover.sh:
```
 ./takeover.sh 
```
This script will arrange everything and your web server will be up in no time. 
We are doing this because we want web server to change upon code changes.(Mentioned above)
If we don't do this then our server will not be changing upon code change.

If you did everything in this order then your web server will be running on your host machine at ```localhost:5000```



Set Flask server visible from public ip address (tested in ubuntu 18): 

1) Switch To Static IP Address https://websiteforstudents.com/switch-static-ip-address-ubuntu-17-04-17-10/

2) Set dynamic dns in router settings https://prnt.sc/o5jnxp

3) Set port forwarding in router settings https://prnt.sc/oz9xvz (more details https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/)

4) Install Dynamic Update Client (see more https://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/)

5) Find out your public ip here https://2ip.ru/ 




A stackoverflow question that helped https://stackoverflow.com/questions/36597643/flask-server-not-visible-from-my-public-ip-address



DB

To connect to instance using SSH:
ssh -i /home/gsu/Downloads/dejavu.pem ec2-user@ec2-3-16-131-11.us-east-2.compute.amazonaws.com

https://prnt.sc/p4dexy 

http://ec2-3-16-131-11.us-east-2.compute.amazonaws.com/phpinfo.php

http://ec2-3-16-131-11.us-east-2.compute.amazonaws.com/phpMyAdmin/


# ec2-3-16-131-11.us-east-2.compute.amazonaws.com db connection config :
# login : root
# password : Po8WuX?v0B9inO6UMOpr


mysql -u root -pPo8WuX?v0B9inO6UMOpr
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY ‘Po8WuX?v0B9inO6UMOpr’;
FLUSH PRIVILEGES;
exit

1. Add MySQL to inbound rules.
Go to security group of your ec2 instance -> edit inbound rules -> add new rule -> choose MySQL/Aurora and source to Anywhere.


2. Add bind-address = 0.0.0.0 to my.cnf
In instance console:

sudo vi /etc/my.cnf
this will open vi editor.
in my.cnf file, after [mysqld] add new line and write this:

bind-address = 0.0.0.0
Save file by entering :wq(enter)

now restart MySQL:
sudo systemctl restart mariadb
sudo chkconfig mariadb on

3. Create a remote user and grant privileges.
login to MySQL:

mysql -u root -pPo8WuX?v0B9inO6UMOpr

Now write following commands:

GRANT ALL PRIVILEGES ON *.* to root@localhost IDENTIFIED BY 'Po8WuX?v0B9inO6UMOpr' WITH GRANT OPTION;

GRANT ALL PRIVILEGES ON *.* to root@'%' IDENTIFIED BY 'Po8WuX?v0B9inO6UMOpr' WITH GRANT OPTION;

FLUSH PRIVILEGES;

EXIT;

After this, MySQL dB can be remotely accessed by entering public dns/ip of your instance as MySQL Host Address, username as root and password as Po8WuX?v0B9inO6UMOpr;. (Port is set to default at 3306)



Run command on server with flask :

setsebool -P httpd_can_network_connect_db=1
sudo apt-get install mysql-server
mysql -u root -h 3.16.131.11 -p