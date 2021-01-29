ECHO OFF
GOTO START
:MENU
pause
:START
CLS
SET M=''
ECHO +--------------------------------------+-------+
ECHO + Type number and press Enter          +  UID  +
ECHO +--------------------------------------+-------+
ECHO + 1 - Start compile for PIPY           + CPIPY +
ECHO + 2 - Start compile for Tests          + CTEST +
ECHO + 3 - Publish to real                  + PREAL +
ECHO + 4 - Publish to test                  + PTEST +
ECHO + 5 - Install   to   global            + INGLB +
ECHO +   - Uninstall from global            + UNGLB +
ECHO + 7 - Install   to   env               + INENV +
ECHO + 8 - Uninstall from env               + UNENV +
ECHO + 9 - Run test from env                + RTEST +
ECHO + 0 - Create cmd                       + CRCMD +
ECHO + - - Install new env                  + INEWE +
ECHO +--------------------------------------+-------+
ECHO + Press enter without number to exit   +       +
ECHO +--------------------------------------+-------+
SET /P M=Type 1, 2, 3, or 4 then press ENTER:
CLS
IF %M%==1 GOTO CPIPY
IF %M%==2 GOTO CTEST
IF %M%==3 GOTO PREAL
IF %M%==4 GOTO PTEST
IF %M%==5 GOTO INGLB
IF %M%==7 GOTO INENV
IF %M%==8 GOTO UNENV
IF %M%==9 GOTO RTEST
IF %M%==0 GOTO CRCMD
IF %M%==- GOTO INEWE
IF %M%=='' GOTO EOF
GOTO MENU
:CPIPY
ECHO STARTING CLEAR ----------------------
RD dist /s /q
RD build /s /q
RD "NewLifeUtils.egg-info" /s /q
ECHO FINISHING CLEAR ---------------------
python setup.py sdist bdist_wheel
GOTO MENU
:CTEST
python setup.py sdist
GOTO MENU
:PREAL
twine upload --repository pypi dist/*
GOTO MENU
:PTEST
twine upload --repository testpypi dist/*
GOTO MENU
:INGLB
pip uninstall newlifeutils --yes
ECHO FINISHING UNINSTALL -----------------
python setup.py install
GOTO MENU
:INENV
env\Scripts\python setup.py install --upgrade
GOTO MENU
:RTEST
env\Scripts\python test.py
GOTO MENU
:CRCMD
cmd /k
GOTO MENU
:INEWE
virtualenv env
GOTO MENU