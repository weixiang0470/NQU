# **Host Only Network Mode**
- If don't have choice at **Host only**
    - `File` -> `Tools` -> `Network Manager` -> `Create`

# **Change `SELINUX` from `enforcing` to `disabled`**
## **Step 1**
- Key in `gedit /etc/selinux/config` in terminal

![etc_selinux_config](Images/W2Note1.png)

## **Step 2**
- From picture above change `enforcing` to `disabled`
- Save and exit

## **Step 3**
- Key in `getenforce` in terminal, if reply `Disabled` then done!

# **Closing Firewall**
## **Step 1**
- `systemctl status firewalld`
    - To check the status of firewall
## **Step 2**
- `systemctl stop firewalld`
    - To inactive/stop firewall

![Status_Firewalld](Images/W2Note2.png)
- **enabled** means will auto start/active when machine start

## **Step 3**
- `systemctl disable firewalld`
    - To **disable** firewall, will not open/active firewall _automatically_

![disabled_Firewall](Images/W2Note2.1.png)

# **SSH server**
## **Step 1**
- `sudo yum install -y openssh-server`
    - To install **ssh server**,`-y` set yes/y to all response
- `ifconfig`
    - To check ip address of the VM
    ![checking_ip_address_of_VM](Images/W2_ssh1.png)
    - `192.168.64.2` is the ip address that we need

## **Step 2**
- `ping 192.168.64.2`
    - Open terminal at host machine and ping the ip address of VM
    - ![Ping_VM_from_Host](Images/W2_ssh2.png)

## **Step 3**
- `systemctl status sshd`
    - To check the status of ssh server, if it is inactive then use command below to start ssh server
    - ![Check_ssh_Status](Images/W2_ssh3.png)
- `systemctl start sshd`
    - To start ssh server, if success then move to the last step
    - ![Check_again](Images/W2_ssh4.png)

## **Step 4**
### **Mac version**
- `ssh user@192.168.64.2`
    - Open terminal at host machine and connect with the command above.
    - `user` is the username of the VM
    - `192.168.64.2` is the ip address of the VM at **Step 1**
    - ![Connect_ssh](Images/W2_ssh5.png)
    - And done!!!
### **Windows version**
- Use APP like **Putty** and connect with ssh server which is **22 port**

## **Extra**
- Now you can also use SFTP software/server to transfer file into the VM!

# **Web server**
## **Step 1**
- `sudo yum install httpd -y`
    - To install http server
    - ![install_httpd](Images/W2_http1.png)
- `systemctl status httpd`
    - ![checking_httpd_status](Images/W2_http2.png)
- `ifconfig`
    - To check ip address, `192.168.64.2` is mine VM ip address

## **Step 2**
- `cd /var/www/html`
    - Change directory into httpd server directory
- `echo "Hello test Http server" > test.htm`
    - _Need super user permission_ , add `sudo` infront or user `su` to become root user
    - Creating a htm file call `test.htm` and content is `Hello test Http server`
    - ![Create_file](images/W2_http3.png)

## **Step 3**
- `systemctl start httpd`
    - ![Start_and_check_httpd_status](Images/W2_http4.png)

## **Step 4**
- `192.168.64.2/test.htm`
    - Open browser in host machine and type in the command above
    - `192.168.64.2` is the ip address of VM
    - `test.htm` is the file name under `/var/www/html` directory
    - ![Browser_Pic](Images/W2_http5.png)