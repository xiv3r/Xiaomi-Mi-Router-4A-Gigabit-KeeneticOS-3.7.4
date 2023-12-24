
@Echo off
 
:m1
Echo 1 - Connect to router
Echo 2 - Read eeprom.bin
Echo 3 - Read  backup.bin
Echo 4 - Write breed.bin for 4ag/3Gv2


 
echo.
Set /p choice="Select: "
if not defined choice goto m1
if "%choice%"=="1" (1.start_main.bat)
if "%choice%"=="2" (2.start_create_backup_eeprom.bat)
if "%choice%"=="3" (3.start_create_backup.bat)
if "%choice%"=="4" (4.start_write_uboot_Breed.bat)




Echo.
Echo 
Echo.
Echo.
goto m1
pause >nul