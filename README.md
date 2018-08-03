Borderlands Online BPD Generator
================================

This is the code which runs my [Borderlands 2 / The Pre-Sequel BPD Graphs](http://apocalyptech.com/games/bl-bpd/)
generation page.  The meat of the application is actually a Python 3
script which makes use of some of my [FT Explorer](https://github.com/apocalyptech/ft-explorer)
data libraries, and the rest is a PHP shell which goes around that.

**WARNING:** The PHP page itself isn't actually standlone, and you'll
have to do some work if you want to host this yourself elsewhere.  It's
hooked into my site's overall framework, so those calls will not work.
It shouldn't be difficult to adapt it anywhere else, though, just replace
all the calls to `$page` with your own template. stuff.

Requirements
============

* This has only ever been run on Linux.  It should be easy enough to
  adapt to anywhere else, though.

* The main `bpd_dot.py` generation script is in Python 3.

* The application requires a local [Graphviz](https://www.graphviz.org/)
  install, specifically the binaries `dot` and `unflatten`.

* The PHP code itself doesn't have any specific requirements that I'm
  aware of, apart from having a hardcoded path to `/usr/bin/python36` and
  to the Graphviz utilities at `/usr/bin/dot` and `/usr/bin/unflatten`.

* The PHP code will attempt to write cached images into a `cache`
  directory.  It's recommended that your site not allow directory indexes,
  though that's not explicitly configured in here.

Credits
=======

The bundled pre-dumped object data is taken from BLCMM, by
[LightChaosman](https://www.youtube.com/channel/UCgJ6TA5sZ_Rwc1LPDYbQT1Q), and
is included with his gracious consent.

License
=======

This is licensed under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).
See [COPYING.txt](COPYING.txt).

Redistribution of the bundled data in the `resources` directory should be
cleared with LightChaosman first.  Try the
[Shadow's Evil Hideout discord channel](https://discord.gg/0YjZxbVBS9b3bXUS).
