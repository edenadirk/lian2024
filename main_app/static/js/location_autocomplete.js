document.addEventListener('DOMContentLoaded', function() {
    var input = document.getElementById('id_location');
    var autocomplete = new google.maps.places.Autocomplete(input);

    autocomplete.addListener('place_changed', function() {
        
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }

        // You can access additional place details here if needed
        // For example: place.formatted_address, place.geometry.location.lat(), place.geometry.location.lng()
    });
});