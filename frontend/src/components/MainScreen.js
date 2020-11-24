import React, {useState, useEffect} from "react";
import axios from "axios";
import TextField from "@material-ui/core/TextField"
import Button from "@material-ui/core/Button"
import Select from "@material-ui/core/Select"
import MenuItem from "@material-ui/core/MenuItem"

export default function ExampleComponent(props){
   const [tags, setTags]  = useState([])
   const [items, setItems] = useState([])
   const [selectedTag, setSelectedTag] = useState(null)
   const [newItemName, setNewItemName] = useState("")
   const [newTagName, setNewTagName] = useState("")

   function addItem(){
     const item = {item_name : newItemName, tag_name :selectedTag}
     axios.post("http://localhost:5000/items_add", item)
      .then(response => {
        setItems([...items, item])
        setNewItemName("");
        setSelectedTag("")
      }
      )
      .catch(error => console.log(error))
   }

   function addTag(){
    const tag = {tag_name : newTagName}
    axios.post("http://localhost:5000/tags_add", tag)
     .then(response => {
       setTags([...tags, tag])
       setNewTagName("");
     }
     )
     .catch(error => console.log(error))
  }

   useEffect(() => {
     console.log("intial request!")
      axios.get("http://localhost:5000/tags_all")
        .then(response => setTags(response.data))
        .catch(error => console.log(error));

      axios.get("http://localhost:5000/items_all")
        .then(response => {
          setItems(response.data)
        console.log(response)})
        .catch(error => console.log(error));

   }, []);

   //display all the items
   //drop down showing all the tags
   //input cell for item name
   //

   return (
    <>
    <div>
      <TextField 
        label = "New Item"
        value = {newItemName}
        onChange = {(event) => setNewItemName(event.target.value)}
      ></TextField>


      <Select
        value = {selectedTag}
        onChange = {(event) => setSelectedTag(event.target.value)}
      >
        {tags.map((tag)=><MenuItem value = {tag.tag_name}>{tag.tag_name}</MenuItem>)}
      </Select>

      <Button
        onClick = {addItem}
        disabled = {newItemName == ""}
      >
        Add Item
      </Button>
    </div>


    <div>
      <TextField 
        label = "New Tag"
        value = {newTagName}
        onChange = {(event) => setNewTagName(event.target.value)}
      ></TextField>

      <Button
        onClick = {addTag}
        disabled = {newTagName == ""}
      >
        Add Tag
      </Button>

    </div>


      <h1>Items</h1>
      {items.map((item) => 
        <p>{item.item_name}</p>
      )}

    </>
  );
}



