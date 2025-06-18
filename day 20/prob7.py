posts=[
    {"user":"alice","post":"hi"},
    {"user":"bob","post":"hello"},
    {"user":"alice","post":"again"},
    {"user":"x","post":"xyz"},
    {"user":"bob","post":"again"}
    
]
post_count = {}
for i in posts:
    if i["user"] in post_count:
        post_count[i["user"]]=post_count[i["user"]]+1
    else:
        post_count[i["user"]]=1
print(post_count)