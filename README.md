A simple flask app using vagrant. 

You need : 
 * Vagrant 
 * Virtualbox ( I am using vagrant with virtualbox)
 * Git (to clone this repo)

NOTE : You need to execute the takeover.sh from inside the created vagrant vm to make this server work. In this way the server will update itself upon code change. 

- Step 1 -
 
-- Clone this repo and cd into it .
 
git clone https://github.com/Frewx/vagrantFlaskProject.git && cd vagrantFlaskProject

- Step 2 - 

vagrant up

-- After you've done this (it will take some time) you need to connect to the machine.

- Step 3 - 

 vagrant ssh   to connect to the vm. From here we will execute a shell script.

- Step 4 -

-- cd into the /vagrant directory which we keep everyting about this vm.(This is where the script lies.)

 cd /vagrant

-- Execute the takeover.sh:

 ./takeover.sh 

This script will arrange everything and your web server will be up in no time. 
We are doing this because we want web server to change upon code changes.(Mentioned above)
If we don't do this then our server will not be changing upon code change.

If you did everything in this order then your web server will be running on your host machine at localhost:5000

