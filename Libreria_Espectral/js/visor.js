
			var map = new ol.Map({ 
			   layers: [ 
				 new ol.layer.Tile({ 
					source: new ol.source.OSM() 
				 }) 
			   ], 
			   target: 'map', 
			   view: new ol.View({ 
				 center: [0, 0], 
				 zoom: 2 
			   }) 
			});

			var view = new ol.View({
			   center: [41.56, -4.63],
			   zoom: 7
			});

			var view = new ol.View({
			   center: [41.56, -4.63],
			   zoom: 7
			});
			
			map.addControl(new ol.control.ZoomSlider()); 