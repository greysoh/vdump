```
                                                               
                                                                 
              ,---,                           ____               
            .'  .' `\                       ,'  , `.,-.----.     
          ,---.'     \          ,--,     ,-+-,.' _ |\    /  \    
     .---.|   |  .`\  |       ,'_ /|  ,-+-. ;   , |||   :    |   
   /.  ./|:   : |  '  |  .--. |  | : ,--.'|'   |  |||   | .\ :   
 .-' . ' ||   ' '  ;  :,'_ /| :  . ||   |  ,', |  |,.   : |: |   
/___/ \: |'   | ;  .  ||  ' | |  . .|   | /  | |--' |   |  \ :   
.   \  ' .|   | :  |  '|  | ' |  | ||   : |  | ,    |   : .  |   
 \   \   ''   : | /  ; :  | : ;  ; ||   : |  |/     :     |\`-'   
  \   \   |   | '\` ,/  '  :  \`--'   \   | |\`-'      :   : :      
   \   \ |;   :  .'    :  ,      .-./   ;/          |   | :      
    '---" |   ,.'       \`--\`----'   '---'           \`---'.|      
          '---'                                       \`---`      
                                                               
                              vDump
```
# vDump
Dump all videos from a YouTube channel.
## Requirements
- A web browser
- Python 3+ (tested on Python 3.10)
- `yt-dlp` from pip (`pip install yt-dlp`)
## Steps
0. Make sure you have all the requirements set up above.
1. Go to a YouTube channel, and scroll to the bottom of the page.
2. Open `Inspect Element` (Ctrl+Shift+I), and go to the `Console` tab.
3. Paste the contents of `dumper.js` into the `Console`, then press `Enter`.
4. When it is done, scroll up until you see the object.
5. Copy the object created (must be the root of it), into a file named `ytmanifest.json`.
   - On Firefox, right click on the root of the object (`Array(x_amount)` on Firefox).
   - Right click on it, then click `Copy Object`.
   - On Chrome, good luck.
6. Run `dl.py` (`python dl.py`).
