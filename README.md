ninjab
======

Features
--------

* Tries to be as cross platform as possible.
* Configuration for the most common needs.
* Will set bash options to make it better to use.
* Tries to turn on bash features which isnt enable as default (but is very usefull)
* Colorizing the output where possible.
* Usefull "smart" bash prompt
* Aliases which tries to save you time and give you more info as default.
* Creates some usefull hotkeys
* Different parts
  * [1_bash](https://github.com/xeor/ninjab/wiki/parts-1_bash)
  * [3_aliases](https://github.com/xeor/ninjab/wiki/parts-3_aliases)
  * [4_prompt](https://github.com/xeor/ninjab/wiki/parts-4_prompt)
  * [5_stateinfo](https://github.com/xeor/ninjab/wiki/parts-5_stateinfo)
  * [6_pipes](https://github.com/xeor/ninjab/wiki/parts-5_pipes)
* Lots more, take a look inside the files in parts/


Known issues
------------
* *sudo su*: When sudoing to root (sudo su), we will get some problems using the prompt. Therefor, a plain prompt is set when using sudo. You can use an alias called 'ss' to sudo yourself to root without this problem. 'ss' will run 'sudo bash -l' which works as expected using the prompt.

Installation
------------
If you want easy updates, and maybe want to contribute at some point. Use this method.

### Using git
1. `git clone git://github.com/xeor/ninjab.git ninjab`: Clone the repository to wherever you want
2. `cp ninjab/config ~/.ninjab.conf && nano ~/.ninjab.conf`: Create your own local config file and edit it.
3. `echo '. /home/username/ninjab/loader' >> ~/.profile`: Make sure the loader is started with a new shell
4. Try to start a new shell

### Using RPM
1. `wget https://github.com/downloads/xeor/ninjab/ninjab-latest.noarch.rpm`
2. `rpm -ivh ninjab-latest.noarch.rpm`
3. `cp /usr/share/ninjab/config ~/.ninjab.conf && nano ~/.ninjab.conf`: Create your own local config file and edit it.
4. `echo '. /usr/share/ninjab/loader' >> ~/.profile`: Make sure the loader is started with a new shell
5. Try to start a new shell

Configuration
-------------
ninjab looks for configuration in 4 different places, in this order.

* `config` in its own directory first. Dont edit this file, it might get things added in future versions.
* `/etc/ninjab.conf` for global configuration.
* `config.local` in its own directory. If you want any local changes use this. It wont be touched by updates.
* `~/.ninjab.conf` in your home directory.