function test() {
  console.log("hi..")
}



val = (x) => {
  document.getElementById("output").value += document.getElementById(x).innerText;
};



function clearOut() {
  document.getElementById("output").value = "";
}



let elem = document.querySelectorAll(".calculator__key--operator");
elem.forEach(op => {
  op.addEventListener("click", (e) => {
    if (e.target.value == "+") {
      console.log("found value is +");
    }
  })
})


let x = document.querySelectorAll(".calculator__key");
x.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    console.log(e.target);
    console.log("Value: " + e.target.value);
  })
})