"""
Code Snippets
"""

#https://www.reddit.com/r/Python/comments/12b9p5f/text_parsing_now_you_have_three_problems_david/
"""
Text Parsing: Now You Have Three Problems (David Beazley)
https://github.com/dabeaz/blog/blob/main/2023/three-problems.md
"""

#https://www.reddit.com/r/Python/comments/133ztzc/what_are_some_of_the_best_python_talks_to_rewatch/jicdo6b/?context=3
"""
What are some of the best python talks to (re)watch?
...
Recently i have been looking around for cool/good talks about python and found some things that i thought were super interesting like

https://realpython.com/must-watch-pycon-talks/#9-solve-your-problems-with-sloppy-python

https://www.youtube.com/watch?v=YY7yJHo0M5I

https://www.youtube.com/watch?v=sPiWg5jSoZI

but most of these are already a bit older.

Do any of you have interesting talks you can recommend?

https://www.youtube.com/watch?v=T-TwcmT6Rcw

https://www.youtube.com/watch?v=9zinZmE3Ogk
...

My favorite Python talk:

James Powell: So you want to be a Python expert? | PyData Seattle 2017
https://www.youtube.com/watch?v=cKPlPJyQrt4
"""

#https://www.reddit.com/r/learnpython/comments/12p2x11/what_are_some_good_publicly_available_python/jgkz7pw/?context=3
"""
You might find this resource useful https://github.com/vinta/awesome-python
...
Pro-tip, search for awesome and anything on GitHub and someone has probably made a list for it. e.g. https://github.com/MunGell/awesome-for-beginners
"""

# https://www.reddit.com/r/learnpython/comments/135hhrf/convert_boolean_values_into_strings_yes_or_no/jijtevq/?context=3
def convert_bool_str(mybool: bool) -> str:
    """
    Convert Boolean values into strings “yes” or “no”
    """
    return ["no", "yes"][mybool]

print(convert_bool_str(False))


#https://www.reddit.com/r/Python/comments/12tr2sn/pythoneers_here_what_are_some_of_the_best_python/jh46fkg/?context=3
"""
also the f'{foo=}' trick,
it equates to f'foo={foo}',
very useful in writing logging and error messages
"""
foo = "eins"
print(f'{foo=}')
"""
Works with expressions too:

foos = [1, 2]
bar, qaz = 3, 3
f"{(len(foos), bar + qaz)=}"

evalutates to:

(len(foos), bar + qaz)=(2, 6)
"""

#https://www.reddit.com/r/learnpython/comments/11l2mfw/help_with_save_load_a_player_stats_dictionary_for/jbblose/?context=3
"""
Ok so this is mutating:

player_stats["player_hp"] = 100

And this is rebinding:

player_stats = {"player_hp": 100}

In the first case, you're changing an item in the existing dictionary. In the second, you're referencing a completely new dictionary and pointing player_stats at that instead of what it was pointing at before.

You need global in the second case (assuming the name was defined outside of the current function) but you don't in the first case, because you're not changing what the name points at.

So for example you would need global in your load_game function, because you're changing what the name points at: a new dict which you have just loaded. But you wouldn't need it in update_player_hp as there you just change an item of the existing dict.
"""

# ?
#dir_sort = dict(sorted(dir_sizes.items(), key=lambda x: x[1], reverse=True))
