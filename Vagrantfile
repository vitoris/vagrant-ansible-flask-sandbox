Vagrant.configure("2") do |config|

  config.vm.hostname = "lb"
  config.vm.define "nginx" do |lb|
    lb.vm.box = "ubuntu/bionic64"
    lb.vm.network :private_network, ip: "10.2.2.25"
    lb.ssh.insert_key = false
    lb.ssh.shell = "bash"
    lb.vm.provision :ansible do |ansible|
      ansible.playbook = "playbook-lb.yml"
      ansible.verbose = 'vv'
    end
  end

  config.vm.hostname = "server1"
  config.vm.define "server1" do |app1|
    app1.vm.box = "ubuntu/bionic64"
    app1.vm.network :private_network, ip: "10.2.2.26"
    app1.ssh.insert_key = false
    app1.ssh.shell = "bash"
    app1.vm.provision :ansible do |ansible|
      ansible.playbook = "playbook-server.yml"
      ansible.verbose = 'vv'
    end
  end

  config.vm.hostname = "server2"
  config.vm.define "server2" do |app2|
    app2.vm.box = "ubuntu/bionic64"
    app2.vm.network :private_network, ip: "10.2.2.27"
    app2.ssh.insert_key = false
    app2.ssh.shell = "bash"
    app2.vm.provision :ansible do |ansible|
      ansible.playbook = "playbook-server.yml"
      ansible.verbose = 'vv'
    end
  end

end
