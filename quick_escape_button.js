//  Create the button
var escapeButton = document.createElement("button");
escapeButton.innerText = "Quick Escape";

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
document.querySelector(".escapeButtonClass").style.cssText = "position: fixed; right: 1.84615rem; top: 1.84615rem; height: 4.30769rem; width: 8.30769rem; background: #a60f2d; border: none; float: right; color: white; border-radius: 12px;"
