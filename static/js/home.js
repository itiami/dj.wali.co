function changeFn(x) {
  var Sel_Ind = document.getElementById(x).selectedIndex;
  var popUrl = document.getElementById(x).options[Sel_Ind].value;
  winpops = window.open(popUrl, targes = '_self');
}

function dt() {
  let d = new Date();
  timeNow = d.toLocaleTimeString('fr-FR', { timeZone: 'Europe/Paris' });
  document.getElementById("date").innerText = timeNow;
}

setInterval(() => {
  dt();
}, 1000);


// image rotation
(() => {
  document.getElementById("img").addEventListener("mousemove", () => {
    document.getElementById("img").style.transform = "rotate(90deg)";
    document.getElementById("img").style.transition = "2s";
  })

  document.getElementById("img").addEventListener("mouseout", () => {
    document.getElementById("img").style.transform = "rotate(0deg)";
    document.getElementById("img").style.transition = "2s";
  })

})();


// window.onload = function () {
//   const navItems = document.querySelectorAll('#navbar li');

//   for (const item of navItems) {
//     item.addEventListener('mouseenter', function () {
//       const dropdown = this.querySelector('.dropdown');
//       if (dropdown) {
//         dropdown.style.display = 'block';
//       }
//     });

//     item.addEventListener('mouseleave', function () {
//       const dropdown = this.querySelector('.dropdown');
//       if (dropdown) {
//         dropdown.style.display = 'none';
//       }
//     });
//   }
// };


// $(document).ready(function () {
//   $('.dropdown-submenu a.test').on("click", function (e) {
//     $(this).next('ul').toggle();
//     e.stopPropagation();
//     e.preventDefault();
//   });
// });