Vagrant.configure("2") do |config|

  config.vm.define "nginx" do |lb|
    lb.vm.hostname = "loadbalancer"
    lb.vm.box = "ubuntu/bionic64"
    lb.vm.network :private_network, ip: "10.2.2.25"
    lb.ssh.insert_key = false
    lb.ssh.shell = "bash"
    lb.vm.provision :ansible do |ansible|
      ansible.playbook = "playbook-lb.yml"
      ansible.verbose = 'vv'
    end
  end

  N = 2
(1..N).each do |machine_id|
  config.vm.define "server#{machine_id}" do |machine|
    machine.vm.hostname = "srv#{machine_id}"
    machine.vm.network "private_network", ip: "10.2.2.#{25+machine_id}"
    machine.vm.box = "ubuntu/bionic64"
    machine.ssh.insert_key = false
    machine.ssh.shell = "bash"
    machine.vm.provision :ansible do |ansible|
      ansible.playbook = "playbook-server.yml"
      ansible.verbose = 'vv'
    end
  end
end
end
