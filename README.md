<p align="center">
 <img alt="ApertureTerminal" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Aperture_Laboratories_Logo.svg/1024px-Aperture_Laboratories_Logo.svg.png" height="140" />
</p>

# ApertureTerminal

Customizes your Mac terminal to look like the popular Aperture Science terminal from the Portal series by Steam (if you haven't, go play it!)

# Dependencies
If you dont already have these installed, they are very easy to get with Homebrew (instructions at https://brew.sh). Its just brew install (name) once you have it installed.
 
  git `brew install git`
 
  python (version 3 is recommended) `brew install python`
  
  pip (comes with python, usually)
  
  portaudio (brew install portaudio) `brew install portaudio`
  
 built for the newer macOS zsh terminal.
  
# Hardware/OS requirements
Really, you just need any type of mac running OSX or later! Its that simple!

# Setup
In you macOS terminal, navigate to Applications > Utilites > Terminal and open it.
Next, type the following: 

`cd Desktop`

This will change your working directory to the desktop! Then type this:

`git clone https://github.com/Codeiology/ApertureTerminal.git`

A new folder called ApertureTerminal should appear on your desktop! Now, type this:

`cd ApertureTerminal`

Now your working directory is the repository! Now, we can get to the customization, starting with:

`pbcopy < motd.txt`

This will copy the custom MOTD to your clipboard. Now navigate back to your home directory:

`cd ~`

And type this:

`sudo nano /etc/motd`

This will put you in the nano text editor terminal, where you will simply Command+V to paste it in.
Now, you just gotta save it! All you gotta do is hold Control+X, and then hit Y, and then enter/return.
You should now be back in the regular terminal. Close out of the window and reopen the terminal to check that it worked!

Great! Now for the custom prompt! Go back to the repository:

`cd ApertureTerminal`

and copy some more code:

`pbcopy < zshprompt.sh`

back to the home directory:

`cd ~`

Go back to the nano terminal by typing:

`sudo nano zshprompt.sh`

Now, you know the drill, just Command+V, and boom! Hit Control+X, Y, and enter/return.
Now that you are back in the regular terminal, go back to the repo:

`cd ApertureTerminal`

and copy some more code:

`pbcopy < zshprompt.sh`

Back to the nano terminal 😁:

`sudo nano .zshrc`

And you know, the regular drill, Hit Command+V, Control+X, Y, then enter/return.
Now, to test that it works, close the window and reopen it, and you should have a fully fledged Aperture Terminal!

If you want to do the python experience I made included with this repo, make sure you have python installed, the repo is on the desktop, and type:

`glados`

Boom! By the way, the code is JAT4736251 ;)

# Custom Commands

Assuming that you did everything right and the ApertureTerminal file is in your desktop and nowhere else, you should be able to execute some custom commands (like the one above with `glados`)!
type `help` to get started!

# To Undo

If you have decided you have had enough Aperture terminal, you can do the following to undo everything:

`sudo nano .zshrc`

Then delete everything and save it with Command+V, Control+X, Y, then enter/return. Now,

`sudo nano /etc/motd`

And delete everything there, too. Now everything should be back to normal!
