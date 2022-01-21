//* Цикл через все кнопки выпадающего списка для переключения между скрытием и отображением его выпадающего содержимого -
// это позволяет пользователю иметь несколько выпадающих списков без каких-либо конфликтов */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}