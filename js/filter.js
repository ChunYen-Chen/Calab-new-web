let but_year = document.getElementById("filter-year");
let item_year = document.getElementById("filter-year-list");

function UpdateFilter( but, item ) {
//  expect there is only one children in button
    if (but.value == 'true') {
        but.value = 'false';
        item.style.display = 'none';
        but.children[0].classList.add('fa-rotate-90');
    } else {
        but.value = 'true';
        item.style.display = 'block';
        but.children[0].classList.remove('fa-rotate-90');
    }
}

UpdateFilter( but_year, item_year );

document.addEventListener('DOMContentLoaded', function () {
    but_year.addEventListener('click', function () {
        UpdateFilter( but_year, item_year );
    });
});
