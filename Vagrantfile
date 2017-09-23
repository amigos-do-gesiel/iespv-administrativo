# coding: utf-8
Vagrant.configure("2") do |config|
  config.vm.define "web" do |web|
    web.vm.box = "ubuntu/trusty64"
    web.vm.network "forwarded_port", guest: 8000, host: 8000
    web.vm.synced_folder ".", "/home/vagrant/"

    web.vm.provider "virtualbox" do |vb|
      vb.name = "dj"
      vb.memory = "512"
      vb.gui = false
    end

    #Add this requirements on shell for use postgres database: postgresql postgresql-contrib  
    web.vm.provision "shell", inline: <<-SHELL
        sudo apt-get install -y python-pip python-dev libpq-dev                                                                            
        sudo pip install -r requirements.txt
    SHELL
  end

end

