# Garbageman
Garbageman is a simple script to handle jpg files, selecting non-desired pages and moving from a list (csv) of directory for a specific one or just upper one folder from its location

## Usage

### Colect Wanted JPG Files

#### CSV File

Path1 | Page Unwanted1 | Page Unwanted2 | Page Unwanted3 ... Page UnwantedN |

Path2 | Page Unwanted1 | Page Unwanted2 | Page Unwanted3 ... Page UnwantedN |

Path3 | Page Unwanted1 | Page Unwanted2 | Page Unwanted3 ... Page UnwantedN |

#### Script

In order to execute the Garbageman,

For moving a list of wanted jpg files, specify the csv path and saving path:
```
python3 garbageman.py -m CSV-PATH-FILE SAVING-PATH
```

### Moving JPG Files

#### CSV File

Path1 |

Path2 |

Path3 |

#### Script

For move all jpg files, specify the csv path and saving path [For moving to its upper folder, just leave it blank]:
```
python3 garbageman.py -u CSV-PATH-FILE SAVING-PATH
```
