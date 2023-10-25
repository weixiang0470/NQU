# **Linux File System**
- Single tree structure 
- Only one highest node (root`/`)
- Everthing is file, ex: mouse is file, keyboard is file, terminal is file
- File and Directory are case sensitve(區分大小寫), `a.txt` and `A.txt` are different file
## **Linux System Directory**
### **/dev**
- 設備(device)，不管有形(mouse,keyboard)還是無形的設備(terminal)
- sda , sdb , ... , sdz , sdaa , sdab (SCSI hard disk)
    - sda1 , sda2 means partition of sda
- bd (ide hard disk)
- lp (printer)
- pts/0 , pts/1 ,pts/2
### **/bin**
- Binary 二進制檔(執行檔), Normal user's tools program
- `vim`,`w`
### **/sbin**
- Superuser Binary, root user's tools program
- `useradd`,`yum`
### **/home**
- home directory for all user, ex: jack, user, marry...
### **/usr**
- Unix resources
- Third party resources/packages(library(/lib),執行檔executable file(/bin),...)
### **/var**
- Variable file (可變動的檔案)
- Log file (who access,when,where,...)
- Web server's home directory, `/var/www/html`
- Email
### **/lib64**
- Linux's library(Linux 函式庫), 64 bits
- `[lib][library_name][.so/.a].[version]`
- `.so` 動態函式庫
- `.a` 靜態函式庫
- 靜態函式庫
    - 編譯時會將靜態函式庫編譯進去
	- 編譯出來檔案較大
    - 執行時只需執行檔無需靜態函式庫
- 動態函式庫
    - 編譯時不會將動態函式庫編譯進去
	- 編譯出來檔案較小
	- 執行時需要執行檔和動態函式庫
	- 執行時才去函式庫執行
### **/etc**
- System setting, ex: IP address, Domain name server, user's account, user's password
- 系統配置檔, 伺服器配置檔
- Only root user can access
- `resolv.conf` , system's server file, ex: dns server
- `inittab`, 開機時進入單人模式or圖形化模式
### **/boot**
- 系統核心(kernel)
- 關於開機時將kernel載入進記憶體所使用的kernel檔
### **/root**
- root's home directory(管理者的家目錄)
### **/tmp**
- temporary file
- Everyone can access(read and write) to this file
### **/mnt**
- Mount(掛載), for USB drive, Hard drive
- When USB drive connected to linux, it will identify as `sdb` and mapping under `/mnt`, any operation in `/mnt/sdb` will reflex on USB drive
### **/media**
- Mount (掛載), for DVD, CDROM
### **/proc**
- Process , a running program called process
- Process's information


## **Extra**
- 不同的分割區就有不同的檔案系統,有不同的特色
    - Windows
        - FAT16, for 16 bits OS
		- FAT32, for 32 bits OS ,5bg 存不起來, suitable for small file
		- EXFAT, 5gb ok, suitable for large file
        - NTFS, 5gb ok, suitable for large file
    - File system for saving "video" needs large capacity
    - File system for saving "text" like Dcard, needs many partition but each division can be small capacity
