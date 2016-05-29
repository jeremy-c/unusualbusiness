/* ==|====================
   Module/Mobile Menu
   ======================= */

'use strict';

// import {default as L} from 'leaflet';
// import 'leaflet-geosearch';
// import GoogleMapsAPI from 'googlemaps';

let Organization = () => {

  let initLeaflet = function() {
    let org_location_map = L.map('leaflet').setView([51.505, -0.09], 13);//.setView([0, 0], 2);
    let addressText = 'Amsterdam';
    let geo_search_provider = new L.GeoSearch.Provider.Esri();

    new L.Control.GeoSearch({
        provider: geo_search_provider,
        position: 'topcenter',
        showMarker: true,
        retainZoomLevel: false
    }).addTo(org_location_map);

    geo_search_provider.GetLocations( addressText, function ( data ) {
      // in data are your results with x, y, label and bounds (currently availabel for google maps provider only)
    });
  };

  let initGmaps = function() {
    // var publicConfig = {
    //   key: 'AIzaSyAwN3OewMWFunrZb6C5RC_T3VjEcEZ9hVo',
    //   stagger_time:       1000, // for elevationPath
    //   encode_polylines:   false,
    //   secure:             true // use https
    //   // proxy:              'http://127.0.0.1:9999' // optional, set a proxy for HTTP requests
    // };
    // var gmAPI = new GoogleMapsAPI(publicConfig);
    //
    // // geocode API
    // var geocodeParams = {
    //   "address":    "Utrecht, the Netherlands",
    //   // "components": "components=country:NL",
    //   // "bounds":     "55,-1|54,1",
    //   // "language":   "nl",
    //   // "region":     "nl"
    // };
    //
    // gmAPI.geocode(geocodeParams, function(err, result){
    //   console.log(result);
    // });
  };

  let init = function() {
    // initLeaflet();
    initGmaps();
  };

  return {
    init: init
  };
};

export default Organization;
