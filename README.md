# quantcast_coding_task

The code was written in Python (.py) and convert into an executable file "most_active_cookie.exe" <br />
-Cookie_log.csv was given as a test file <br />
-To run: Download the .exe file and write in the commandline in the following format: <br />
./most_active_cookie [filename] -d [MM-DD-YYYY] <br />
<br />
Test example: <br />
<br />
./most_active_cookie cookie_log.csv -d 2018-12-09  
AtY0laUfhglK3lC7 <br />
<br />
./most_active_cookie cookie_log.csv -d 2018-12-08  
SAZuXPGUrfbcn5UA  <br />
4sMM2LxV07bPJzwf  <br />
fbcn5UAVanZf6UtG  <br />
<br />

-Invalid argument would result in error response, test: <br />
<br />
./most_active_cookie cookie_log.csv -d 2018-12 <br />
Error: Date Format: YYYY-MM-DD     <br />
<br />
./most_active_cookie <br />
Incorrect number of argument! <br />
<br />
./most_active_cookie cookie_log.csv  dsa 2018-12-08 <br />
-d UTC: Please enter the right timezone <br />
<br />
./most_active_cookie cookie_lov -d 2018-12-08  <br />
cookie_lov : No such file or directory <br />

