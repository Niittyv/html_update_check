# html_update_check
This script checks whether a remote webpage has changed since last visit and the content that has changed.

Name the html-file from your previous webpage visit "base.html". The script will fetch the current version of the destination webpage using Firefox and will compare it to base.html.

Change the url in pw.py file to your destination webpage url.

The comparison result will be written into txt-file.

First run < python pw.py > and after that run < python compare.py "base.html" "remote.html" >. Alternatively just double click run.cmd file on a Windows machine.



