Requirement
- VMware Fusion 13

Step 1
- Download Windows 11 at [Windows Insider Preview Downloads](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewARM64)
    - Need register to Windows Insider 

Step 2
- Download Homebrew with the command below run on terminal:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Step 3
- Install qemu
```
brew install qemu
```
- Convert VHDX to vmdk through `qemu-img`
    - `qemu-img convert -O vmdk input_VHDK_file output_file.vmdk -p`
    - ex : `qemu-img convert -O vmdk /Users/wongweixiang/Downloads/Windows11_InsiderPreview_Client_ARM64_en-us_22598.VHDX ~/Desktop/windows11.vmdk -p`

Step 4
- Open VMware Fusion and create new VM
- ![vm01](Img/mac_win/vm01.png)
- ![vm02](Img/mac_win/vm02.png)
- ![vm03](Img/mac_win/vm03.png)
- ![vm04](Img/mac_win/vm04.png)
- ![vm05](Img/mac_win/vm05.png)

Step 5
- Start VM and when see this 
    - ![win01](Img/mac_win/win01.png)
- Press `fn + Shift + f10` , will show this
    - ![win02](Img/mac_win/win02.png)
    - ![win03](Img/mac_win/win03.png)

Step 6
- `oobe\bypassnro`
    - To have the choice **I don't have internet**
    - ![oobe\bypassnro](Img/mac_win/oobe_bypassnro.png)
- And now just start install windows 11 normally

Step 7
- Reinstall VMware tool, to have internet and others service
1. Open powershell
    - ![powershell01](Img/mac_win/powershell01.png)
2. `Set-ExecutionPolicy RemoteSigned`
    - ![powershell02](Img/mac_win/powershell02.png)
3. Reinstall VMware tools
    - ![win04](Img/mac_win/win04.png)
4. Run setup with powershell
    - ![win05](Img/mac_win/win05.png)
5. After that we have Internet!
    - ![win06](Img/mac_win/win06.png)
6. Resolution of Windows11, set this up we will have a full screen of windows 11
    - ![win07](Img/mac_win/win07.png)


Done


_**[Reference](https://www.youtube.com/watch?v=srOty2jflF4)**_