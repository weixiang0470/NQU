# **Midterm**
- seq 
- tr

# **Final**
1. 無密碼遠端登錄
2. `scp source destination` (遠端拷貝)
3. `rpm -qa | grep httpd`
4. nfs
5. `dd if=/dev/zero of=filename bs=1M count=100`
6. samba

# **Using Network**
- Prestep : Check device, ip address, and gateway
    - ![prestep](Img/W11/prestep.png)
    - Device : **ens160**
    - Ip address : **172.20.10.3**
    - Gateway : **172.20.10.1**
1. `systemctl disable NetworkManager.service` : Not neccesary
2. `systemctl stop NetworkManager.service`
    - 網路標籤會不見
    - ![Stop_NetworkManager](Img/W11/Stop_NetworkManager.png)
3. `cd /etc/sysconfig/network-scripts`
    - `vim ifcfg-ens160` : In my case is **ens160** and edit file
    - DEVICE , IPADDR , GATEWAY need to check before stop **NetworkManager**
```
TYPE=Ethernet
DEVICE=ens160
ONBOOT=yes
BOOTPROTO=static
IPADDR=172.20.10.3
NETMASK=255.255.255.0
GATEWAY=172.20.10.1
```
4. `systemctl start network.service`
    - `systemctl status network.service` : Will show active
    - `yum install -y network-scripts` : CentOs8 need to install manually
    - Add **HWADDR=MAC_Address** into **ifcfg-ens160** (check before stop NetworkManager) if `systemctl start network` failed

5. `systemctl restart network.service`
    - `ping 8.8.8.8` : If success will be able to ping 8.8.8.8

![network_done](Img/W11/network_done.png)