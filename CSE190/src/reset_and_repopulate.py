
# These random comments are for my end; apparently eclipse require them. Just leave them.
print ("Deleting tables...")
execfile("script_table_reset.py")  # @UndefinedVariable

print ("Filling members...")
execfile("script_table_filling_members.py")  # @UndefinedVariable
print ("Filling friends...")
execfile("script_table_filling_friends.py")  # @UndefinedVariable
print ("filling topics...")
execfile("script_table_filling_topics.py")  # @UndefinedVariable
print ("filling posts...") 
execfile("script_table_filling_posts.py")  # @UndefinedVariable
print ("filling views...")
execfile("script_table_filling_view.py")  # @UndefinedVariable