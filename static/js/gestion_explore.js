listImages = JSON.parse(json_data);


function display_box(buttonImage)
/*
management of the dialogue box allowing to visualize the information of the image

:parameter:
    buttonImage: HTML object
        retrieves the clicked button

:return:
    the dialogue box with the information
*/
{
    id=""
    //Retrieve the id of the image corresponding to the clicked button
    for (Img of listImages)
    {
        
        if(Img.image_id == parseInt(buttonImage.id.split('_')[2]))
        {
            console.log(Img)
            id = listImages.indexOf(Img)
        }
    }
    console.log(id)
    var modalContainer = document.createElement("div");
    modalContainer.setAttribute("id", "modal");
    if(id <= listImages.length/3)
    {
        modalContainer.className += "align-self-start";
    }
    else if(id >= listImages.length/3 && id <= listImages.length/3 * 2)
    {
        modalContainer.className += "align-self-center";
    }
    else
    {
        modalContainer.className += "align-self-end";
    }
    var customBox = document.createElement("div");
    customBox.className = "custom_box";
    var customBoxRow = document.createElement("div");
    customBoxRow.className="row";
    var customBoxCol1 = document.createElement("div");
    customBoxCol1.className="col-6";
    customBoxRow.appendChild(customBoxCol1);
    var customBoxCol2 = document.createElement("div");
    customBoxCol2.className="col-6";
    customBoxRow.appendChild(customBoxCol2);

    //add informations in the structure of the dialogue box
    customBoxCol1.innerHTML = "<img src='" + baseUrl + "/media/" + listImages[id]['image_name'] + ".jpg' class='img_container img-fluid img-thumbnail w-100 h-100' alt='Non'>"
    customBoxCol2.innerHTML += "<h3>Microscopy:</h3>";
    customBoxCol2.innerHTML += "<p>" +  listImages[id]['microscopy'] + "<p>";
    customBoxCol2.innerHTML += "<h3>Description:</h3>";
    customBoxCol2.innerHTML += "<p>" +  listImages[id]['description'] + "<p>";
    if(listImages[id]['cell_type'] != "None")
    {
        customBoxCol2.innerHTML += "<h3>Cell type:</h3>";
        customBoxCol2.innerHTML += "<p>" +  listImages[id]['cell_type'] + "<p>";
    }
    if(listImages[id]['component'] != "None")
    {
        customBoxCol2.innerHTML += "<h3>Component:</h3>";
        customBoxCol2.innerHTML += "<p>" +  listImages[id]['component'] + "<p>";
    }
    if(listImages[id]['organism'] != "None")
    {
        customBoxCol2.innerHTML += "<h3>Organism:</h3>";
        customBoxCol2.innerHTML += "<p>" +  listImages[id]['organism'] + "<p>";
    }
    if(listImages[id]['organism'] != "None")
    {
        customBoxCol2.innerHTML += "<h3>DOI:</h3>";
        customBoxCol2.innerHTML += "<p>" +  listImages[id]['doi'] + "<p>";
    }
    
    customBoxRow.innerHTML += "<button id='modal_close' class='btn btn-lg btn-outline-dark w-25 my-3'>Close</button>";
    modalShow(modalContainer, customBox, customBoxRow);    
}

function modalShow(modalContainer, customBox, customBoxRow)
/*
creation of the div and its children for the display of information

:parameter:
    modalContainer: HTML object
        div created
    customBox: HTML object 
        child of modalContainer
    customBoxRow: HTML object 
        child of customBox
*/
{
    var imagesContainer = document.getElementById("block_images");
    list_buttons = document.getElementsByClassName("See");
    customBox.appendChild(customBoxRow);
    modalContainer.appendChild(customBox);
    imagesContainer.appendChild(modalContainer);
    //disabled the buttons when the box is open
    for (button of list_buttons)
    {
        button.setAttribute("disabled", true);
    }
    var modal_close = document.getElementById('modal_close');
    location.href= "#modal";
    modal_close.addEventListener('click', function() {
        modalClose(modalContainer, list_buttons, imagesContainer);
    });

}

function modalClose(modalContainer, list_buttons, imagesContainer)
/*
remove of the div and its children

:parameter:
    modalContainer: HTML object
        div created
    list_buttons: list of HTML objects 
        set of button
    imagesContainer: HTML object 
       div containing all the images
*/
{
    //reactivation of the buttons after closing the dialogue box
    for (button of list_buttons)
    {
        button.removeAttribute("disabled");
    }
    while(modalContainer.hasChildNodes())
    {

        modalContainer.removeChild(modalContainer.firstChild);

    }
    imagesContainer.removeChild(modalContainer);
}



function show_search()
/*
display management of the search div

:parameter:
    None
*/
{
    var search = document.getElementById("collapseForm");
    if(search.style.display === "flex")
    {
        search.style.display = "none"
    }
    else
    {
        search.style.display = "flex"
    }
}





