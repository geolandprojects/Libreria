const mapContainer = document.querySelector('.map-container');
const map = L.map(mapContainer).setView([51.505, -0.09], 13);

const osm = createOsmLayer();
const marker = createMarker();

map
	.addLayer(osm)
  .addLayer(marker)
  .addControl(createLayersControl({ OpenStreetMap: osm }, { Markers: marker }));

////////////

function createOsmLayer() {
	return L.tileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { noWrap: true });
}

function createMarker() {
	return L.marker([51.5, -0.09])
  	.bindPopup('<b>Hello world!</b><br>I am a popup.')
    .bindTooltip('my tooltip text');
}

function createLayersControl(baseLayers, overlays) {
	return L.control.layers(baseLayers, overlays);
}
