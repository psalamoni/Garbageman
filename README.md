# Garbageman
Garbageman is a simple script to handle jpg files, selecting non-desired pages and moving from a list (csv) of directory for a specific one or just upper one folder from its location

## Usage

### Colect Wanted JPG Files

#### CSV File

Path | Page Unwanted | Page Unwanted | Page Unwanted ...

#### Script

In order to execute the Garbageman,

For moving a list of wanted jpg files, specify the csv path and saving path:
```
python3 garbageman.py -m CSV-PATH-FILE SAVING-PATH
```

### Moving JPG Files

#### CSV File

Path

#### Script

For move all jpg files, specify the csv path and saving path [For moving to its upper folder, just leave it blank]:
```
python3 garbageman.py -u CSV-PATH-FILE SAVING-PATH
```
