//  Create the button
var escapeButton = document.createElement("button");


//add the escape button class
escapeButton.className = "escapeButtonClass";

//  Append somewhere
var body = document.getElementsByTagName("body")[0];
body.appendChild(escapeButton);

//  Add event handler
escapeButton.addEventListener ("click", function() {
  window.location.href = "https://google.com";
});

// Add styles for the button
document.querySelector(".escapeButtonClass").style.cssText = "position: fixed; right: 1.84615rem; top: 1.84615rem; width: 8.30769rem; border: none; float: right; color: lightgray; border-radius: 12px; background-color: #881e1e; height: 4.5rem";
document.querySelector(".escapeButtonClass").innerHTML = 'Quick Escape';
    
