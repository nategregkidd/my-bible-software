# This is a test program to attempt to simulate a concordance.
import pandas as pd

bibledata = pd.read_csv("./csv/t_asv.csv")
print(bibledata)
print()
print(bibledata.head())
print()
print(bibledata.columns)
print()
ids = bibledata["id"]
print(ids)

print("\n\n\n")
while True:
    book = input("which book ya want?: ")
    requested_book = bibledata[bibledata['b'] == int(book)]
    print(requested_book.head())

genesis = bibledata[bibledata['c'] == 1]
print("\n\n\n genesis!")
print(genesis.head())