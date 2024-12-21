def reading(self):
    with open('deed.txt', 'r') as f:
        s = f.read()
        self.whip = ast.literal_eval(s)


import json
>>> d = {"one":1, "two":2}
>>> json.dump(d, open("text.txt",'w'))

This code dumps to a text file

$ cat text.txt 
{"two": 2, "one": 1}

Also you can load from a JSON file:

>>> d2 = json.load(open("text.txt"))
>>> print d2
{u'two': 2, u'one': 1}



import pickle

a = {
  'a': 1,
  'b': 2
}

with open('file.txt', 'wb') as handle:
  pickle.dump(a, handle)

with open('file.txt', 'rb') as handle:
  b = pickle.loads(handle.read())

print a == b # True

pair = {'name': name,'location': location}
with open('F:\\twitter.json', 'a') as f:
     f.writelines('{}:{}'.format(k,v) for k, v in pair.items())
     f.write('\n')

