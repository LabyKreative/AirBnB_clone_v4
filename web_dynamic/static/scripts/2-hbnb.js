// This code block ensures that the JavaScript runs once the DOM is fully loaded and ready.
$(document).ready(function () {
  // Initialize an object to store the selected amenities.
  let checkedAmenities = {};

  // Attach a change event handler to all checkboxes.
  $(document).on('change', "input[type='checkbox']", function () {
    if (this.checked) {
      // If checkbox is checked, add the corresponding amenity to the object.
      checkedAmenities[$(this).data('id')] = $(this).data('name');
    } else {
      // If checkbox is unchecked, remove the corresponding amenity from the object.
      delete checkedAmenities[$(this).data('id')];
    }

    // Extract values from the object and create an array.
    let lst = Object.values(checkedAmenities);

    if (lst.length > 0) {
      // If there are selected amenities, display them in the associated <h4> element.
      $('div.amenities > h4').text(Object.values(checkedAmenities).join(', '));
    } else {
      // If no amenities are selected, display a non-breaking space in the <h4> element.
      $('div.amenities > h4').html('&nbsp;');
    }
  });

  // Perform an AJAX GET request to retrieve the API status information.
  $.get('http://0.0.0.0:5003/api/v1/status/', function (data, textStatus) {
    // Check if the request was successful.
    if (textStatus === 'success') {
      // Check if the API status is 'OK'.
      if (data.status === 'OK') {
        // If the API is available, add the 'available' class to the designated element.
        $('#api_status').addClass('available');
      } else {
        // If the API is not available, remove the 'available' class from the designated element.
        $('#api_status').removeClass('available');
      }
    }
  });
});
