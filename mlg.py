import mlg_header_files
trip = []
story = ""
trip.append(input("Enter your friend's name: "))
trip.append(input("Enter a place you recently visited: "))
trip.append(input("How was the weather there ?: "))
trip.append(input("Enter a place nearby that place you visited: "))
trip.append(input("What did you find there in abundance ?: "))
trip.append(input("How did you like it ?: "))
trip.append(input("What did you like there ?: "))
trip.append(input("Where else did you go there ?: "))
trip.append(input("What adventurous sport did you do there ?: "))
trip.append(input("What is there to see ?: "))
trip.append(input("What's the fav food over there ?: "))
trip.append(input("What are the natives proud of ?: "))
trip.append(input("What do the people love to do in sun ?: "))
trip.append(input("Where do they swim ?: "))
trip.append(input("Overall, how was your trip ?: "))
story = "{}".format(mlg_header_files.tell_story(trip))
print(story)
