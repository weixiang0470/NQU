# pwd
- Print Work Directory
- To show current working directory

# ls
- list all file/directory
- `ls -l`
    - `drwxr-xr-x`
        - `d` : directory, if first is `-` then is file, if `b` then is block device(hard disk, USB), if `c` then is char device(字元設備,mouse,keyboard,terminal), if `l` then is link
    - `----------`
        - First `-` is show above
        - Owner(3 bits),Group(3 bits),Other(3 bits)
        - `r` : read
        - `w` : write and delete
        - `x` : executable
- `ls -l test` (test is directory)
    - `ls -l test` : Will only show the total file/directory of **test**
    - `ls -l -d test` : Will give the information of the **test** directory
- `ls -l -h`
    - File size will show in k, M, GB
- `ls -a`
    - Show hidden file

# cp
- Copy files and directories
- `cp [source] [destination]`
    - `cp aa /tmp` : copy file **aa** to **/tmp**
- `-r` : recursive(for directory) , `-f` : force , `-i` : query

# mv
- move (rename) files
- change file/directory's name
- move file/directory
- `-r` : recursive(for directory) , `-f` : force , `-i` : query

# cd
- Change directory
- `cd /tmp` : change to `/tmp` directory
- `cd ~` : change to home directory
- `cd -` : change back to last directory

# sudo
- Change to super user(admin) when executing the current command, after the command done will change back to normal user

# su
- Change to super user permanently, use `exit` change back to normal user

# apt
- For installation, use at **Ubuntu** and **Debian** series

# yum
- For installation, use at **Redhat**/**Fedora**/**Centos** series
- `yum install software_package`
    - To install software
- `yum remove software_package`
    - To remove software

# kill
- To terminate process
- `kill -9 4740`
    - `-9` : force kill
    - `4740` : pid, process id

# gedit
- Graphical text editor
- `gedit a.txt`
    - Open a.txt by graphical text editor

# systemctl
- `status` : to check current status, ex : `systemctl status firewalld` means check firewall is active or inactive
- `stop` : To disabled server
- `start` : To enable server
- `reload` 
- `restart`

# echo
- `echo hi` : Terminal will reply "hi"
- `echi "hi" > a.txt` : Will create a.txt file with content "hi", if a.txt exists then will rewrite a.txt with "hi"
- `>>` : 追加
    - `echo 123 >> a.txt` : Will add 123 into the last row of a.txt instead of replace it
- `echo $?`
    - `$?` : Last command success or not?
    - 0 : success
    - Others : having issue


# ./
- To confirm is this directory 
- `./hello` : Execute `hello` file, if `hello` is executable

# cat
- Will show contents at terminal, ex : `cat a.txt` , will show contents in a.txt at terminal
- `cat -n a.txt` : Will show with row indicated
    - ![cat-n](Images/cat-n.png)
- `cat <<EOF > b.txt`
    - `Helloworld`
    - `Test`
    - `EOF` (end)
        - Will create b.txt(if not exist) with content "Helloworld" and "Test"
        - `<<EOF` : Next `EOF` will end 
- `cat a.txt b.txt > c.txt`
    - Mix a.txt and b.txt into c.txt

# more
- Only go to next page
- Will have more information

# less
- Can go last page and next page

# head
- `head -n 3 a.txt`
    - Print out first 3 row of a.txt

# tail
- `tail -n 5 a.txt`
    - Print out last 5 row of a.txt
- `tail -f /tmp/a.txt`
    - `-f` : Keep follow (listen)

# stat
- Display file's status
- `stat a.txt` : Will show status(time information) of a.txt

# man
- Manual
- `man ls` : Show the manual for `ls`
- After enter manual, use `/-h` and enter will go to the **-h** place

# whatis
- Ask programming's API
- `whatis open`
	- open (2)  - describe 
    - `man 2 open` will give more specific manual of the specific "open"

# halt
- `halt -p` : pause
- Others similar command : `shutdown` , `poweroff`

# touch
- Can use to **create new empty file** and **renew file's timestamp**

# chmod
- Change permission of file, change file mode bits
- `chmod -x aaa.txt`
    - Give aaa.txt executable permission

# uname
- Print system information
- `uname -r` : Show system kernel version
- `uname -a` : Show complete information (system)

# hostname
- Show hostname 
- `hostnamectl set-hostname Jack` : change hostname to "Jack"

# whoami
- To know is which user(root/jack/user/...), print effective userid

# w
- Show who is logged on and what they are doing
- pts/0 : terminal at vm
- `echo "hi" > /dev/pts/2`
    - Show "hi" on pts/2 terminal

# jobs
- Show all job
- `fg 2` : continue job 2

# passwd
- Change new password for current user
- `passwd tom` : Change password for tom

# netstat
- `netstat -tunlp | grep 80`
    - `t` : tcp
	- `u` : udp
	- `l` : listen 狀態
	- `p` : process
	- `n` : 不解析
    - `grep 80` : filter if have "80" 

# exit
- Exit root user to normal user

# pstree
- Show process list
# dmesg 
- Dump message

# Extra
## enp0s3
- NIC for connect to Internet
## enp0s8
- NIC in Virtual box, for host only adapter
## **$ and #**
- `$` : Signal indicate normal user
- `#` : Signal indicate root user

## . and ..
- `.` : Current directory
- `..` : Last directory(上一層目錄)