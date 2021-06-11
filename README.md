# uninstall-script-maker

* This program generates uninstallation scripts for windows command line

* It intakes the application list through modifiable csv in the data folder called "appnames.csv"

* It intakes a common version to append to all these installer files

* It generates a text file with the complete command which you can copy on command line instance and execute

## To do list
* Add tests for final file generation

## Future improvements
* delete any current uninstall scripts and always create new file
* User interface addition
* Convert program to EXE so it doesnt require python installation
* Bring out the command concatenations to be read from external text files instead of hardcoded
* Add logging
* Add comments in code
* Generate .bat file instead of .txt
