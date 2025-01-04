@echo off
for %%f in (*.assets) do python unity_ost.py "%%f"
echo Done!
pause
