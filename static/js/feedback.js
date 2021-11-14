var body = document.getElementById("body");
body.setAttribute("oncontextmenu", "return false");
body.setAttribute("onkeydown", "return false");
body.setAttribute("onmousedown", "return false")



function check(input)
{
    var correct = document.getElementById("answerCorrect");
    var label_input = document.getElementById("id_" + input.value)
    var label_correct = document.getElementById("id_" + correct.value)
    var list_input = document.getElementsByName("answer")

    if(input.value ==  correct.value)
    {
        label_input.className = "text-success";
    }
    else
    {
        label_input.className = "text-danger";
        label_correct.className = "text-success";
    }
    for(answer of list_input)
    {
        if(answer != input)
        {
            answer.setAttribute('disabled', true);
        }
    }

}
