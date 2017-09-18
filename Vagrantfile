# coding: utf-8
Vagrant.configure("2") do |config|

  config.vm.define "db" do |db|
    db.vm.box = "ubuntu/trusty64"
    db.vm.network "forwarded_port", guest: 5432, host: 5432
    db.vm.network "public_network", ip: "192.168.1.11"
    db.vm.synced_folder ".", "/home/vagrant/"

    db.vm.provider "virtualbox" do |vb|
      vb.name = "dj-database"
      vb.memory = "512"
      vb.gui = false
    end

    db.vm.provision "shell", inline: <<-SHELL
                                                                        sudo apt-get install -y postgresql
                                                                                    sudo su - postgres -c "psql -f /vagrant/db-config.sql"
                                                                                                sudo su - postgres -c 'echo "host all all 192.168.1.10/24 trust" >> /etc/postgresql/9.3/main/pg_hba.conf'
                                                                                                            sudo su - postgres -c "echo listen_addresses=\\'*\\' >> /etc/postgresql/9.3/main/postgresql.conf"
                                                                                                                        sudo service postgresql restart
        SHELL
  end

  config.vm.define "web" do |web|
    web.vm.box = "ubuntu/trusty64"
    web.vm.network "forwarded_port", guest: 8000, host: 8000
    web.vm.network "public_network", ip: "​ 192.168.1.10"
    web.vm.synced_folder ".", "/home/vagrant/"

    web.vm.provider "virtualbox" do |vb|
      vb.name = "dj"
      vb.memory = "512"
      vb.gui = false
    end

    web.vm.provision "shell", inline: <<-SHELL
                                                                            sudo apt-get install -y python-pip python-dev libpq-dev postgresql postgresql-contrib
                                                                                      
            sudo pip install django==1.9.8 flake8 psycopg2 django-bootstrap4 pytest pytest-django pytest-cov factory_boy unipath 
        SHELL
  end

end
