document.getElementById("downloadBtn").addEventListener("click", async () => {
  const daysInput = document.getElementById("daysInput");
  const days = daysInput.value;

  try {
    const permissionStatus = await navigator.permissions.query({ name: 'geolocation' });
    if (permissionStatus.state === 'granted' || permissionStatus.state === 'prompt') {
      const position = await getCurrentPosition();
      const lat = position.coords.latitude;
      const long = position.coords.longitude;
      console.log(lat,long)
      //https://salatiapi-1-j5004120.deta.app/latLong/?lat=45&long=45&days=32
      const apiUrl = `https://salatiapi-1-j5004120.deta.app/latLong/?lat=${lat}&long=${long}&days=${days}`;
      console.log(lat,long,apiUrl)
      const response = await fetch(apiUrl);
      const data = await response.text();

      downloadCalendar(data, 'prayer-times-calendar.ics');
    } else {
      throw new Error('Location permission not granted');
    }
  } catch (error) {
    alert('Error: ' + error.message);
  }
});

function getCurrentPosition() {
  return new Promise((resolve, reject) => {
    navigator.geolocation.getCurrentPosition(resolve, reject, { enableHighAccuracy: true });
  });
}

function downloadCalendar(data, filename) {
  const blob = new Blob([data], { type: 'text/calendar;charset=utf-8;' });
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = filename;
  link.style.display = 'none';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
