# udacity
udacity projects

Installation Preparation

This program requires a number of things installed for it to run properly. Install the following:

Python 2.7 [http://docs.python-guide.org/en/latest/starting/installation/][http://docs.python-guide.org/en/latest/starting/installation/]

Vagrant [https://www.vagrantup.com/][https://www.vagrantup.com/]

VirtualBox [https://www.virtualbox.org/][https://www.virtualbox.org/] installed.



Running program

-- open terminal
--change directory to vagrant
cd /vagrant

Press enter and then type:

--powers up vagrant
vagrant up

--logs into vagrant
vagrant ssh

Once the processes are complete, navigate to the tournament directory:

-- change directory to tournament folder
cd /vagrant/tournament

Then type the following to create the database tables necessary for the program to run.

--launch psql interface and reads sql file
psql -f tournament.sql
 
Finally, execute the following to run the test Python file:

-- run project
python tournament_test.py
