# Ashish chime-fullstack-project fork

Hey! Tried to hold myself to a 3-4 hour timeframe to see how much I could get done in a realistic situation.  With a bit more time, theres a few changes I would make:

React:
  1. Create seperate components for AddItem, AddTag, and MenuList.  
  2. Keep tagList and itemList as shared state in MainScreen, passing down to components as props. 
  3. Keep API-calling functions for adding tags and adding items in MainScreen, passing down to components as props.
  4. Maintain state of input fields in individual components.    
  
 UI:
 1. Add Flexbox for each component to center vertically and horizontally
 2. Use Materials UI Grid to create layout and add some padding between components
 3. Clean up the CSS for input fields and button, make MenuList scrollable
 
 Back-end:
 1. Make tag_name field "unique = True" in model.  Check for duplicate in Tag POST route.
 2. Not using Marshmallow for serializing.
 
To be honest, I dont have a ton of experience using SQLALchemy. Spent a good chunk of time debugging some issues with that.  If you guys do have the oppurtunity for some back-end work, I could defintely study up on the docs and work some examples on my own to get up to speed.
 

