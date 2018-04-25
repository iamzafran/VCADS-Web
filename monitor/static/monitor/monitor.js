var markerArray = [];

function initMap(){
        var uluru = {lat: -25.363, lng: 131.044};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: uluru
        });

        console.log("Map");

        firebase.auth().onAuthStateChanged(function(user) {
          if (user) {
            // User is signed in.
            var isAnonymous = user.isAnonymous;
            var uid = user.uid;
            console.log(isAnonymous);




            var firebaseRef = firebase.database().ref('vehicle_location');
        var geoFire = new GeoFire(firebaseRef);

        var geoQuery = geoFire.query({
          center: [1.532048, 103.577093],
          radius: 100.5
        });



        var onKeyEnteredRegistration = geoQuery.on("key_entered", function(key, location, distance) {
            console.log(key + " entered query at " + location + " (" + distance + " km from center)");
            var latitude = location[0];
            var longitude = location[1];
            console.log(latitude);
            console.log(longitude);
            var vehicle_location = {lat: latitude, lng: longitude};

            var marker = new google.maps.Marker({
                  position: vehicle_location,
                  map: map,
                  speed: 0,
                  track: 0,
                  license_number: key

             });

             marker.addListener('click', function(){
                console.log(this.speed+"");
                console.log(this.track+"");
                console.log(this.position+"");
                console.log(this.license_number+"");

                var vehicleRef = firebase.database().ref('vehicle_data/'+this.license_number);
                var vehicleLocationRef = firebase.database().ref('vehicle_location/'+this.license_number+"/l");


                vehicleRef.on('value', function(snapshot) {
                    console.log(snapshot.val());
                    var data = snapshot.val();
                    marker.speed = data.speed;
                    marker.track = data.track;

                    $('#speed').text(data.speed+"");
                    $('#track').text(data.track+"");

                });

                vehicleLocationRef.on('value', function(snapshot) {
                    var data = snapshot.val();
                    latitude = data[0];
                    longitude = data[1];
                    console.log(latitude+" ,"+longitude);
                    $('#latitude').text(latitude+"");
                    $('#longitude').text(longitude+"");

                });




             });

             var vehicleDataRef = firebase.database().ref('vehicle_data/'+key);

             vehicleDataRef.on('value', function(snapshot) {
                console.log(snapshot.val());
                var data = snapshot.val();
                marker.speed = data.speed;
                marker.track = data.track;
             });

             markerArray[key] = marker;
        });

        var onKeyMovedRegistration = geoQuery.on("key_moved", function(key, location, distance) {
            var marker = markerArray[key];
            var latitude = location[0];
            var longitude = location[1];
            var vehicle_location = {lat: latitude, lng: longitude};
            marker.setPosition(vehicle_location);
        });

          } else {

          }

        });


}


