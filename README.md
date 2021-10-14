# interval_process_ender_py

This tool allows you to automatically end or constantly restart a certain process (on Windows PC's) repeatedly within a specific, user-defined interval.

It's a very niche use tool, imagine a scenario like this: some program/process has a memory leak, and the vendor doesn't fix it in a timely manner.. so you'd rather restart it silently ever now and then before it builds up a huge memory usage. This tool is a result of my personal need for this, when dwm.exe was leaking memory on a Windows Insider preview build (causing regular crashes of games) and I couldn't rollback, so it saved my life. Who knows it can still help others in various scenario's, so i will publish it after all.

Of course, this tool can also be used for programs that spawn obnoxious processes which you don't want to have running in the background (so you'd set a really low scan interval, and make it end the process automatically every few seconds or so). Or even less likely, and not advisable - you want to frustrate the proper working of process(es) from something like a virus, before you can clean it out properly/need to deal with an intrusive program you can't have any processes running for while uninstalling it ('in use' errors and that it attempts to restart itself instantly), and with this tool you no longer need to go to Windows safe mode for it.



#### Below are the usage instructions. For convenience, it's advised to put it inside a .bat file (entire script command line, like below examples) and doubleclick that .bat file to enable the autorestart / auto shutdown scanner indefinitely.

## Usage syntax:
python auto_process_ender.py -pname [process].exe -interval [milliseconds] --restart

## Example with restart:
python auto_process_ender.py -pname dwm.exe -interval 5000 --restart
