bashrc
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
  * [1_bash](https://github.com/xeor/bashrc/wiki/parts-1_bash)
  * [3_aliases](https://github.com/xeor/bashrc/wiki/parts-3_aliases)
  * [4_prompt](https://github.com/xeor/bashrc/wiki/parts-4_prompt)
* Lots more, take a look inside the files in parts/


Known issues
------------
* *sudo su*: When sudoing to root (sudo su), we will get some problems using the prompt. Therefor, a plain prompt is set when using sudo. You can use an alias called 'ss' to sudo yourself to root without this problem. 'ss' will run 'sudo bash -l' which works as expected using the prompt.

Installation
------------

If you want easy updates, and maybe want to contribute at some point. Use this method.

1. `git clone git://github.com/xeor/bashrc.git bashrc`: Clone the repository to wherever you want
2. `nano bashrc/config`: Edit the configuration file.
3. `echo '. /home/username/bashrc/loader' >> /home/username/.profile`: Make sure the loader is started with a new shell
4. Try to start a new shell
