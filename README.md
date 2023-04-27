# playOnce
A simple blender add-on utility

<img width="454" alt="playOnceVIEW3D UI" src="https://user-images.githubusercontent.com/96590051/232178830-f213133f-fea7-4986-8808-db937d3047f3.png">

This is a really simple blender add-on that makes it easier to play back your animation only once when you are testing it.

It has bothered me for years that when it comes to testing my animations, blender automatically loops playback continuously, forcing me to hit the pause button when I want to stop it. Why would the developers have set it up this way? It's curious to me, am I the only one to prefer to replay only once to see how it all flows in a single run? Did I overlook some obvious button?

Well, no matter now. This add-on, playOnce, creates a check box that can be toggled to allow blender users to decide whether the timeline playback should automatically loop continuously after the playhead reaches the endframe (blender's current default) or not. When playOnce is toggled ON and its "play" button is pressed, the playhead will only play back your animation just once, and then stop at the end frame. Get it? Play Once! :D

Hope you enjoy it and I certainly welcome any suggestions or collaborations on this. Please don't hesitate to contact me directly.

Best wishes, Andrew


PS:

To use this in blender, simply download the playOnce.py file and go to Preferences>Add-ons and then install and activate the file.

Since this is the earliest version, I haven't yet implemented an __init__ file so that you can install it as a zip and activate that way, maybe I'll do that next. Also I will probably refactor the code sometime. One feature I have yet to figure out how to do (please feel free to fork and fix!) is to change the operator on the playback button in the Timeline topbar - playOnce works in the UI side (N) panel, but not the main blender buttons yet.


