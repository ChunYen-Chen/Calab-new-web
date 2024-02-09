function filterItemsById() {
// check if one of the checkboxed is checked
  const checkboxes = document.querySelectorAll('input[type="checkbox"]');
  const items      = document.querySelectorAll('.publication');

// 1. initilize to none
  items.forEach(item => {
    item.style.display = 'none';
  });

// 2. display by selected
  let oneChecked = false;
  checkboxes.forEach(function (checkbox) {
    if ( checkbox.checked ) {oneChecked = true;}
    items.forEach(item => {
      const itemTags = item.getAttribute('data-tags').split(' ');

      if (checkbox.checked && itemTags.includes(checkbox.id)) {
        item.style.display = 'block';
      }
    });
  });

// 3. display all if none is selected
  if ( !oneChecked ) {
    items.forEach(item => {
      const itemTags = item.getAttribute('data-tags').split(' ');

        item.style.display = 'block';
    });
  }
}

