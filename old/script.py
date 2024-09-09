from proxmoxer import ProxmoxAPI

# Connect to Proxmox
proxmox = ProxmoxAPI('81.230.229.37', user='root@pam', password='1234a', verify_ssl=False)

# Create an LXC container
proxmox.nodes('proxmox_node').lxc.create(vmid=300, ostemplate='local:vztmpl/ubuntu-22.04-standard_22.04-1_amd64.tar.zst', storage='local-lvm', hostname='web-server', memory=4096, cores=2, net0='name=eth0,bridge=vmbr0,ip=dhcp')
