import React, { useEffect, useRef, useState } from 'react';
import ComparisonSlider from './ComparisonSlider/ComparisonSlider';
import Chip from '@mui/material/Chip';
import DatePicker from "react-datepicker"; import { DateRangePicker } from 'react-date-range';
import 'react-date-range/dist/styles.css'; // main style file
import 'react-date-range/dist/theme/default.css'; // theme css file
import DeckGL from '@deck.gl/react';
import { LineLayer } from '@deck.gl/layers';
import { StaticMap } from 'react-map-gl';
import { GeoJsonLayer } from '@deck.gl/layers';
let websocket;
let zoomLevel;
let timespan;
let selectedLocation;
// Set your mapbox access token here
const MAPBOX_ACCESS_TOKEN = 'pk.eyJ1Ijoic2lkZGhhcnRoODgwMCIsImEiOiJjbHE5MHdnOHgxZmg5MnFrenAycTA3ZGwzIn0.tdYy4ei04LqwpdExhGebqA';

// Viewport settings
const INITIAL_VIEW_STATE = {
  longitude: -98.5795,
  latitude: 39.8283,
  zoom: 3,
  pitch: 30,
  bearing: 0
};

// Data to be used by the LineLayer
const data = [
  { sourcePosition: [-122.41669, 37.7853], targetPosition: [-122.41669, 37.781] }
];

function initializeMap(mapRef, credentials) {
  const map = new Microsoft.Maps.Map(mapRef.current, { credentials });
  // Get the initial zoom level
  let zoomLevel = map.getZoom();
  console.log('Initial zoom level:', zoomLevel);
  Microsoft.Maps.Events.addHandler(map, 'click', function (e) {
    map.entities.clear();
    var pin = new Microsoft.Maps.Pushpin(e.location);
    map.entities.push(pin);
    console.log(e.location);
    if (websocket.readyState === WebSocket.OPEN) {
      selectedLocation = e.location;
      websocket.send(JSON.stringify({
        startDate: timespan.startDate,
        endDate: timespan.endDate,
        location: e.location,
        zoomLevel: zoomLevel
      }))
    }
    e.handled = true;
  });
  // Add a viewchange event handler
  Microsoft.Maps.Events.addHandler(map, 'viewchange', function () {
    zoomLevel = map.getZoom();
  });
  // Add a viewchangeend event handler
  Microsoft.Maps.Events.addHandler(map, 'viewchangeend', function () {
    const center = map.getCenter();
    console.log('Map center:', center);
    map.entities.clear();
    var pin = new Microsoft.Maps.Pushpin(center);
    map.entities.push(pin);
    console.log(center);
    if (websocket.readyState === WebSocket.OPEN) {
      selectedLocation = center;
      websocket.send(JSON.stringify({
        startDate: timespan.startDate,
        endDate: timespan.endDate,
        location: center,
        zoomLevel: zoomLevel
      }))
    }
  });
  return map;
}

function geocodeQuery(map, query, searchManager) {
  if (!searchManager) {
    Microsoft.Maps.loadModule('Microsoft.Maps.Search', function () {
      searchManager = new Microsoft.Maps.Search.SearchManager(map);
      geocodeQuery(map, query, searchManager);
    });
  } else {
    let searchRequest = {
      where: query,
      callback: function (r) {
        if (r && r.results && r.results.length > 0) {
          map.entities.clear();
          var pin = new Microsoft.Maps.Pushpin(r.results[0].location);
          map.entities.push(pin);
          map.setView({ bounds: r.results[0].bestView });
          console.log(r.results[0].location);
          if (websocket.readyState === WebSocket.OPEN) {
            selectedLocation = r.results[0].location;
            websocket.send(JSON.stringify({
              startDate: timespan.startDate,
              endDate: timespan.endDate,
              location: r.results[0].location,
              zoomLevel: zoomLevel
            }))
          }
        }
      },
      errorCallback: function (e) {
        alert("No results found.");
      }
    };
    searchManager.geocode(searchRequest);
  }
}

function App() {
  const mapRef = useRef(null);
  const [monthsToShow, setMonthsToShow] = useState(window.innerWidth < 768 ? 1 : 2);
  const [location, setLocation] = useState('');
  const [ws, setWs] = useState(null);
  const [timeoutId, setTimeoutId] = useState(null);
  const [timestamp, setTimestamp] = useState(Date.now());
  const [referenceImageSrc, setReferenceImageSrc] = useState('/static/vite.svg');
  const [modifiedImageSrc, setModifiedImageSrc] = useState('/static/react.svg');
  const [isFocused, setIsFocused] = useState(false);
  const [cards, setCards] = useState([]);
  const [showDeckGL, setShowDeckGL] = useState(false);
  const [showComparison, setShowComparison] = useState(false);
  const [deckGLData, setDeckGLData] = useState(null);
  const [startDate, setStartDate] = useState(new Date());
  const tenDaysAgo = new Date();
  tenDaysAgo.setDate(tenDaysAgo.getDate() - 10);
  const [dateRange, setDateRange] = useState({
    startDate: tenDaysAgo,
    endDate: new Date(),
    key: 'selection'
  });
  timespan = dateRange;
  const connectWebSocket = () => {
    if (!websocket || websocket.readyState === WebSocket.CLOSED) {
      websocket = new WebSocket('ws://localhost:8000/test/');

      websocket.onopen = () => {
        console.log('WebSocket is connected.');
        clearTimeout(timeoutId);
      };

      websocket.onmessage = (event) => {
        console.log('Received: ' + event.data);
        const message = JSON.parse(event.data);

        if (message.status === 'image_generated') {
          const newCards = [];
          message.type.forEach((type) => {
            if (type.IsCard === false) {
              if (type.Name === 'Reference') {
                if (type.URL === null) {
                  setShowComparison(false);
                } else {
                  setShowComparison(true);
                  setReferenceImageSrc(`/static/${type.URL}`);
                }
              } else if (type.Name === 'Modified') {
                if (type.URL === null) {
                  setShowComparison(false);
                } else {
                  setShowComparison(true);
                  setModifiedImageSrc(`/static/${type.URL}`);
                }
              }
            } else if (type.IsCard === true) {
              console.log(type);
              newCards.push(type);
            }
          });
          setCards(newCards);
          console.log('Updated images');
          if (message.data === null) {
            setShowDeckGL(false);
          } else {
            setShowDeckGL(true);
            setDeckGLData(message.data);
          }
        }
      };

      websocket.onclose = (event) => {
        console.log('WebSocket is closed. Reconnect will be attempted in 1 second.', event.reason);
        setTimeoutId(setTimeout(connectWebSocket, 1000));
      };

      websocket.onerror = (err) => {
        console.error('WebSocket encountered error: ', err.message, 'Closing socket');
        websocket.close();
      };
      setWs(websocket);
    }
  };

  useEffect(() => {
    const handleResize = () => {
      setMonthsToShow(window.innerWidth < 768 ? 1 : 2);
    };
    window.addEventListener('resize', handleResize);
    const script = document.createElement('script');
    script.src = 'http://www.bing.com/api/maps/mapcontrol?callback=getMap';
    script.async = true;
    document.body.appendChild(script);

    let map, searchManager;

    window.getMap = function () {
      map = initializeMap(mapRef,
        'API KEY'
        // 'Aj550yTjbKBN4nBv_EL-dAca-Jvgwf-5JIh60nsRZCg58edLANZuvcacRP4OKmmK'
      );
    };

    window.geocodeQuery = function (query) {
      geocodeQuery(map, query, searchManager);
    };
    connectWebSocket();
    return () => {
      document.body.removeChild(script);
      websocket.close();
      clearTimeout(timeoutId);
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const handleSearch = () => {
    window.geocodeQuery(location);
  };
  const handleVoiceSearch = () => {
    setIsFocused(true);
    const recognition = new window.webkitSpeechRecognition();
    recognition.onresult = (event) => {
      setLocation(event.results[0][0].transcript);
      setIsFocused(false);
    };
    recognition.start();
  };

  const [state, setState] = useState([
    {
      startDate: new Date(),
      endDate: null,
      key: 'selection'
    }
  ]);

  const onClick = info => {
    if (info.object) {
      alert(info.object.properties.Name);
    }
  }
  const layers = [
    new GeoJsonLayer({
      id: 'nationalParks',
      data: deckGLData,
      filled: true,
      pointRadiusMinPixels: 5,
      pointRadiusScale: 2000,
      getPointRadius: f => 5,
      getFillColor: data => data.properties.Name.includes("National Park") ? [250, 0, 0, 250] : [86, 144, 58, 250],
      pickable: true,
      autoHighlight: true,
      onClick
    }),
  ];
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      <div
        style={{
          position: 'relative',
          display: 'inline-flex',
          backgroundColor: 'rgba(255, 255, 255, 0.5)',
          backdropFilter: 'blur(10px)',
          borderRadius: '20px',
          border: '1px solid rgba(255, 255, 255, 0.2)',
          transition: 'all 0.3s ease',
          transform: isFocused ? 'scale(1.05)' : 'scale(1)',
          boxShadow: isFocused ? '0 5px 15px rgba(0,0,0,0.3)' : '0 5px 15px rgba(0,0,0,0.1)'
        }}
      >
        <button
          onClick={handleVoiceSearch}
          style={{
            padding: '10px',
            fontSize: '16px',
            backgroundColor: 'transparent',
            color: '#008CBA',
            border: 'none',
            cursor: 'pointer'
          }}
        >
          <i class="fa fa-microphone"></i>
        </button>
        <input
          id="location"
          type="text"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          style={{
            padding: '10px',
            fontSize: '16px',
            paddingLeft: '40px',
            paddingRight: '40px',
            backgroundColor: 'transparent',
            borderRadius: '20px',
            border: 'none',
            outline: 'none'
          }}
          placeholder="Location"
          onFocus={() => setIsFocused(true)}
          onBlur={() => setIsFocused(false)}
        />
        <button
          onClick={handleSearch}
          style={{
            padding: '10px',
            fontSize: '16px',
            backgroundColor: 'transparent',
            color: '#4CAF50',
            border: 'none',
            cursor: 'pointer'
          }}
        >
          <i class="fa fa-search"></i>
        </button>
      </div>
      <DateRangePicker
        onChange={item => {
          setDateRange(item.selection);
          if (item.selection.startDate.getTime() !== item.selection.endDate.getTime()) {
            timespan = item.selection;
            websocket.send(JSON.stringify({
              startDate: item.selection.startDate,
              endDate: item.selection.endDate,
              location: selectedLocation,
              zoomLevel: zoomLevel
            }))
          }
        }}
        showSelectionPreview={true}
        moveRangeOnFirstSelection={false}
        months={monthsToShow}
        ranges={[dateRange]}
        direction="horizontal"
      />
      <div className="container">
        <div className="locationPicker" ref={mapRef} style={{
          width: '90vw',
          height: '90vw',
          marginTop: '20px',
          marginBottom: '20px', // Add space below the map
          borderRadius: '25px',
          boxShadow: '0 0 10px rgba(0, 0, 0, 0.2)',
          overflow: 'hidden'
        }} />
        <ComparisonSlider
          imageBefore={referenceImageSrc}
          imageAfter={modifiedImageSrc}
          style={{
            marginTop: '20px', // Add space above the comparison slider
            margin: '20px',
            boxShadow: '0 0 20px rgba(0, 0, 0, 0.3)',
            borderRadius: '25px',
            overflow: 'hidden'
          }}
        />
      </div>
      <div className="chip-container">
        {cards.map((card, index) => (
          <Chip
            key={index}
            label={card.Name}
            clickable
            color="primary"
          />
        ))}
      </div>
      {showDeckGL && (
        <div style={{
          height: '90vw', width: '90vw', position: 'relative', boxShadow: '0 0 20px rgba(0, 0, 0, 0.3)',
          borderRadius: '25px',
          overflow: 'hidden'
        }}>
          <DeckGL initialViewState={INITIAL_VIEW_STATE} controller={true} layers={layers} >
            <StaticMap mapStyle="mapbox://styles/mapbox/dark-v9" mapboxApiAccessToken={MAPBOX_ACCESS_TOKEN} />
          </DeckGL>
        </div>
      )}
    </div>
  );
}

export default App;
