// to capture value using id
function getValueById() {
    let inputValue = "First Name: " + document.getElementById("fname").value;
    document.getElementById("output").innerHTML = inputValue;
}

// to get the value using classname. which needs to be treated as array..
function getValueByClassName() {
    let inputValue = document.getElementsByClassName("form-control")[0].value;
    document.getElementById("output").innerHTML = inputValue;
}

// self invoked Method_1
(function () {
    let output = document.getElementById("output");
    document.getElementById("jsBtn").addEventListener(
        "click", () => {
            console.log(list);
            output.innerHTML = list;
        })
})();


// self invoked Method_2
(() => {
    const inputs = document.querySelectorAll("input[name=symb]");

    inputs.forEach((elem) => {
        //console.log(elem.id);
        elem.addEventListener("click", (() => {
            console.log(elem.id);
            document.getElementById("output").innerHTML = elem.id;
        }))
    })
})();

// using Axios CDN XMLHttpRequest....


