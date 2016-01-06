# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

# Managed boxes for this role (should have all platform and version defined in
# meta/main.yml)
VMS = {
  :trusty => {
    :box => "ubuntu/trusty64"
  }
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  VMS.each_pair do |name, options|

    config.vm.define name do |vm_config|

      # Set proper box
      vm_config.vm.box = options[:box]
  
      # Update system and install requirements
      vm_config.vm.provision "shell" do |sh|
        sh.inline = "sudo apt-get update \
                      && sudo apt-get install python-pip curl -y \
                      && sudo pip install ansible pytest"
      end
  
      # Run pytest tests for filter plugins
      vm_config.vm.provision "shell" do |sh|
        sh.inline = "cd /vagrant \
                      && rm -f tests/__pycache__/*.pyc \
                      && py.test -v"
        sh.privileged = false
      end
  
      # Run Ansible provisioning
      vm_config.vm.provision "ansible" do |ansible|
        ansible.playbook  = "tests/test_vagrant.yml"
      end
  
      # Run Serverspec tests
      vm_config.vm.provision "serverspec" do |serverspec|
        serverspec.pattern = 'spec/*_spec.rb'
      end

    end
  end
end

