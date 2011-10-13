## 0.3.2 (2011-10-04)

* A 'ninjab-setup' command which is installed in /usr/bin/ninjab-setup, to setup ninjab after base-install
* parts-prompt - Status if previous command took more than X seconds (default 10)
* parts-prompt - Info about running tmux sessions, if any
* A couple of bugfixes and polishing


## 0.3.1 (2011-10-01)

* Global 'ninjab' command for controlling ninjab.
* Support for osx brew installed bash_completion
* parts-prompt - Better git status when not in any default branch. Eg, when you are viewing remote branches, tags, and so on..
* Bug fixes


## 0.3 (2011-09-18)

* First initial version, started at v0.3 because its the "3rd" personal
  made version.
* new feature: Created a .spec file for rpm package creation, use
  `sh bin/build_rpm_package.sh` to build the newest version.
