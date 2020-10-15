import datetime

GEEK_MUSIC_LINKS = [
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Computer+Love+by+Kraftwerk">Computer Love by Kraftwerk</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Paranoid+Android+by+Radiohead">Paranoid Android by Radiohead</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Computer+Age+by+Neil+Young">Computer Age by Neil Young</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Digital+by+Joy+Division">Digital by Joy Division</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Silver+Machine+by+Hawkwind">Silver Machine by Hawkwind</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Start+the+Simulator+by+A-Ha">Start the Simulator by A-Ha</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Internet+Connection+by+M.I.A.">Internet Connection by M.I.A.</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Deep+Blue+by+Arcade+Fire">Deep Blue by Arcade Fire</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=I+Will+Derive!+by+MindofMatthew">I Will Derive! by MindofMatthew</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Lobachevsky+by+Tom+Lehrer">Lobachevsky by Tom Lehrer</a>']

    
SNAKE_MUSIC_LINKS = [
 '<a target="_blank" href="https://www.youtube.com/results?search_query=The+Universe+Song+by+Monty+Python">The Universe Song by Monty Python</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Crawling+King+Snake+by+The+Doors">Crawling King Snake by The Doors</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Ain\'t+No+Love+In+the+Heart+of+the+City+by+Whitesnake">Ain\'t No Love In the Heart of the City by Whitesnake</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=The+Serpent+by+Genesis">The Serpent by Genesis</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Charm+the+Snake+by+Christopher+Cross">Charm the Snake by  Christopher Cross</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Slither+by+Velvet+Revolver">Slither by Velvet Revolver</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Where\'s+My+Snake+by+Bow+Wow+Wow">Where\'s My Snake by Bow Wow Wow</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=The+Sidewinder+Sleeps+Tonight+by+R.E.M.">The Sidewinder Sleeps Tonight by R.E.M.</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Tube+Snake+Boogie+by+ZZ+Top">Tube Snake Boogie by ZZ Top</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Union+of+the+Snake+by+Duran+Duran">Union of the Snake by Duran Duran</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Sneaky+Snake+by+Tom+T.+Hall">Sneaky Snake by Tom T. Hall</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Snakebit+by+Kris+Kristofferson">Snakebit by Kris Kristofferson</a>',
 '<a target="_blank" href="https://www.youtube.com/results?search_query=Long+Come+a+Viper+by+Dan+Hicks+&+His+Hot+Licks">' ## don't add a commma!
 'Long Come a Viper by Dan Hicks & His Hot Licks</a>']


TESTS = {
 
  "anagrams": [
      (("listen","silent"), True, 1),
      (("Listen","Silent"), True, 1),
      (("this","that"), False, 1),
      (("this","This"), False, 1),
    ],

   "is_palindrome": [
      ("Abba", True, 1),
      ("Python", False, 1),
      ("Rotator", True, 1),
      ("Was it a cat I saw?", True, 1),
    ],

   "is_english_word": [
      ("this",      True, 1),
      ("Python",    True, 1),
      #("Pytastic",  False, 1),
      ("HelP",      False,  1),
      ("Flibbertigibbet", True,  1),
      ("Brexit",          False, 1),
      ],

   "password_strength": [
       ("python",            "ILLEGAL",     1 ),
       ("boa constrictor",   "ILLEGAL",     1 ),
       ("Secret9",           "WEAK",     1 ),
       ("secret99",          "MEDIUM",   1 ),
       #("Secret999!",        "MEDIUM",   1 ),  
       #("BMX-122333444555Z", "MEDIUM",   1 ),
       ("7Kings8all9Pies!",   "STRONG",   1 ),
    ],

  "find_all_anagrams": [
        ("cheese", [], 1 ),
        ("Python", ['phyton', 'typhon'], 1),
        ("Listen!", [], 1 ),
        ("SeaBird", ['abiders', 'braised', 'darbies', 'sidebar'], 1),  
      ],
    
   "find_palindromes_of_length": [
       ( 7, ['deified', 'halalah', 'reifier',
              'repaper', 'reviver', 'rotator',
              'sememes'], 1 ),
       ( 10, [], 1 ),
      ],

    "total_play_time" : [
       ( "geek-music" , datetime.timedelta(minutes=45,seconds=32), 2),
       ( "snake-music" , datetime.timedelta(seconds=2911), 1)
    ],

    "youtube_query_links" : [
       ( "geek-music" ,  GEEK_MUSIC_LINKS,  2),
       ( "snake-music" , SNAKE_MUSIC_LINKS, 1)
    ]
}

## This wrapper just returns none, which supresses
## the result being printed out in Jupyter notebooks
def do_tests( function ):
    do_tests_return_marks( function )
    return None

def do_tests_return_marks( function ):
    max_marks = 0
    marks = 0
    function_name = function.__name__
    if function_name not in TESTS:
        print("\n!!! ERROR: no tests defined for function:", function_name)
        return (0,0)
    
    print("\nRunning tests for function:", function_name )
    tests = TESTS[function_name]
    for test in tests:
        (test_input, test_answer, test_marks) = test
        max_marks += test_marks

        print( "  * {}( {} )  ...".format(function_name, test_input.__repr__() ))

        if not type(test_input) == tuple:
           test_input = (test_input,)

        result = function(*test_input)

        print("    returned:", result.__repr__() )

        # Handle case where answer may be a list in any order
        # by sorting both the result and the answer.
        if ( type(test_answer) == tuple and test_answer[0] == "any_order"
             and type(result) == list 
           ):
           result.sort()
           test_answer = test_answer[1]
           test_answer.sort() 

        if result == test_answer:
           print("    Correct :)   ({})".format(test_marks) )
           marks += test_marks
        else:
           print("    Incorrect :(   (should be {})".format(test_answer.__repr__()))
    print( "Total marks for this function: {} (of {})".format(marks, max_marks) )          
    return (marks, max_marks)
        

##SPELL_CHECK_TOTAL = 10
##SCTOTSTR = "(of 10)"
##SPELL_TEST_FILENAME = "spelling.txt"
##
##def do_all_tests( functions, hand_grades ):
##      scmark = hand_grades["spell_check_file"]
##      if scmark:
##          marks = scmark
##      else:
##          marks = 0

def do_all_tests( functions ):
      marks = 0
      max_marks = 0
      for function in functions:
          fmark, fmax = do_tests_return_marks(function)
          marks += fmark
          max_marks += fmax
      #print("\nHand grade for spell_check_file:", scmark, SCTOTSTR)
      print("\nFINAL TOTAL =", marks, " (of", str(max_marks) + ")")
      print("\nTests version:", tests_version())        
      print("\nNOTE: This test set is for pre-testing of your code.")
      print("The tests used for final grading will be different.")
      print("Thus, your final grade may also be different from" )
      print("the grade given here.")

def tests_version():
     return( "14th October, 2020")


