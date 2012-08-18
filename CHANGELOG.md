## 0.3.4

* parts-prompt - Per folder configuration posibility
* parts-prompt - Some minor bugfixes with text overwriting other text on the shell
* parts-prompt - Unlimited history extra log. Enabled by default, set load_part_bash_extra_unlimited_history to "" in config to disable.

## 0.3.3 (2012-01-22)

* parts-prompt - Only show detached tmux sessions
* parts-prompt - Better git handeling
* parts-prompt - Prepend ourself to PROMPT_COMMAND, in case other tools are using it as well
* functions/parts-prompt - Better color handeling. Choose between bash and tput. bash
	as default since tput is buggy some times
* parts-prompt . Some minor bugfixes


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
