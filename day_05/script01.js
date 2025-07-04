var selectedRow = null;{
function onFormSubmit() {
var sdata = readFormData();
if(isValid()){
    if (selectedRow == null)wRecord(sdata);
    alert("Your details are saved Sucessfully........");
  }
 else{
  updateRecord(sdata);
 }
  resetForm();
}
}
function readFormData() {
    var data = {};
    data["Name"] = parseInt(document.getElementById("Name").value);
    data["College"] = parseInt(document.getElementById("College").value);
    data["course"] = parseInt(document.getElementById("course").value);
    return data;
}
function reset(){
    document.getElementById("Name").value = "";
    document.getElementById("College").value = "";
    document.getElementById("course").value = "";
     selectedRow = null;
}
function insertNewRecord(data){
    var table = document.getElementById("slist").getElementsByTagName("tbody")[0];
    var newRow = table.insertRow(table.length);
    cell1=newRow.insertCell(0);
    cell1.innerHTML=data.Name;
 cell2=newRow.insertCell(1);
    cell2.innerHTML=data.College;
 cell3=newRow.insertCell(2);
    cell3.innerHTML=data.course;
    cell4=newRow.insertCell(3);
    cell4.innerHTML=`<a onClick="onEdit(this)">Update</a><a onClick="onDelete(this)">Delete</a>`;
}




