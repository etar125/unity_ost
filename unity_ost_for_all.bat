@echo off
for %%i in (*.assets) do  set files=!files! "%%i"
python unity_ost.py %files%
echo Done!
pause
