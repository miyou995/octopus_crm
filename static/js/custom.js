/**
 *
 * You can write your JS code here, DO NOT touch the default style file
 * because it will make it harder for you to update.
 * 
 */
 "use strict";

 
        
 function onButtonPress() {
  $('.alert').alert('close');
}   

function additem() {
  var table = document.getElementById("mytable");
  var row = table.insertRow(-1);
  var cell0 = row.insertCell(0);
  var cell1 = row.insertCell(1);
  var cell2 = row.insertCell(2);
  var cell3 = row.insertCell(3);
  var cell4 = row.insertCell(4);
  cell0.innerHTML = "NEW CELL1";
  cell1.innerHTML = "NEW CELL2";  
  cell2.innerHTML = "NEW CELL2";  
  cell3.innerHTML = "NEW CELL2";   
  cell4.innerHTML = "NEW CELL2";      
}