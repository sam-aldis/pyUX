# pyUX

[![Join the chat at https://gitter.im/pyUX/Lobby](https://badges.gitter.im/pyUX/Lobby.svg)](https://gitter.im/pyUX/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
=======
You can clone both this project and its sub project (the UX Designer)
just by runnning
```
curl https://ukjp-design.com/pyUX.sh | sh
```
(Feel free to look at the source for this if your a bit worried about running unknown scripts)
also make sure you have the latest version of npm installed first with:
```
npm i -g npm
```
-------
A unified UML based python User Experience/UI Toolkit
-------


We aim to bring a cross platform (X/U)ML based UI experience for
all developers.

We will eventually be bringing you a GUI to create these UI's and
hope for a low learning curve for new developers looking to either
create Native stand-alone desktop application or Native addons for
their webservices in python.

At the moment bindings with GTK/wxPython will probably be preferred as we want
the project to be cross platform but in the future will provide a way
to use each platforms Native UI Elements whilest still keeping projects
cross platform.

We will also need to have a way to create binary files or something
similar to a .jar file which will run on every platform and contain the
python runtime files. this may be achieved with dockr for the moment.

-------
## Roadmap

- Current work is mostly going on in the subproject pyUXStudio, the outputed files will be parsed initially with pyUX but it could be implemented for other languages
- Once pyUXStudio is finished then work will continue on the API
- Start work on custom elements predesigned to look the same for all platforms (i.e. material design style xml elements)
- Create packager and deployment system
- Publish
- :smile:

### Feel free to issue pull requests, I will review daily when possible.
