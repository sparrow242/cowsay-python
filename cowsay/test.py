# We are using this tests to be sure, the output will not change

import unittest
import io
import sys

from .main import beavis, cheese, daemon, cow, dragon, ghostbusters
from .main import kitty, meow, milk, pig, stegosaurus, stimpy, turkey
from .main import turtle, tux

LOREM = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum."""
LOREM = LOREM.replace("\n", "")

BEAVIS_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                              _------~~-,
                                                           ,'            ,
                                                           /               \\
                                                          /                :
                                                         |                  '
                                                         |                  |
                                                         |                  |
                                                          |   _--           |
                                                          _| =-.     .-.   ||
                                                          o|/o/       _.   |
                                                          /  ~          \\ |
                                                        (____\@)  ___~    |
                                                           |_===~~~.`    |
                                                        _______.--~     |
                                                        \\________       |
                                                                 \\      |
                                                               __/-___-- -__
                                                              /            _ \\
"""

CHEESE_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                           /     \_/         |
                                                          |                 ||
                                                          |                 ||
                                                         |    ###\  /###   | |
                                                         |     0  \/  0    | |
                                                        /|                 | |
                                                       / |        <        |\ \
                                                      | /|                 | | |
                                                      | |     \_______/   |  | |
                                                      | |                 | / /
                                                      /||                 /|||
                                                         ----------------|
                                                              | |    | |
                                                              ***    ***
                                                             /___\  /___\
"""

DAEMON_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                          /- _  `-/  '
                                                         (/\/ \ \   /\
                                                         / /   | `    \
                                                         O O   ) /    |
                                                         `-^--'`<     '
                                                        (_.)  _  )   /
                                                         `.___/`    /
                                                           `-----' /
                                              <----.     __ / __   \
                                              <----|====O)))==) \) /====
                                              <----'    `--' `.__,' \
                                                           |        |
                                                            \       /
                                                      ______( (_  / \______
                                                    ,'  ,-----'   |        \
                                                    `--{__________)        \/
"""

COW_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                         ^__^
                                                         (oo)\_______
                                                         (__)\       )\/\
                                                             ||----w |
                                                             ||     ||
"""

DRAGON_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                                               / \\  //\\
                                                                |\\___/|      /   \\//  \\\\
                                                                /0  0  \\__  /    //  | \\ \\
                                                               /     /  \\/_/    //   |  \\  \\
                                                               \@_^_\@'/   \\/_   //    |   \\   \\
                                                               //_^_/     \\/_ //     |    \\    \\
                                                            ( //) |        \\///      |     \\     \\
                                                          ( / /) _|_ /   )  //       |      \\     _\\
                                                        ( // /) '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
                                                      (( / / )) ,-{        _      `-.|.-~-.           .~         `.
                                                     (( // / ))  '/\\      /                 ~-. _ .-~      .-~^-.  \\
                                                     (( /// ))      `.   {            }                   /      \\  \\
                                                      (( / ))     .----~-.\\        \\-'                 .~         \\  `. \\^-.
                                                                 ///.----..>        \\             _ -~             `.  ^-`  ^-_
                                                                   ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                                                                      /.-~
"""

GHOSTBUSTERS_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                                     __---__
                                                                  _-       /--______
                                                             __--( /     \ )XXXXXXXXXXX\v.
                                                           .-XXX(   O   O  )XXXXXXXXXXXXXXX-
                                                          /XXX(       U     )        XXXXXXX\
                                                        /XXXXX(              )--_  XXXXXXXXXXX\
                                                       /XXXXX/ (      O     )   XXXXXX   \XXXXX\
                                                       XXXXX/   /            XXXXXX   \__ \XXXXX
                                                       XXXXXX__/          XXXXXX         \__---->
                                               ---___  XXX__/          XXXXXX      \__         /
                                                 \-  --__/   ___/\  XXXXXX            /  ___--/=
                                                  \-\    ___/    XXXXXX              '--- XXXXXX
                                                     \-\/XXX\ XXXXXX                      /XXXXX
                                                       \XXXXXXXXX   \                    /XXXXX/
                                                        \XXXXXX      >                 _/XXXXX/
                                                          \XXXXX--__/              __-- XXXX/
                                                           -XXXXXXXX---------------  XXXXXX-
                                                              \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                                                                ""VXXXXXXXXXXXXXXXXXXV""
"""

KITTY_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \

                                                         ("`-'  '-/") .___..--' ' "`-._
                                                             ` *_ *  )    `-.   (      ) .`-.__. `)
                                                             (_Y_.) ' ._   )   `._` ;  `` -. .-'
                                                          _.. `--'_..-_/   /--' _ .' ,4
                                                       ( i l ),-''  ( l i),'  ( ( ! .-'
"""

MEOW_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                                        _ ___.--'''`--''//-,-_--_.
                                                            \\`"' ` || \\\\ \\ \\\\/ / // / ,-\\\\`,_
                                                           /'`  \\ \\ || Y  | \\|/ / // / - |__ `-,
                                                          /\@"\\  ` \\ `\\ |  | ||/ // | \\/  \\  `-._`-,_.,
                                                         /  _.-. `.-\\,___/\\ _/|_/_\\_\\/|_/ |     `-._._)
                                                         `-'``/  /  |  // \\__/\\__  /  \\__/ \\
                                                              `-'  /-\\/  | -|   \\__ \\   |-' |
                                                                __/\\ / _/ \\/ __,-'   ) ,' _|'
                                                               (((__/(((_.' ((___..-'((__,'
"""

MILK_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                             ____________
                                                             |__________|
                                                            /           /\
                                                           /           /  \
                                                          /___________/___/|
                                                          |          |     |
                                                          |  ==\ /== |     |
                                                          |   O   O  | \ \ |
                                                          |     <    |  \ \|
                                                         /|          |   \ \
                                                        / |  \_____/ |   / /
                                                       / /|          |  / /|
                                                      /||\|          | /||\/
                                                          -------------|
                                                              | |    | |
                                                             <__/    \__>
"""

PIG_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                                   ,.
                                                                  (_|,.
                                                                  ,' /, )_______   _
                                                              __j o``-'        `.'-)'
                                                              (")                 \'
                                                              `-j                |
                                                                  `-._(           /
                                                                      |_\  |--^.  /
                                                                  /_]'|_| /_)_/
                                                                      /_]'  /_]'
"""

STEGOSAURUS_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                                                   / `.   .' "
                                                                           .---.  <    > <    >  .---.
                                                                           |    \  \ - ~ ~ - /  /    |
                                                       _____          ..-~             ~-..-~
                                                      |     |   \~~~\.'                    `./~~~/
                                                     ---------   \__/                        \__/
                                                    .'  O    \     /               /       \  "
                                                   (_____,    `._.'               |         }  \/~~~/
                                                    `----.          /       }     |        /    \__/
                                                          `-.      |       /      |       /      `. ,~~|
                                                              ~-.__|      /_ - ~ ^|      /- _      `..-'
                                                                   |     /        |     /     ~-.     `-. _  _  _
                                                                   |_____|        |_____|         ~ - . _ _ _ _ _>
"""

STIMPY_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                             .    _  .
                                                            |\_|/__/|
                                                            / / \/ \  \
                                                           /__|O||O|__ \
                                                          |/_ \_/\_/ _\ |
                                                          | | (____) | ||
                                                          \/\___/\__/  //
                                                          (_/         ||
                                                           |          ||
                                                           |          ||\
                                                            \        //_/
                                                             \______//
                                                            __ || __||
                                                           (____(____)
"""

TURKEY_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                                                           ,+*^^*+___+++_
                                                                                     ,*^^^^              )
                                                                                  _+*                     ^**+_
                                                                                +^       _ _++*+_+++_,         )
                                                            _+^^*+_    (     ,+*^ ^          \\+_        )
                                                           {       )  (    ,(    ,_+--+--,      ^)      ^\\
                                                          { (\@)    } f   ,(  ,+-^ __*_*_  ^^\\_   ^\\       )
                                                         {:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
                                                        ( /  (    (        ,___    ^*+_+* )   <    <      \\
                                                         U _/     )    *--<  ) ^\\-----++__)   )    )       )
                                                          (      )  _(^)^^))  )  )\\^^^^^))^*+/    /       /
                                                        (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
                                                       (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
                                                        *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
                                                        \\             \\_)^)_)) ))^^^^^^^^^^))^^^^)
                                                         (_             ^\\__^^^^^^^^^^^^))^^^^^^^)
                                                           ^\\___            ^\\__^^^^^^))^^^^^^^^)\\\\
                                                                ^^^^^\\uuu/^^\\uuu/^^^^\\^\\^\\^\\^\\^\\^\\^\\
                                                                   ___) >____) >___   ^\\_\\_\\_\\_\\_\\_\\)
                                                                  ^^^//\\\\_^^//\\\\_^       ^(\\_\\_\\_\\)
                                                                    ^^^ ^^ ^^^ ^
"""

TURTLE_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         \
                                                                                             ___-------___
                                                                                         _-~~             ~~-_
                                                                                      _-~                    /~-_
                                                           /^\__/^\         /~  \                   /    \
                                                         /|  O|| O|        /      \_______________/        \
                                                        | |___||__|      /       /                \          \
                                                        |          \    /      /                    \          \
                                                        |   (_______) /______/                        \_________ \
                                                        |         / /         \                      /            \
                                                         \         \^\\         \                  /               \     /
                                                           \         ||           \______________/      _-_       //\__//
                                                             \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                                                               ~-----||====/~     |==================|       |/~~~~~
                                                                (_(__/  ./     /                    \_\      \.
                                                                       (_(___/                         \_____)_)
"""

TUX_SOLUTION = r"""
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consetetur sadipscing |
| elitr, sed diamnonumy eirmod tempor invidunt ut   |
| labore et dolore magna aliquyam erat,sed diam vol |
| uptua. At vero eos et accusam et justo duo dolore |
| s et ea rebum.                                    |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         .--.
                                                        |o_o |
                                                        |:_/ |
                                                       //   \ \
                                                      (|     | )
                                                     /'\_   _/`\
                                                     \___)=(___/
"""

def capture_output(function, arguments):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    function(arguments)
    sys.stdout = sys.__stdout__
    captured_output.seek(0)
    return captured_output.read()

def delete_empty_lines(data):
    new_data = []
    for line in data:
        if len(line.strip()) > 0:
            new_data.append(line)
    return new_data

class TestCowsay(unittest.TestCase):

    def test_beavis(self):
        output = capture_output(beavis, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(BEAVIS_SOLUTION)
        assert output == solution

    def test_cheese(self):
        output = capture_output(cheese, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(CHEESE_SOLUTION)
        assert output == solution

    def test_daemon(self):
        output = capture_output(daemon, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(DAEMON_SOLUTION)
        assert output == solution

    def cow_daemon(self):
        output = capture_output(cow, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(COW_SOLUTION)
        assert output == solution

    def test_dragon(self):
        output = capture_output(dragon, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(DRAGON_SOLUTION)
        assert output == solution

    def test_ghostbusters(self):
        output = capture_output(ghostbusters, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(GHOSTBUSTERS_SOLUTION)
        assert output == solution

    def test_kitty(self):
        output = capture_output(kitty, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(KITTY_SOLUTION)
        assert output == solution

    def test_meow(self):
        output = capture_output(meow, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(MEOW_SOLUTION)
        assert output == solution

    def test_milk(self):
        output = capture_output(milk, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(MILK_SOLUTION)
        assert output == solution

    def test_pig(self):
        output = capture_output(pig, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(PIG_SOLUTION)
        assert output == solution

    def test_stegosaurus(self):
        output = capture_output(stegosaurus, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(STEGOSAURUS_SOLUTION)
        assert output == solution

    def test_stimpy(self):
        output = capture_output(stimpy, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(STIMPY_SOLUTION)
        assert output == solution

    def test_turkey(self):
        output = capture_output(turkey, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(TURKEY_SOLUTION)
        assert output == solution

    def test_turtle(self):
        output = capture_output(turtle, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(TURTLE_SOLUTION)
        assert output == solution

    def tux_turtle(self):
        output = capture_output(tux, (LOREM))
        output = delete_empty_lines(output)
        solution = delete_empty_lines(TUX_SOLUTION)
        assert output == solution


if __name__ == "__main__":
    unittest.main()