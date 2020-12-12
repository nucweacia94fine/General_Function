@echo off
echo 正在清除C槽垃圾文件，請稍等......

del /f /s /q %windir%\Temp\
rd /s /q %windir%\Temp\
md %windir%\Temp

del /f /s /q %windir%\prefetch\*.*
rd /s /q %windir%\prefetch\
md %windir%\prefetch

del /f /s /q "%userprofile%\Local Settings\Temp\*.*"
rd /s /q "%userprofile%\Local Settings\Temp\" 
md "%userprofile%\Local Settings\Temp"

del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*"
rd /s /q "%userprofile%\Local Settings\Temporary Internet Files\"
md "%userprofile%\Local Settings\Temporary Internet Files"

del /f /s /q "%userprofile%\Local Settings\Google\Chrome\User Data\Default\File System\*.*"
rd /s /q "%userprofile%\Local Settings\Google\Chrome\User Data\Default\File System\"
md "%userprofile%\Local Settings\Google\Chrome\User Data\Default\File System"


del /f /s /q "c:\Windows\SoftwareDistribution\DataStore\*.*"
rd /s /q "c:\Windows\SoftwareDistribution\DataStore\"
md "c:\Windows\SoftwareDistribution\DataStore\"

del /f /s /q "c:\Windows\SoftwareDistribution\Download\*.*"
rd /s /q "c:\Windows\SoftwareDistribution\Download\"
md "c:\Windows\SoftwareDistribution\Download\"

del /f /s /q %systemdrive%\*.tmp
del /f /s /q %systemdrive%\*._mp
del /f /s /q %systemdrive%\*.log
del /f /s /q %systemdrive%\*.gid
del /f /s /q %systemdrive%\*.chk
del /f /s /q %systemdrive%\*.old
del /f /s /q %windir%\*.bak


echo 清除系統垃圾完成！
echo. & pause