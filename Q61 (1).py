#author name is Julia
import dbm
photo_category = dbm.open("captions", "c")
photo_category["animals.png"] = "a picture of a zebra"
photo_category["me.png"] = "a photo of me"
photo_category["brother.png"] = "a photo of my brother"
photo_category["animals.png"] = "a lion"
photo_category["me.png"] = "me and my sister"
photo_category["brother.png"] = "my sister"
for item in photo_category:
    print(item, photo_category[item])
