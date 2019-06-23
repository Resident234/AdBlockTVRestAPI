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

3) Set port forwarding in router settings https://prnt.sc/o5jlyk (more details https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/)

4) Install Dynamic Update Client (see more https://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/)

5) Find out your public ip here https://2ip.ru/ 




A stackoverflow question that helped https://stackoverflow.com/questions/36597643/flask-server-not-visible-from-my-public-ip-address