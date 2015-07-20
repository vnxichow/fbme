import facebook

print "Hi, I'm a status updater!"

# developers.facebook.com/tools/explorer to get a test token w/correct permissions
token = "your token here"
graph = facebook.GraphAPI(token)

# ask the user for their status
status = raw_input("What do you want your status to be?")

#post the status
graph.put_object(parent_object='me', connection_name='feed',
                 message=status)
