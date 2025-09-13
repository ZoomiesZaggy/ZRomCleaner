ZRom Cleaner

I built this to clean up a messy ROM library. Too many duplicates, tiny revision differences, and mixed regions. ZRom Cleaner keeps one great copy per game, does not split multi disc sets, and starts in Preview so nothing gets deleted by accident.

What It Does

- Keeps the best version of each game.
- USA first by default. You can switch to Japan first, Europe first, or your own order.
- Optional "Original + Best Revision" pairing.
- Multi disc sets stay intact.
- Moves extras to a Quarantine folder by default, so you can undo.
- Simple app window with Preview, Apply, Undo, and a CSV report.
- Dark Mode and a Cancel button for long scans.

Download

1. Go to the Releases tab of this repo.
2. Download the Windows zip or the Mac zip.
3. Unzip and run the app.

Before You Start

1) Back up your ROMs.  
   The app starts in Preview. Nothing moves until you Apply. Hard Delete is off by default.

2) Know your ROM folder path.  
   Windows: D:\Roms  
   Windows with spaces: "D:\Roms\NES and SNES"  
   Mac or Linux: /Volumes/SSD/Roms  
   Mac or Linux with spaces: "/Volumes/SSD/Retro Games"

3) Test on a small folder first.  
   Try 20 to 50 ROMs. Run Preview, then Apply.

4) Quarantine and Undo.  
   Removed files go to _ZRomCleaner_Quarantine (unless you change it). Undo restores.

5) Free space check.  
   Leave 10 to 20 percent free for Quarantine.

6) Avoid cloud sync while cleaning.  
   Work on a local drive. Move back later if you want.

Quick Start for Windows

1. Download the Windows zip from Releases.
2. Right click the zip and choose "Extract All".
3. Open "ZRomCleaner.exe".
4. If Windows warns you, click "More info", then "Run anyway".

Quick Start for Mac

1. Download the Mac zip from Releases.
2. Unzip and open "ZRomCleaner".
3. If macOS blocks it, go to System Settings > Privacy and Security > Open Anyway.

Using the App

1. Click "Browse" and pick your ROM folder.
2. Choose a "Region Profile" (USA first is default), or type your own order like U E UK J W.
3. Click "Preview". This is a safe test run; nothing is moved yet.
4. Review the list.
5. Turn on "Apply" and run again when you are ready.
6. Extras are moved to the "Quarantine" folder so you can undo.

How It Works

Legend  
[KEEP] kept in place.  
[REMOVE] moved to Quarantine, or deleted if Hard Delete is on.

Example 1 - Region, revision, and special editions (The Legend of Zelda)  
Before  
The Legend of Zelda (USA).nes  
The Legend of Zelda (USA) (Rev 1).nes  
The Legend of Zelda (Europe).nes  
The Legend of Zelda (Virtual Console) (USA).nes  
The Legend of Zelda (Collector's Edition) (USA).iso

After (USA first)  
[KEEP]   The Legend of Zelda (USA) (Rev 1).nes. Reason: best revision.  
[KEEP]   The Legend of Zelda (USA).nes. Reason: original + best pair (optional).  
[KEEP]   The Legend of Zelda (Virtual Console) (USA).nes. Reason: special edition is its own release.  
[KEEP]   The Legend of Zelda (Collector's Edition) (USA).iso. Reason: special edition is its own release.  
[REMOVE] The Legend of Zelda (Europe).nes. Reason: region priority.

Example 2 - Regional priority (Contra)  
Before  
Contra (USA).zip  
Contra (Europe).zip  
Contra (Japan).zip

After (USA first)  
[KEEP]   Contra (USA).zip.  
[REMOVE] Contra (Europe).zip.  
[REMOVE] Contra (Japan).zip.

After (Japan first)  
[KEEP]   Contra (Japan).zip.  
[REMOVE] Contra (USA).zip.  
[REMOVE] Contra (Europe).zip.

Example 3 - Multi disc set  
Before  
Final Fantasy VIII (USA) (Disc 1).bin  
Final Fantasy VIII (USA) (Disc 2).bin  
Final Fantasy VIII (Europe) (Disc 1).bin  
Final Fantasy VIII (Europe) (Disc 2).bin

After (USA first)  
[KEEP]   Final Fantasy VIII (USA) (Disc 1).bin.  
[KEEP]   Final Fantasy VIII (USA) (Disc 2).bin.  
[REMOVE] Final Fantasy VIII (Europe) (Disc 1).bin.  
[REMOVE] Final Fantasy VIII (Europe) (Disc 2).bin.  
Note: multi disc sets are never split.

Command Line (Optional)

If you like the terminal, you can run it there too.

```bash
python zrom_cleaner.py
python zrom_cleaner.py D:\Roms --regions U E UK J W --report report.csv
python zrom_cleaner.py D:\Roms --regions U E UK J W --keep-original-pair --apply
```

Example interaction when no path is provided:

```
$ python zrom_cleaner.py
Enter ROM directory [current directory]:
Validated path: /home/user/roms
```
