print "Deleting tables..."
execfile("script_table_reset.py")

print "Filling members..."
execfile("script_table_filling_members.py")
print "Filling friends..."
execfile("script_table_filling_friends.py")
print "filling topics..."
execfile("script_table_filling_topics.py")
print "filling posts..."
execfile("script_table_filling_posts.py")
print "filling views..."
execfile("script_table_filling_view.py")