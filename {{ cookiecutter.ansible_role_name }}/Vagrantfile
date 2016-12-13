# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

# Require 'yaml' module
require 'yaml'

# Read YAML file with VMs details
vagrant_config = YAML.load_file('./vagrant_config.yml')

# VMs management
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  vagrant_config['vagrant_servers'].each do |server|

    # Define Server seetings
    config.vm.synced_folder ".", "/vagrant", type: vagrant_config['vagrant_synced_folder_type']
    config.vm.define server['name'] do |vm_config|

      # Port forwarding management
      (server['forwarded_port'] ||= []).each do |port_config|
        vm_config.vm.network "forwarded_port", guest: port_config['guest'], host: port_config['host']
      end

      # Set proper box and hostname
      vm_config.vm.box = server['box']
      vm_config.vm.hostname = server['name']


      # Virtualbox vm name management
      vm_config.vm.provider vagrant_config['vagrant_provider'] do |vm|
          vm.name = server['name']
          vm.memory = server['memory'] ||= 512
          vm.cpus = server['cpus'] ||= 1
      end


      # Install python 2.7 if not present (On Xenial)
      vm_config.vm.provision 'shell' do |sh|

        # Debian family
        if (server['family'] == 'debian')
          sh.inline = '! type -P python2.7 \
                       && (sudo apt-get update \
                       && sudo apt-get install python2.7 -y) || true'
        elsif (server['family'] == 'redhat')
          sh.inline = '! type -P python2.7 \
                       && sudo yum install python2.7 -y || true'
        end
      end


      # Create vm public key
      vm_config.vm.provision 'shell' do |sh|
        sh.inline = "ssh-keygen -y -f /vagrant/.vagrant/machines/#{server['name']}/#{vagrant_config['vagrant_provider']}/private_key > /vagrant/.vagrant/machines/#{server['name']}/#{vagrant_config['vagrant_provider']}/public_key"
      end

      # Run provisionners
      vagrant_config['ansible_playbooks'].each do |playbook|

        # Run Ansible provisioning
        vm_config.vm.provision 'ansible' do |ansible|
          ansible.playbook = playbook
          ansible.galaxy_roles_path = '../'
          # Enable requirement if role has dependencies
          # ansible.galaxy_role_file = './requirements.yml'
          ansible.extra_vars = {
            ansible_python_interpreter: '/usr/bin/env python2.7'
          }
          ansible.groups = vagrant_config['ansible_groups']
        end
      end

    end
  end
end
