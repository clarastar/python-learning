def func(*args, **kwargs):
    print (args, kwargs)
func(1, "Welcome", name="thefourtheye", year=2013)


for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
words