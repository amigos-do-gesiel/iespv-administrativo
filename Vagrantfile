# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

    config.vm.define "web" do |web|
        web.vm.box = "ubuntu/trusty64"
        web.vm.network "forwarded_port", guest: 8000, host: 8000
        web.vm.synced_folder ".", "/vagrant"
        
        web.vm.provider "virtualbox" do |vb|
            vb.gui = false
            vb.memory = "512"
        end
       
        web.vm.provision "shell", inline: <<-SHELL
            sudo apt-get install -y python-pip python-dev libpq-dev postgresql postgresql-contrib
            sudo pip install django==1.9.8 flake8 psycopg2 django-bootstrap4 pytest pytest-django
        SHELL
    end

end
