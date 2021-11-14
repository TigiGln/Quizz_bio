listImages = JSON.parse(json_data);

function display_box(buttonImage)
{
    id = parseInt(buttonImage.id.split('_')[2])
    var modalContainer = document.createElement("div");
    modalContainer.setAttribute("id", "modal");
    if(id/3 > 1)
    {
        console.log("hello");
        modalContainer.className += "align-self-center";
        console.log(modalContainer.style);
        
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


    customBoxCol1.innerHTML = "<img src='" + baseUrl + "/media/" + listImages[id-1]['image_name'] + ".jpg' class='img_container img-fluid img-thumbnail w-100 h-100' alt='Non'>"
    customBoxCol2.innerHTML += "<h3>Microscopy:</h3>";
    customBoxCol2.innerHTML += "<p>" +  listImages[id-1]['microscopy'] + "<p>";
    customBoxCol2.innerHTML += "<h3>Description:</h3>";
    customBoxCol2.innerHTML += "<p>" +  listImages[id-1]['description'] + "<p>";
    if(listImages[id-1]['cell_type'] != "None")
    {
        customBoxCol2.innerHTML += "<h3>Cell type:</h3>";
        customBoxCol2.innerHTML += "<p>" +  listImages[id-1]['cell_type'] + "<p>";
    }
    if(listImages[id-1]['component'] != "None")
    {
        customBoxCol2.innerHTML += "<h3>Component:</h3>";
        customBoxCol2.innerHTML += "<p>" +  listImages[id-1]['component'] + "<p>";
    }
    if(listImages[id-1]['organism'] != "None")
    {
        customBoxCol2.innerHTML += "<h3>Organism:</h3>";
        customBoxCol2.innerHTML += "<p>" +  listImages[id-1]['organism'] + "<p>";
    }
    if(listImages[id-1]['organism'] != "None")
    {
        customBoxCol2.innerHTML += "<h3>DOI:</h3>";
        customBoxCol2.innerHTML += "<p>" +  listImages[id-1]['doi'] + "<p>";
    }
    
    customBoxRow.innerHTML += "<button id='modal_close' class='btn btn-lg btn-outline-dark w-25 my-3'>Close</button>";
    modalShow(modalContainer, customBox, customBoxRow);    
}

function modalShow(modalContainer, customBox, customBoxRow)
{
    var imagesContainer = document.getElementById("block_images");
    list_buttons = document.getElementsByClassName("See");
    customBox.appendChild(customBoxRow);
    modalContainer.appendChild(customBox);
    imagesContainer.appendChild(modalContainer);
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
{
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



