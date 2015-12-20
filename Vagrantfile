# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"
RVM_KEY = "409B6B1796C275462A1703113804BB82D39DC0E3"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  # Update system and install requirements
  config.vm.provision "shell" do |sh|
    sh.inline = "sudo apt-get update \
                  && sudo apt-get install python-pip python-dev curl -y \
                  && sudo pip install pytest-cookies"
  end

  # Install ruby and gems
  config.vm.provision "shell" do |sh|
    sh.inline = "gpg --keyserver hkp://keys.gnupg.net --recv-keys #{RVM_KEY} \
                  && curl -L https://get.rvm.io | bash -s stable \
                  && source ~/.rvm/scripts/rvm \
                  && rvm install ruby \
                  && gem install bundle \
                  && gem install byebug"
    sh.privileged = false
  end

  # Run pytest tests
  config.vm.provision "shell" do |sh|
    sh.inline = "cd /vagrant && py.test -v"
    sh.privileged = false
  end

end

