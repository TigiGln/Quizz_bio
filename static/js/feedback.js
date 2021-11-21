//blocking the inspector when on the quiz 
var body = document.getElementById("body");
body.setAttribute("oncontextmenu", "return false");
body.setAttribute("onkeydown", "return false");
body.setAttribute("onmousedown", "return false")



function check(input)
/*
Function to manage quiz feedback when an answer is clicked

:parameter:
    input: html object
        radio button clicked to select its answer

:return:
    Changing the colour according to the correct answer and changing the score
*/
{
    //recovery answer correct
    var correct = document.getElementById("answerCorrect");
    //recovery label input
    var label_input = document.getElementById("id_" + input.value);
    //recovery label answer correct
    var label_correct = document.getElementById("id_" + correct.value);
    //recovery radio button set
    var list_input = document.getElementsByName("answer");
    //recovery old score
    var score = document.getElementById("score")
    score_display = parseInt(score.textContent.split(" ")[0]);
    //recovery question points
    var points_question = parseInt(document.getElementById("point").value);

    //display of the colour according to the answer given
    if(input.value ==  correct.value)
    {
        label_input.className = "text-success";
        newScore = score_display + points_question;
        score.innerHTML = newScore + " points";
    }
    else
    {
        label_input.className = "text-danger";
        label_correct.className = "text-success";
        newScore = score_display - points_question;
        score.innerHTML = newScore + " points";
    }
    //disabled radio button after having answered
    for(answer of list_input)
    {
        if(answer != input)
        {
            answer.setAttribute('disabled', true);
        }
    }

}
