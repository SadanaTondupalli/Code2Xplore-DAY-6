playlist=[180, 200, 220, 210]
invalid_entries=[]
for i in playlist:
    if i<=0:
        invalid_entries.append(i)

if len(invalid_entries)>0:
    print("Invalid Playlist")
    print("Invalid durations found:",invalid_entries)

else:
    total_duration=sum(playlist)
    songs=len(playlist)

    if total_duration<300:
        category="Too Short Playlist"
        recommendation="Add more songs"

    elif total_duration>3600:
        category="Too Long Playlist"
        recommendation="Trim the playlist"

    elif len(set(playlist))!=songs:
        category="Repetitive Playlist"
        recommendation="Add variety"


    elif max(playlist)-min(playlist)<=300:
        category="Balanced Playlist"
        recommendation="Good listening session"

    else:
        category="Irregular Playlist"
        recommendation="Adjust durations"

    print("Total Duration:",total_duration,"seconds")
    print("Songs:",songs)
    print("Category:",category)
    print("Recommendation:",recommendation)