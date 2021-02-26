ECHO OFF
GOTO START
:MENU
pause
:START
CLS
:START_NOCLS
SET M=''
SET ENV=D:\Documents\Py_env\NewLifeUtils env
SET CURRENT=%cd%
setlocal
call :setESC
ECHO %ESC%[40;92m+--------------------------------------+-------+
ECHO %ESC%[40;92m^| %ESC%[40;93mType number and press Enter          %ESC%[40;92m^|  %ESC%[40;95mUID  %ESC%[40;92m^|
ECHO %ESC%[40;92m+--------------------------------------+-------+
ECHO %ESC%[40;92m^| %ESC%[100;93m1%ESC%[40;92m   %ESC%[40;4;96mStart compile for PIPY%ESC%[40;24;92m           ^| %ESC%[40;95mCPIPY %ESC%[40;92m^|
ECHO %ESC%[40;92m^| %ESC%[100;93m2%ESC%[40;92m   %ESC%[40;4;96mPublish to real%ESC%[40;24;92m                  ^| %ESC%[40;95mPREAL %ESC%[40;92m^|
ECHO %ESC%[40;92m^| %ESC%[100;93m3%ESC%[40;92m   %ESC%[40;4;96mInstall   to   global%ESC%[40;24;92m            ^| %ESC%[40;95mINGLB %ESC%[40;92m^|
ECHO %ESC%[40;92m^| %ESC%[100;93m4%ESC%[40;92m   %ESC%[40;4;96mRun test from env%ESC%[40;24;92m                ^| %ESC%[40;95mRTEST %ESC%[40;92m^|
ECHO %ESC%[40;92m^| %ESC%[100;93m5%ESC%[40;92m   %ESC%[40;4;96mTesting mode%ESC%[40;24;92m                     ^| %ESC%[40;95mRTSTM %ESC%[40;92m^|
ECHO %ESC%[40;92m^| %ESC%[100;93m6%ESC%[40;92m   %ESC%[40;4;96mCreate cmd%ESC%[40;24;92m                       ^| %ESC%[40;95mCRCMD %ESC%[40;92m^|
ECHO %ESC%[40;92m^| %ESC%[100;93m7%ESC%[40;92m   %ESC%[40;4;96mInstall new env%ESC%[40;24;92m                  ^| %ESC%[40;95mINEWE %ESC%[40;92m^|
ECHO %ESC%[40;92m+--------------------------------------+-------+
ECHO %ESC%[40;92m^| %ESC%[40;93mPress enter without number to exit   %ESC%[40;92m        ^|
ECHO %ESC%[40;92m+----------------------------------------------+%ESC%[0m
SET /P M=%ESC%[40;94m^>^>^>%ESC%[0m
CLS
IF %M%==1 GOTO CPIPY
IF %M%==2 GOTO PREAL
IF %M%==3 GOTO INGLB
IF %M%==4 GOTO RTEST
IF %M%==5 GOTO RTSTM
IF %M%==7 GOTO CRCMD
IF %M%=='' GOTO EOF
GOTO INVALID
:CPIPY
ECHO STARTING CLEANUP ----------------------
RD "dist" /s /q
RD "build" /s /q
RD "NewLifeUtils.egg-info" /s /q
ECHO FINISHING CLEANUP ---------------------
ECHO STARTING COMPILE ----------------------
python setup.py sdist bdist_wheel
ECHO FINISHING CLEANUP ---------------------
GOTO MENU

:PREAL
twine upload --repository pypi dist/*
GOTO MENU

:INGLB
ECHO STARTING UNINSTALL --------------------
pip uninstall newlifeutils --yes
ECHO FINISHING UNINSTALL -------------------
ECHO STARTING INSTALL ----------------------
python setup.py install
ECHO FINISHING INSTALL ---------------------
GOTO MENU

:RTEST
"%ENV%\Scripts\python.exe" "%CURRENT%\test.py"
GOTO MENU

:RTSTM
"%ENV%\Scripts\python.exe" "%CURRENT%\test.py"
PAUSE
CLS
GOTO RTSTM

:CRCMD
cmd /k
GOTO MENU

:INEWE
virtualenv env
GOTO MENU

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
:INVALID
ECHO Invalid syntax!
GOTO START_NOCLS